while True:
    num = int(input("Enter a number: "))

    # Check if the number is prime
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("The number is not prime. Please try again.")
                
                break
        else:
            print("The number is prime.")
            break
    else:
        print("The number is not prime. Please try again.")
