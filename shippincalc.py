def main():
    items = float(input("Enter the number of items purchased : "))
    shipcharge = 10.95 + 2.95*(items-1)
    print("The charge of the shipping is " + str(shipcharge))
main()