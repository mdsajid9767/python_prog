import prime_no
import print_table
import palindrome_no
import random_number_guess
import calculation_game

# print_table.print_table()
# prime_no.Prime()

# def print_table():
#   check = 'y'
#   while check == 'y':
#     n = int(input("enter a no to print a table: "))
#     for i in range(1, 11):
#       if i == 10:
#         print(n," *",i," = ",n*i)
#         continue
#       print(n," * ",i," = ",n*i)
#     if(input("do you want to print more table: ") == 'y'):
#       check = 'y'
#     else:
#       check = 'n'
#
# def Prime():
#     n = int(input("enter number to check prime: "))
#     if n > 1:
#         for j in range(2, int(n/2)+1):
#            if(n % j == 0):
#                 return n, "is not a prime no"
#                 # return ("not prime")
#                 break
#         else:
#             # return (n, "is a prime no")
#             return ("prime")
#     else:
#         # return (n, "is not a prime no")
#         return ("not prime")

#------------------problem in program

# def Prime():
#     return ("hello")
#
# def print_table():
#     return ("by")
#
# def menu(x):
#     switcher={
#         1: Prime(),
#         2: print_table()
#     }
#     # print(switcher.get(x, "invalid choice"))
#
#     return switcher.get(x, "invalid choice")
#
# choice=int(input("enter your choice \n1. Prime No\n2. Print Table\n0. Exit\n"))
# c=menu(choice)
# print(c)









def exit1():
    return 'n'

check = 'y'
while check == 'y':
    choice=int(input("\nenter your choice \n1. Prime No\n2. Print Table\n3. Palindrome No\n4. Random No Guess\n5. Calculation Game\n0. Exit\n"))
    if choice == 1:
        prime_no.Prime()
    elif choice == 2:
        print_table.print_table()
    elif choice == 3:
        palindrome_no.palindrome_no()
    elif choice == 4:
        random_number_guess.randome_no_guess()
    elif choice == 5:
        calculation_game.cal_game()
    elif choice == 0:
        print("Program terminated")
        check=exit1()

