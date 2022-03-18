import random

def randome_no_guess():
  n = random.randint(1, 101)
  check = 1
  attempt = 0
  while check>0:
    n1 = int(input("Enter your guess: "))
    if n == n1:
      print("Yes, the number is ",n)
      check = 0
    elif n1 > n:
      print("Your guess is too high")
    else:
      print("Your guess is too low")
    attempt += 1
  print("Total attempt is: ", attempt)

# randome_no_guess()