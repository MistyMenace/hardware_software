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
    return results, "Decimal number"

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
