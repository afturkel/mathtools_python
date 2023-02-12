from basic_operations import *
from before_operation_process import *
import os

clear = lambda: os.system('cls')
sys_working = True

userwant = input("Hello, what do you want to do?\n1) Basic Math Operations\nFor example, write '1' for Basic Maths\n")

#while sys_working:
if userwant == "1":
    userwan_op = input("\nWhich kind of operation?\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division(not available for now)\n\n")
    if userwan_op == "1":
        print("Write your operation (ex: 15+20+25)")
        addition(input())
    elif userwan_op == "2":
        print("Write your operation (ex: 15-20-25)")
        subtraction(input())
    elif userwan_op == "3":
        print("Write your operation (ex: 15*20*25)")
        multiplication(input())
    else:
        clear()
        print("Please select correctly.")