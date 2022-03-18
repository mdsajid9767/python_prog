def Prime():
    n = int(input("enter number to check prime: "))
    if n > 1:
        for j in range(2, int(n/2)+1):
           if(n % j == 0):
                print(n, "is not a prime no")
                break
        else:
            print(n, "is a prime no")
    else:
        print(n, "is not a prime no")

#Prime()
