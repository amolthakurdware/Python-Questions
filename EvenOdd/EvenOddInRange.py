# video: https://youtu.be/LlF4ejAZ92g
even_count=0
odd_count=0
for number in range(0,6):
    if number%2==0:
        print(number," is even")
        even_count=even_count+1
    else:
        print(number, " is odd")
        odd_count=odd_count+1

print("Count of even numbers",even_count)
print("Count of odd numbers",odd_count)
