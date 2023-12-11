# name of file: conversion underscore.py\
# title: conversion calcultator
# description: THE file puts the numbers into binary after the user
# prompts them in for a number and binary into decimal or from a decimal to binary


def user_selection () :
    print("1 binary to decimal")
     ans = input("Enter selection: ")
     if ans == "o" :
         return False
     return True

def main() :
    run_me = True
    while run_me:
          run_me =  user_selection()

if __name__ ==  "__main__":
        main()


def max (num1,  num2) :
 if num1 >= num2 :
       print ("1:",num1)
       return  num1
 print ("2:",num2)
 return num2
