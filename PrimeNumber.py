# Video : https://www.youtube.com/watch?v=gV4-OA6iltU

def is_prime(number):
    is_prime=True
    for devisor in range(2,number):
        remainder=number%devisor
        if remainder==0:
            is_prime=False
            break            
    return is_prime

for number in range(2,11):
    if is_prime(number):
        print(number)
