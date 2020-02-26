userString = (input('Please enter a stringof characters '))

isPalindrome = True
i = 0

while i < len(userString) // 2:
    if userString[-i-1] != userString[i]:
        isPalindrome = False
        break
    else: i = i + 1 

print('Is the number a palindrome? ', isPalindrome )              


