#Solve Greatest Common Divisior Problem with Euclis Algortihm 
def euclid(numberOne,numberTwo):
    if numberTwo==0:
        return numberOne
    else: return euclid(numberTwo,numberOne%numberTwo)

if __name__=="__main__":
    print(f"""Greates Common Divisior :{euclid(int(input("Please, enter a number : ")),int(input("Please, enter another number : ")))}""")