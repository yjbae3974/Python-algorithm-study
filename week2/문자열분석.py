def count_characters(line):
    lower_case_count = 0
    upper_case_count = 0
    digit_count = 0
    space_count = 0

    for char in line:
        if char.islower():
            lower_case_count += 1
        elif char.isupper():
            upper_case_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    return lower_case_count, upper_case_count, digit_count, space_count

results = []

while True:
    try:
        line = input()
        counts = count_characters(line)
        results.append(counts)
    except EOFError:
        break

for result in results:
    print(' '.join(map(str, result)))
