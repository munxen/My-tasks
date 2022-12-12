#We accept the start time of the first lesson, the duration of the lesson, the duration of the changes as input, 
# output - call schedule for N lessons:

import time

s_lesson_format =[] #creating a list for data conversion
b = 0
while b == 0:
    s_lesson = s_lesson_format.append((input("The beginning of the first lesson (hour:min/hh:mm): ")))
    for i in s_lesson_format: #Intercepting the error if format not hh\mm
        if len(i) !=5:
            s_lesson_format.clear()
            print ("Please enter the data in the HH:MM format")
        else:
            b +=1
            for z in s_lesson_format: #We format the received data in seconds to work with them
                x = int ((z[:2]))*60*60
                y = int ((z[3:]))*60
                start_lesson = x + y #the start time of the first lesson

time_lessons = int (input("Duration of the lesson, min:"))*60
min_free_time = int (input("Duration of free time, min:"))*60
num_lessons = int (input ("How many lessons do I need a schedule for:"))

"""We convert all the time received and get the end of the first lesson"""
sec_end_first_lesson = start_lesson + time_lessons
end_first_lesson = time.strftime("%H:%M", time.gmtime(int(sec_end_first_lesson)))

"""If the number of lessons is not more than one"""
if num_lessons == 1:
    print (str(num_lessons) + " lesson: " + " ".join(s_lesson_format) + " - " + end_first_lesson )
"""If the number of lessons is more than one"""
if num_lessons >1:
    """A cycle with a formula for determining the time"""
    k = 1 #lever for comparison with the number of lessons
    print (str(k) + " lesson: " + " ".join(s_lesson_format) + " - " + end_first_lesson )
    while k != num_lessons: #it starts with 2 lessons
        k += 1
        sec_end_first_lesson += min_free_time
        rst1 = time.strftime("%H:%M", time.gmtime(int(sec_end_first_lesson)))
        sec_end_first_lesson += time_lessons
        rst2 = time.strftime("%H:%M", time.gmtime(int(sec_end_first_lesson)))
        print (str(k) + " lesson: " + rst1 + " - " + rst2)