alphabet1 = "abcdefgijklmnopgrstuvwxyzabcdefgijklmnopgrstuvwxyz"
alphabet2 = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
number = "12345678901234567890"
encrypt = input ("Enter a clear messang: ")
key = int(input("Please enter a key (number from 1-25): "))
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position1 = alphabet1.find(letter)
    newPosition1 = position1 + key
    position2 = alphabet2.find(letter)
    newPosition2 = position2 + key
    position3 = number.find(letter)
    newPosition3 = position3 + key
    if letter in alphabet1:
        encrypted = encrypted + alphabet1 [newPosition1]
    if letter in alphabet2:
        encrypted = encrypted + alphabet2[newPosition2]
    if letter in number:
        encrypted = encrypted + number[newPosition3]

print ("Your chiper is: ", encrypted)