from math import floor

def extract_digits(n):
    # Increase value to 4 digits
    value = n
    exponent = 0
    while value < 999.5 and exponent < 3:
        value *= 10
        exponent += 1

    value = floor(value + 0.5) / (10**exponent)

    str_value = str(value)
    dp_pos = str_value.find('.') - 1
    digits = [int(x) for x in list(str_value.replace('.', ''))[:4]]
    return { 'dp_pos': dp_pos, 'digits': digits }
