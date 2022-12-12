#There is a list of lists with the names of children of several school classes, you need to make a dictionary in which 
# the “key” will be the name of the child, and the value is the number of children with that name in all classes of the school.

school_list =['Tanya','Vanya','Anya','Ira','Zhenya','Artem','Tanya','Masha','Anya','Vitya','Anton','Galya','Vova','Anya','Ira']
school_list_names = { }
x = False
start_name = 0 #index of the initial name
copy = 0 #number of copies of names found
while x == False:
    for names in school_list: #we do a search to compare each name with other names in the list
        while x == False:
            first_name = school_list[start_name] #first name (selected by variable)
            second_name = names #second name (selected by brute force)
            if first_name == second_name:
                "Match found"
                start_name += 1
                copy += 1
            if first_name != second_name:
                "Match are not found"
                start_name += 1
            if start_name == len(school_list):
                "Reset parameters. Go to compare the next name"
                school_list_names[names] = copy
                start_name = 0
                copy = 0
                break
    x = True #completion of the loop when the iteration is over
print (school_list_names)