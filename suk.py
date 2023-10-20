import re


# Password checking
def check_pas(a):
    flg=0
    if len(a)<8:
        print("The length of password is less than 8")
        flg=1
    elif not re.search("[a-z]",a):
        print("There should be atleast 1 small characters")
        flg=1
    elif not re.search("[A-Z]", a):
        print("Atleast 1 upper charcter")
        flg=1
    elif not re.search("[0-9]", a):
        print("Atleast 1 digit from 0-9")
        flg=1
    elif not re.search("[@#$*]", a):
        print("Required 1 or more special character")
        flg=1
    else :
         print("Valid password")
    return flg


# Getting details from user
def insrt_dtls():
    name = input("Enter your name:")
    mail = input("Enter your mail id:")
    passw = input("Enter password")
    flag = check_pas(passw)
    if flag == 0:
        print(name, mail, passw)
    else:
        print("Invalid password")


print("Enter details")
insrt_dtls()
