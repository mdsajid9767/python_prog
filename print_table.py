def print_table():
  check = 'y'
  while check == 'y':
    n = int(input("enter a no to print a table: "))
    for i in range(1, 11):
      if i == 10:
        print(n," *",i," = ",n*i)
        continue
      print(n," * ",i," = ",n*i)
    if(input("do you want to print more table: ") == 'y'):
      check = 'y'
    else:
      check = 'n'

# print_table()