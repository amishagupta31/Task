def check_password(password):
    if len(password) < 8:
        return "Weak"

    upper = lower = digit = special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch in "!@#$%^&*":
            special = True

    score = upper + lower + digit + special

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

print(check_password("Abc@1234"))
