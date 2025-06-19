celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

word = input("Enter a word: ").strip().lower()

if word and word[0] in "aeiou":
    print(f"'{word}' starts with a vowel.")
else:
    print(f"'{word}' does not start with a vowel.")