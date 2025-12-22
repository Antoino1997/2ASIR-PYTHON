def spongecase(text):
    result = ""
    use_upper = False

    for char in text:
        if char.isalpha():
            if use_upper:
                result += char.upper()
            else:
                result += char.lower()

            use_upper = not use_upper
        else:
            result += char

    return result

print("Enter a sentence:")
user_input = input()
print(spongecase(user_input))