import random
import os
import codecs
import sys
import csv
import re
from gtts import gTTS
from playsound import playsound
import win10toast

p = ""
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&"
passlen = 5
value = 0
p = "".join(random.sample(s, passlen))
for i in range(len(p)):
    value += ord(p[i])


def en_alg(inpAlp, temp):  # Encryption Algorithm
    return (inpAlp + value) - 250 + (2 + temp)


def de_alg(outAlp, temp, val):
    let = outAlp
    i = temp
    kvalue = val
    return let - 2 - i + 250 - kvalue


def operation(choise):  # Encryption Output Result
    if choise == 1:
        os.system('cls')
        inp = str(input("Data Input: "))
        os.system('cls')
        print("Encryption Key: " + p)
        print("")
        print("Encrypted Data: ", end="")
        encryptor(inp)
        print("")
        print(" Location: C:\\Users\\Public\\Documents\\En_De_Data\\" + p + ".txt")
        ex = input("Key and Saved to the Location. Press Enter to Close!")

    elif choise == 2:
        os.system('cls')
        key = str(input("Enter Encryption File Name: "))
        decryptor(key)
        print("")
        ex = input("Copy your info. Press Enter to Close!")
    elif choise == 3:
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        print("It's your choise make it correct! -_-")
        mainMenu()


def encryptor(data):  # Encryption Function
    temp = []
    for i in range(len(data)):
        let = ord(data[i])
        inp = chr(en_alg(let, i))
        temp.insert(i, inp)

    for i in range(len(temp)):
        print(temp[i], end="")
    write_file(temp, p)


def write_file(data, pin):  # File Wright
    file_name = 'C:\\Users\\Public\\Documents\\En_De_Data\\' + p + '.txt'
    with open(file_name, 'w', encoding='utf8') as x_file:
        x_file.write('')
        for i in range(len(data)):
            x_file.write('{}'.format(data[i]))


def read_file(name):  # Read File
    value = name
    temp = 'C:\\Users\\Public\\Documents\\En_De_Data\\' + value + '.txt'
    file_name = temp
    File_object = open(temp, "r", encoding='utf8')
    return (File_object.read())


def decryptor(key):  # Decryption Function
    temp = []
    kvalue = 0
    print("Data: ", end="")
    notification("Decryption Successfull!")
    data = read_file(key)
    for i in range(len(key)):
        kvalue += ord(key[i])
    for i in range(len(data)):
        let = ord(data[i])
        temp.insert(i, chr(de_alg(let, i, kvalue)))

    for i in range(len(temp)):
        print(temp[i], end="")
    print("")

    write_file_Audio(temp, key)
    print("Want to listen Audio?")
    req = ord(input("If yes press 'y' and enter: "))
    if req == ord('y'):
        audio_play(key)
    else:
        print("Thank You")


def write_file_Audio(data, pin):  # File Wright
    file_name = 'C:\\Users\\Public\\Documents\\En_De_Data\\' + pin + '_output.txt'
    with open(file_name, 'w', encoding='utf8') as x_file:
        x_file.write('')
        for i in range(len(data)):
            x_file.write('{}'.format(data[i]))


def audio_play(key):
    link = 'C:\\Users\\Public\\Documents\\En_De_Data\\' + key + "_output.txt"
    fh = open(link, "r")
    myText = fh.read().replace("\n", " ")
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save('C:\\Users\\Public\\Documents\\En_De_Data\\' + key + "_output.mp3")
    fh.close()
    playsound('C:\\Users\\Public\\Documents\\En_De_Data\\' + key + '_output.mp3')


def mainMenu():  # Main Menu
    os.system('cls')
    print("What do you want to do?")
    print("1. Encryption?")
    print("2. Decryption?")
    print("3. Logout?")
    choise = int(input("Your Choice: "))
    operation(choise)


def forgetUName():
    link = 'reset'
    main(link)


def user_out():
    count = 0
    temp = 'uID.txt'
    with open(temp, 'r') as file:
        file_reader = csv.reader(file)
        for row in file:
            for i in range(len(row)):
                if row[i] == ',':
                    break
                else:
                    count += 1
    print("User Name: " + row[:count])
    print("Password : " + row[count + 1:])
    ex = input("Copy your info. Press Enter to Close!")


def use_ver(file):
    os.system('cls')
    user = input("Enter Recovery Key: ")
    for row in file:
        if row[0] == user:
            user_found = [row[0]]
            user_out()
            break
        else:
            os.system('cls')
            print("Wrong Key")


def main(link):
    if link == 'uID':
        temp = str(link) + '.txt'
        with open(temp, 'r') as file:
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()
    else:
        temp = str(link) + '.txt'
        with open(temp, 'r') as file:
            file_reader = csv.reader(file)
            use_ver(file_reader)
            file.close()


def user_find(file):
    user = input("Enter your username: ")
    for row in file:
        if row[0] == user:

            user_found = [row[0], row[1]]
            pass_check(user_found)
            break
        else:
            os.system('cls')
            print("User Not Found -_-")
            forget()


def pass_check(user_found):
    user = input("Enter your password: ")
    if user_found[1] == user:
        mainMenu()
    else:
        os.system('cls')
        print("Wrong Password")
        forget()


def forget():
    print("1. Try Again?")
    print("2. Recover User name and Password?")
    temp = int(input("Your Choice: "))
    if temp == 2:
        os.system('cls')
        forgetUName()
    else:
        os.system('cls')
        print("$$$Welcome to data En De Cryptor$$$")
        fst_login()


def recovery_Key():  # File Wright
    data = input("Recovery Key : ")
    file_name = 'reset.txt'
    with open(file_name, 'w', encoding='utf8') as x_file:
        x_file.write('')
        for i in range(len(data)):
            x_file.write('{}'.format(data[i]))


def newUser():  # File Wright
    print("###New User Registration###")
    u = input("New Username: ")
    p = input("New Password: ")
    data = u + ',' + p
    file_name = 'uID.txt'
    with open(file_name, 'w', encoding='utf8') as x_file:
        x_file.write('')
        for i in range(len(data)):
            x_file.write('{}'.format(data[i]))


def create_new_der():
    path = 'C:\\Users\\Public\\Documents\\En_De_Data'
    access_rights = 0o755
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print("%s" % path)
    else:
        print(" %s " % path)


def notification(data):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('En_De_Cryptor', data, duration=0)


def fst_login():
    uID = False
    with open('uID.txt') as my_file:
        my_file.seek(0, os.SEEK_END)  # go to end of file
        if my_file.tell():  # if current position is truish (i.e != 0)
            my_file.seek(0)  # rewind the file for later use
            uID = True
        else:
            uID = False

    if uID == True:
        link = 'uID'
        main(link)

    else:
        newUser()
        recovery_Key()
        create_new_der()
        notification("Registration Successfull!!!")
        os.system('cls')
        print("Registration Successfull!!!")
        fst_login()


print("$$$Welcome to data En De Cryptor$$$")
fst_login()