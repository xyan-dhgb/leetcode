number = int(input())

numberToBits = bin(number)[2:]

bitsToString = str(numberToBits)

sumOfBit1 = 0

for bits in bitsToString:
    if bits == '1':
        sumOfBit1 += 1

print(sumOfBit1)