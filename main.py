number = int(input("Enter a number: "))
binary = bin(number)[2:]
print("Binary is:", binary)

n = int(input("Which bit number do you want to see? (1 = first form left): "))
if 1 <= n <= len(binary):
    bit = binary[n - 1]
    print("That bit is:", bit)
else:
    print("Oops! Bit number too big.")