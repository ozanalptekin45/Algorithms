def isPrimeNumber(number):
    for i in range(2,int(number**(0.5))+2):
        if number%i==0:return False
    return True

if __name__=="__main__":
    print("Number is prime") if isPrimeNumber(int(input("Please, enter a number : "))) else print("Number is not prime")

