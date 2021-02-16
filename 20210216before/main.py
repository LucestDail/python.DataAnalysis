def mask_security_number(security_number):
    digit = str(security_number);
    secure = []
    for i in range(len(digit)):
        secure.append(digit[i])
    secure[-4:] = '****'
    return ''.join(secure)

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))