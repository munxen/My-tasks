#Write a program that will predict the number of people who have turned into zombies after a certain time 
# the number of days after the start of an unknown epidemic. We accept the number of people who have already 
# turned into zombies by the beginning of the calculation, the number of people that each of them can infect, as well 
# the day on which the calculation is performed

"""We accept the data"""
zombies = int (input("How many zombies were there at the beginning of the calculation: "))
do_zombies = int (input("How much can everyone infect: "))
days = int (input("On which day we make a miscalculation :"))

k = 1
"""Conclusion"""
if days == 1:
    print ("1 day: " + str(zombies))
if days >1:
    print ("1 day: " + str(zombies))
    while k != days:
        k += 1
        d = zombies*do_zombies+zombies
        print (str(k) + " days: " + str(d) )
        zombies = d
        
