binary = input()

while len(binary) % 3 != 0:
    binary = '0' + binary
    #11 => 011. 8진수는 2진수 3개를 한번에 본다.
octal = ''
for i in range(0, len(binary), 3):
    three_bits = binary[i:i+3]
    octal_digit = int(three_bits, 2)
    octal += str(octal_digit)

print(octal)
