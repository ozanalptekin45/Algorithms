def isPrimeNumber(lastNumber):
    for number in range (2,lastNumber+1):
        for i in range(2,int(number**(0.5))+2):
            if number%i==0:break
        else:print (f"{number} is prime number")

if __name__=="__main__":
    lastNumber=int(input("Please, enter a number : "))
    isPrimeNumber(lastNumber)