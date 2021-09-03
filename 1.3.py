num_init = int(input('enter a number -'))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num = num // 10
    print(num)
print(f"Max digit in number {num_init} is {maximum}")