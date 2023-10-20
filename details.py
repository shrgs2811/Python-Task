import re


# Password checking
def check_pas(p):
    flg = 0
    if len(p) < 8:
        print("The length of password is less than 8")
        flg = 1
    elif not re.search("[a-z]", p):
        print("There should be at least 1 small character")
        flg = 1
    elif not re.search("[A-Z]", p):
        print("At least 1 upper character")
        flg = 1
    elif not re.search("[0-9]", p):
        print("At least 1 digit from 0-9")
        flg = 1
    elif not re.search("[@#$*]", p):
        print("Required 1 or more special character")
        flg = 1
    return flg


# Getting details from user
def insrt_dtls():
    name = input("Enter your name:")
    mail = input("Enter your mail id:")
    while 1:
        passw = input("Enter password")
        flag = check_pas(passw)
        if flag == 0:
            return name, mail, passw
        else:
            print("Invalid password")


# Writing details into file
def wrt_dtls(d):
    try:
        f = open(d[0] + ".txt", "x")
        dt = "Name:"+d[0]+"\n"+"Mail:"+d[1]+"\n"+"Password:"+d[2]
        f.write(dt)
        f.close()
    except:
        print("\nOops!File already existing")


# Read from a file
def rd_dtls(nam):
    try:
        f = open(nam+".txt", "r")
        print(f.read())
    except:
        print("There is no such file")


print("1 - For entering details\n2 - For searching details\n3 - Exit")
while 1:
    val = input("Enter an option:")
    if int(val) == 1:
        x = insrt_dtls()
        wrt_dtls(x)
    elif int(val) == 2:
        sname = input("Enter name")
        rd_dtls(sname)
    elif int(val) == 3:
        exit()
