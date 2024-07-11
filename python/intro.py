#name = input("What is your name? ")
#age = input("How old are you? ")
#month = input("What month were you born in? ")

#int (age)

#print("Hi", name, "nice to meet you! You are", age, "years old. Born in", month)

#grade = float(input("Input your grade: "))

#if grade < 49:
    #print("F")

#elif grade >= 50 and grade <= 59:
    #print("D")

#elif grade >= 60 and grade <= 70:
    #print("C")

#elif grade >= 70 and grade <= 84:
    #print("B")

#elif grade >= 85 and grade <= 100:
    #print("A")

#else: 
    #print("You failed")



#phonebook = {
    #"John" : 938477566,
    #"Jack" : 938377264,
    #"Jill" : 947662781
#}

#phonebook["Bob"] = 6749876453
#print(phonebook)



#skibidi = [1, 2, 3, 4, 5, 6, 7, 8]
#idibiks = []

#for i in skibidi:
    #idibiks.insert(0, i)

#print(idibiks)

#a = [1, 1, 1]
#b = [0,0, 0]
#c = [0,"c", 1]


#if a[0] == a[1] == a[2] == 1:
    #print("1 won")
#elif a[0] == a[1] == a[2] == 0:
    #print("0 won")
#else:
    #print("there is no winner")


#if b[0] == b[1] == b[2] == 1:
    #print("1 won")
#elif b[0] == b[1] == b[2] == 0:
    #print("0 won")
#else:
    #print("there is no winner")


#if c[0] == c[1] == c[2] == 1:
    #print("1 won")
#elif c[0] == c[1] == c[2] == 0:
    #print("0 won")
#else:
    #print("there is no winner")



#num = int(input("Input a number:"))

#factorial = 1

#for i in range(1, num + 1):
    #factorial = factorial*i

#print(num, "factorial is", factorial)


#import random

#num = random.randint(0,100)
#guess = int(input("Guess the number (0-100): "))


#while num != guess:
    #if guess > num:
        #guess = (int(input("Your number is greater than the random number. Choose another number: ")))
    #else:
        #guess = (int(input("Your number is less than the random number. Choose another number: ")))
        
        
#print("You guessed the number! The number was", guess)



#def roastmarshmallow():
    #print("Start a bonfire")
    #print("Put marshmallow on stick")
    #print("Roast marshmallow on top of fire until golden")
    #print("Take marshmallow off the stick and eat it!")


#for i in range(0,6):
    #roastmarshmallow()


#def spicyPrint():
    #x = ["red", "orange", "yellow", "green", "blue", "purple"]
    #print(x)

#for i in range(0,6):
    #print(spicyPrint())
    #print("\n")


'''def spicyPrint(InputList):
    for i in InputList:
        print(i,end='')

hat = [1, 2, 3, 4, "red"]
spicyPrint(hat)'''



'''def countCharacters():
    x = input("input a string:")
    print((len(x)))

countCharacters()'''



#def convertSentenceUpper(sentence):



'''prices = [10, 20, 30, 40, 50]


for i in prices:
    print(i*0.8)'''



'''class Person:
    def __init__(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender 

p1 = Person("John", 30, "male")
p2 = Person("Mary", 25, "female")
p3 = Person("Sarah", 40, "female")

print(p1.name, p1.age, p1.gender)

print(p2.name, p2.age, p2.gender)

print(p3.name, p3.age, p3.gender)'''



'''class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

m1 = Movie("The Lion King", "Roger Allers and Rob Minkoff", 1994)
m2 = Movie("Frozen", "Chris Buck and Jennifer Lee", 2013)
m3 = Movie("Up", "Pete Docter and Bob Peterson", 2009)

print(m1.title, m1.director, m1.year)

print(m2.title, m2.director, m2.year)

print(m3.title, m3.director, m3.year)'''



'''class Student:
    def __init__(self, name, ID_number, age, mark, favorite_class):
        self.name = name
        self.ID_number = ID_number
        self.age = age
        self.mark = mark
        self.favorite_class = favorite_class

s1 = Student("John", 1, 15, "B+", "science")'''



'''file = open("new_file.txt", "w")

file.write("This is the firt line of text. \n")
file.write("This is the second line of text \n")

file.close()'''



filepath= 'yapnotes.txt'
with open(filepath, 'r') as fileReader:
    content=fileReader.read()
    print(content)
    