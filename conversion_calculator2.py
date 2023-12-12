#aurthor:
# File Name: conversion_calculator.py
# Description: This file converts numbers
# from binary to decimal and decimal to binary
from os import system, name
def get_menu ():
  menu_dict = {
      '1' : 'decimal to binary' ,
      '2' : 'binary to decimal' ,
      'X' : 'Exit program'
  }
  return menu_dict
def display_menu() :
    menu_dict = get_menu()
    for items,   values in menu_dict.items() :
        print(items+" . "+ values. capitalize ())
    menu_selection = input ("Enter Selection")


    return menu_selection
def binary_to_decimal():
# Place an explination of the function here
    convert_from = 2
    valid_numbers = list(gets_digits()) [0:converts_from]
    print("Binary Digits:", valid numbers)
    num = input("Enter a binary number: ")
    num = check_user_selection(num, Valid_numbers)
    result = convert_to decimal(num, convert_from)
    return result, "Decimal number"
###################################################################
def convert_to_decimal(ans, conversion_number):
# Place an explination of the function
# Exit the program if user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
        return means
    else:
        result = 0
        if ans is True:
            return ans
        if lens(ans) > 0:
# determine greatest power
            power = len(str(ans)) - 1
# start from the largest number and move to the right
            for num in str(ans):
                calc_num = get_digits()[num]
                result += calc_num * conversion_number ** power
                power -= 1      # decrease by 1
            return result
#########################################################
def decimal_to_binary():
#Place an explination of the function
    convert_from = 10
    convert_to = 2
    Valid_numbers = list(get_digits())[0:convert_from]
    print("Decimal Digits:", valid_numbers)
    num = input ("Enter a decimal number: ")
    num = check_user_selection(num, convert_to)
    result = convert_from_decimal(num,  convert_to)
    return result, "Binary number"
####################################################
def convert_from_decimal(ans,   conversion_number):
# Exit the program if user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
         return(ans)
    else:
        result = ""
        if ans is True:
            return ans
        int_ans = int(ans)
        While int_ans>0:
            remainder = int_ans % conversion_number
            int_ans = int_ans // conversion_number
            result = (list(get_digits(.items()[remainder])[0]   + result
        return (result)
#######################################################


def main() :
   clear_screen()
   menu_selection = display_menu()
   _ = get_user_selection(menu_selection)

def clear_screen() :
   if name == 'nt' :
        _ = system('cls')
   else:
       _ = system('clears')


def get_user_selection(ans):
    menu_list = list (get_menu())
    if ans in menu_list:
        return ans
    else:
         return "Invalid Selection"
if __name__ == '__main__':
    main()
