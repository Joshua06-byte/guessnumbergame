from random import randint
n = (randint(1,100))
print(n)

while True: 
    number = (int(input("please try and guess a number between 1 and 100: ")))
    if (number == n) :
        print ("you have guessed it")
        break
    elif (number > n):
        print ("the number of your choosing is more then the number itself")
    elif (number < n):
        print ("the number of your choosing is less then the number itself")