def main():
    num = int(input("Enter a number: "))  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:
                print(False)  
                break 
            elif (num % i) > 1:
                print(True)
                break
    elif num == 1:  
        print(False)
    else:
        print("Please enter vaild number")

main()