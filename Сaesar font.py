alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = int(input("Enter encryption step: "))
message = input("Message for encryption: ").upper()
demessage = input("Message for decryption: ").upper()
en_message = "" #a variable for an encrypted message
for i in message:
    """Encrypton"""
    place = alphabet.find(i)
    new_place = place + x
    if i in alphabet:
        en_message += alphabet[new_place]
    else:
        en_message += i
print (en_message)
en_message = "" #a variable for an decrypted message
for i in demessage:
    """Decryption"""
    place = alphabet.find(i)
    new_place = place - x
    if i in alphabet:
        en_message += alphabet[new_place]
    else:
        en_message += i
print (en_message)