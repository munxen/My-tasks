import random

alphabet = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'
pass_lenght = int(input("Enter the length of the generated password: ")) #password length
cycle = pass_lenght #lever for the cycle
password_list = [] #list of characters

"""Generation"""
while cycle!=0:
    letter = alphabet[random.randint(0,51)] #generating a random letter
    password_list.append(letter)
    num = random.randint(0,9) #generating a random num
    password_list.append(num)
    cycle-=1

"""Pasword creating"""
random.shuffle(password_list) #shuffle the password list
password = password_list[:pass_lenght]

"""Showpass"""
print (''.join(map(str,password)))