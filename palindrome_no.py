def palindrome_no():
    x=int(input("enter no to check palindrome: "))
    x1=x
    r=0
    while(x>0):
        n=x%10
        r=(r*10)+n
        x=(x//10)
    if (x1 == r):
        print(x1,"is a palindrome no")
    else:
        print(x1,"is not a palindrome no")

# palindrome_no()