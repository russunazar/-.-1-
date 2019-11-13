string = input("Enter a string: ")
word = string[::-1]
print(*reversed(word.split(5)))