#Video link: https://youtu.be/rAP8rknKnJY

def find_factorial(number):
    factorial=1
    if(number<0):
        print("Factorial of a negative number can not be calcualted")
        return
    for i in range(1,number+1):
        factorial=factorial*i
    return factorial


number=int(input("Enter a number:"))
factorial=find_factorial(number)
print("Factorial of ",number," is ",factorial)
