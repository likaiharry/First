# Fileneme: test001.py

import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = text.lower()
    print(text)
    text = text.replace(' ', '')
    print(text)
    for char in string.punctuation:
        text = text.replace(char, '')
    print(text)
    return text == reverse(text)

def main():
    something = input('Enter text:')
    if (is_palindrome(something)):
        print("Yes, it is")
    else:
        print("No, it is not")

if __name__ == '__main__':
    main()
else:
    print("it was improted!")
