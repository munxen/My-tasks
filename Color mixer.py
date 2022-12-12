#Develop a program that prompts the user to enter the names of the two primary colors to mix. 
# If the user enters anything other than the names “red”, “blue” or “yellow”, the program
# should display a message about error. Otherwise, the program should output the name of 
# the color that will result.
def color_search():
    """Goes through the colors"""
    if 'blue' in COLORS and 'red' in COLORS:
        print("It turned out to be purple!")
    elif 'red' in COLORS and 'yellow' in COLORS:
        print ("It turned out to be orange!")
    elif 'blue' in COLORS and 'yellow' in COLORS:
        print ("It turned out to be green!")
    else:
        print ("Errow. Please select the suggested colors.")
COLORS =[]
print ("Enter two colors to mix.")
print ("Available colors: red, blue, yellow.")
color1 =COLORS.append(input ("The first color:\n"))
color2 =COLORS.append(input ("The second color:\n"))
color_search()
