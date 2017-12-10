def odd_or_even(num):
    """Function to check and print if the num is odd or even"""
    if(num%2==0):
        print("The number is even.")
    else:
        print("The number is odd.")


num=int(input("Enter the number: "))
odd_or_even(num)