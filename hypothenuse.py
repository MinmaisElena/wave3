import math

def main():
    first = int(input("Please enter the first side of the triangle: "))
    second = int(input("Please enter the second side of the triangle: "))
    hyp = math.sqrt(first**2 + second**2)
    print("The length of hypothenuse is "+ str(hyp)+".")

main()