#We take a list of numbers and output the sum of the neighbors of this number in the list.

start_list = [1,2,3,4,5]
new_list = []
left_index = -1
right_index = -len(start_list) +1
middle_index = 0
while middle_index < len(start_list):
    new_list.append(start_list[left_index] + start_list[right_index])
    middle_index += 1 
    left_index +=1
    right_index +=1
print (new_list)