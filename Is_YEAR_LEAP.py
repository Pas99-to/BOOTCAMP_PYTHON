'''
#Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, 
and this is the clue. We don't want any repetitions. We want them to be removed.

#Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

#Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that 
can carry out a conversation with the user and obtain all the data from her/him.

#Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.

#We've provided no test data, as that would be too easy. You can use our skeleton instead
'''

from operator import itemgetter


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
new_list = []

for iteration in my_list:
    if iteration not in new_list:
        new_list.append(iteration)

my_list = new_list[:]

print("The list with unique elements only:")
print(my_list)


# Other Exercise 



'''Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, 
or returns None if any of the arguments is invalid. 

Use the previously written and tested functions. Add your own test cases to the code.

Note: a year, occurring once every four years, that has 366 days including February 29 as an intercalary day.
'''

def is_year_leap(year):
    LEAP_YEAR_STEP1=4
    LEAP_YEAR_STEP2=100
    LEAP_YEAR_STEP3=400
    if year % 4 == 0:
         if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
         else:
            return True  
    else:
        return False  
    

def days_in_month(year, month):
    nudillos_month =[1,3,5,7,8,10,12]
    not_nudillos_month =[4,6,9,11]

    if is_year_leap(year) == True and month == 2:
        return 29
    elif is_year_leap(year) == False and month == 2:
        return 28
    elif month in nudillos_month:
        return 31
    elif month in not_nudillos_month:
        return 30
    else:
        print ("NO existe DIA o Mal digitado")

def day_of_year(year, month, day):
    i = 1
    suma = 0
    while True:
        if day <= 31 :
            if i != month:
                suma += days_in_month(year, i)
            else:
                if i == 2:
                    if day > days_in_month(year, i) :
                        print("Excede de los dias que tiene febrero")
                        break   
                suma = suma + day
                return suma
                break    
            i +=1 
        else:
            print("Los DIAS excenden de los DIAS que tiene el mes")
            break 
        
print(day_of_year(2000,12,31))


