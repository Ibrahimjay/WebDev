# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break


rows = 5
# outer loop

    # inner loop
# for i in range(6):
#         for j in range(6-i):
#             print("*", end='')
#         print('')

# – the number must be divisible by five.
# – if the number is greater than 150, then skip it and move to the next number.
# – if the number is greater than 500, then stop the loop.
# given
# numbers = [12,75,150,180,145,525,50]
# Expected output: 75 150 145

numbers = [12,75,150,180,145,525,50]
i=0
while i<len(numbers):
    number = numbers[i]
    if number % 5 == 0:
        if number > 150:
            continue
        if number > 500:
            break
        print(number)
    i+=1

