#Solve Greatest Common Divisior Problem with Euclis Algortihm 
def euclid(numberOne,numberTwo):
    if numberTwo==0:
        return numberOne
    else: return euclid(numberTwo,numberOne%numberTwo)

numberOne=int(input("Please, enter a number : "))
numberTwo=int(input("Please, enter another number : "))
print(f"Greates Common Divisior :{euclid(numberOne,numberTwo)}")