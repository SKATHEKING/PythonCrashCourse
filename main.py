# The aim of this project is to serve as a python refresher so that the user may reread when revising python code

#set variable
name = 'Mateus Goncalves De Ouro'
#int variable
age = 24
#boolean variable
isMale = True

print(f'Hello my name is {name}, I am {age} years old and yes it is {isMale} I am a man.')

#tuples are an immutable data type
favShoeBrands = ('DC','Nike','Adidas', 'C1rca', 'Supra')

#lists

coolCarsList = ['Nissan skyline', 'Nissan GTR', ' Hellcat', 'Range rover']

#dictionaries

university_grades = {'mateus ' : '2:1', 'sol' : '2:1' , 'chris' : '1' }

def get_university_grades():
    for key,value in university_grades.items():
        print(f'the student {key} has achieved {value} in his academic record')
get_university_grades()

#defining a function and using it to print all coolCarsList
def allCoolCars():
    for car in coolCarsList:
        print(f'{car} is a super cool car!')

allCoolCars()

#list comprehension

temps = [221.0,223.0, 500.0, 600.0]
new_temps = [temps * 10 for temp in temps ]

print(new_temps)

#reading files
cv = open("cvintext.txt")
print(cv.read())
cv.close()