def sum_digit(num):
    total = 0
    str_num = str(num)
    for digit in str_num:
        total += int(digit)
    return total

digit_total = 0
for i in range(1,1001):
    digit_total += sum_digit(i)

print(digit_total)