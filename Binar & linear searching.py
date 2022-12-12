#Write 2 functions:
#Function for linear search in the list: the input is a number that is sequentially compared with each element of the array by 
# order. At the output, we get the index of a given number, if it is in the list.
#Function for binary search in the list: the list needs to be sorted, and then we compare the number not with each element of the 
#list, but each time only with the middle element. Then we narrow the search range. We continue until we find the right element.

def line_search(s_num, massive):
    """Linear search"""
    massive = list(massive)
    x = False
    while x != True:
        for y in massive:
            if y == s_num:
                x = True
                num_index = massive.index(s_num)
                print ("Your number is found in the list. Index: " + str(num_index))
        if x == False:
            x = True
            print ("Your number was not found in the list.")

def binar_search(s_num,massive):
    """Binary search"""
    massive = sorted(list(massive))
    low = 0
    hight = len(massive) - 1
    x = False
    while low <= hight and not x:
        mid = (low+hight)//2
        mid_num = massive[mid]
        if mid_num == s_num:
            x = True
            num_index = massive.index(s_num)
            print ("Your number is found in the list. Index: " + str(num_index))
        if mid_num > s_num:
            hight = mid - 1
        else:
            low = mid + 1
    if x == False:
        x = True
        print ("Your number was not found in the list.")
        
s1 = 10 #desired number
s2 = 7,6,5,4,37,8,9,6 #array
line_search(s1,s2)
binar_search(s1, s2)

#By binary search, the program output the result in 4 steps, linear search - in 9.