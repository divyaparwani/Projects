a=int(input("Enter a no:"))
if a%5==0:
    if a%11==0:
        print(a,"is divisible by both 5 and 11")
elif a%11==0:
    print(a,"is divisible by 11")
elif a%5==0:
    print(a,"is divisible by 5")
else:
    print(a,"is not divisible by 5 or 11")

