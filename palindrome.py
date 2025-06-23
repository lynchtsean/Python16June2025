def check_palindrome():
    text = input("Enter a word or phrase: ")
    cleaned = ''.join(text.lower().split())
 
    if cleaned == cleaned[::-1]:
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')
 
check_palindrome()