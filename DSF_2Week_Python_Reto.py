#!/usr/bin/env python
# coding: utf-8

# # <div align="center"> DSF 2. Week: Python Basics

# In this exercise, you will learn some of the basics of Python.
# 
# If you are already familiar with Python you can skim through the instruction and only focus on the small exercises at each section, and then go to the challenges at the end of the document.
# 
# **Remember**, you have to run the cell (`Ctrl + Enter`) to see its output.

# ## Contents:
# 1. **Hello world!**
# 1. **Variables**
# 1. **Operations**
# 1. **Containers**
# 1. **Conditionals**
# 1. **Loops**
# 1. **Functions**
# 1. **Challenges**

# ## 1. Hello World!
# Let's start by printing text! We can print almost anything. Below are examples with text and numbers.

# In[1]:


print("Hello World!")
print(5)
print(5.1)
print(True)
print(25 * 2)


# Commas in the print function will insert spaces between the entries. This will be particularly useful when we want to print a variable with unknown value, or print many things of different data types.

# In[2]:


print("Give", "me", "some", "space.")

print("The current year is", 2021)

x = 5
print("Jake is", x, "years old.")


# ```\n``` gives a newline, and ```\t``` gives a tab.

# In[3]:


print("This is the first line.\nThis is the second line, with a \t tab.")


# **Exercise: Using only one print function, print your name, age and favorite ZHAW course on three different lines.**

# In[8]:


print("Reto Nüesch Erismann\nAlter: 43 Jahre\nFavorite ZHAW course: DSF :-)")
# Comments can be added with a hashtag!


# ## 2. Variables
# ### Declare and initialize?
# C++ is **statically typed** while Python is **dynamically typed**. This means that in C++, variable types are defined during compilation, while in Python they are defined during run-time.
# 
# Because of this, in C++ you need to both *declare* a variable and its type, and then *initialize* it. In Python, you only need to initialize it. While types exist in Python, they are not written out when defining a variable.

# In[9]:


# defining an integer variable
x = 10
# defining a double variable
y = 3.14
# defining a string
word = "Epoch of Reionisation"

# printing the variables
print(x)
print(y)
print(word)


# In the above example it's easy to see that x is an integer, y is a double, and word is a string. But if you are unsure you can always check the type of a variable using ```type(someVariable)```.

# In[10]:


print( type(x) )
print( type(y) )
print( type(word) )


# ### Changing type dynamically
# A blessing and a curse of Python is that you can change the type of a variable on the fly. Be careful that you don't accidentally change the type of variables unless desired!

# In[11]:


# define an integer
z = 7
# redefine it as a string
z = "Hello"

print(z)


# ### Type conversion
# If you have the number 64 stored as a string, but want to use it in computation, you can **cast** the string to an integer. To cast a variable to a different type, simply "wrap" it inside the type name. You can cast variables that "make sense" to cast. For example, you can cast 13 to a string "13" but you can't cast "hello world!" to a double (what would that even mean?).

# In[12]:


x = "64"
# Need to cast x to an integer otherwise you get an error because you can't add an 'int' with a 'string'
print( 1 + int(x) )


# Here is a list of common casts:
# * Integer: ```int()```
# * Double/Float: ```float()```
# * String: ```str()```
# 
# **Exercise: Create a variable holding a decimal number and cast it to an integer. What happens with the value?**

# In[22]:


x = 9.999
x = int(x)
x = float(x) # Information got lost!
print(x)


# ## 3. Operations
# ### Numerical
# Operations of numbers work similar to C++.

# In[23]:


# addition
print(5 + 5)

# subtraction
print(10 - 20)

# multiplication
print(3 * 3)

# division
print(100 / 2)

# integer division
print(7 // 2)

# remainder
print(7 % 2)

# power
print(2**10)


# ### Strings
# We can use ```+``` for strings to concatenate them.

# In[24]:


fake_language = "Återvänd" + " till" + " apa."
print(fake_language)


# ### Operations with variables
# If a variable is an integer or float, then we can do operations like normal with them.

# In[25]:


x = 5
y = x + 3
z = y - x
print("z =", z)


# We can also use increment, decrement, and similar operators to update the value of a variable.

# In[29]:


x = 100

# same as x = x + 1
x += 1
print(x)

# same as x = x -1
x -= 1
print(x)

# same as x = x * 5
x *= 5
print(x)

# same as x = x / 10
x /= 10
print(x)

# same as x // 3
x //= 3
print(x)

# same as x = x % 6
x %= 6
print(x)

# same as x = x**5
x **= 5
print(x)


# A very common use of this is to increment a variable by one: ```x += 1```

# ## 4. Containers
# Variables like integers, floats and strings are good when we only have one value to keep track of. If we have multiple values we can use a container like:
# 
# 1. List
# 1. Dictionary
# 
# There are many more containers but today we will focus on these two.
# 
# ### Lists
# Lists are similar to arrays in C++, except that can change in size. Common operations on a list include:
# 
# 1. **Access single element** ```my_list[0]``` will retrieve the first element in the list.
# 1. **Append to the list** ```my_list.append("ZHAW")```
# 1. **Delete items at between index a and b** ```del my_list[a:b]``` if you leave a empty, start from beginning to b, and vice versa.
# 1. **Remove a certain element** ```my_list.remove("rabbit")``` will remove "rabbit" if it exists in the list.
# 1. **Sum over all values** ```sum(someList)```
# 1. **Maximum/minimum value in the list** ```max(myList)``` or ```min(myList)```
# 
# A list is created using ```[]```.

# In[34]:


# create a list with some integers
years = [1997, 2000, 2002]

# elements don't have to share datatype!
some_list = [1, "hello", 2.7]

# you can print lists
print("Years:",years)

# print second element of a list and last element
print("Second element of years", years[1])
print("Last element of years", years[-1])

# change the 1st element of a list
years[0] = 1776
print (years)        #added

# append to the list
years.append(2025)
print (years)        #added

# sum over all values
sum_of_years = sum(years)
print (sum_of_years)  #added

# minimum year
minimum = min(years)
print (minimum)        #added

# remove an element
years.remove(2000)
print (years)        #added

# delete first element
del years[0]
print (years)        #added

# you can also create an empty list and then append stuff to it
empty_list = []


# ### Exercise: Create a list with your name (string), age (integer), height in meters (double), and favorite animal (string). After this, change the animal element to "Penguin".

# In[38]:


mylist = ["reto", 43, 1.8, "Tiger"]
mylist[3] = "Penguin"
print(mylist)


# ### Dictionaries
# The basic idea is that the **value** of the elements in the container is tied to a **key**. To access a value in a dictionary, we use the key, not the position like in a list. This is very useful when we want to access a certain value given some other value, like a list of students and their grades. 
# 
# A dictionary is created using ```{}```.
# 
# The keys and values can be any datatype, and they don't need to be the same datatype.

# In[39]:


# A dictionary initiliazed with keys and values: Keys are names, values are grades
grades = {"Axel": 4.0, "Albert": 5.5, "Michael": 6.0}
print(grades)

# access the value via the key
print("Grade of Axel", grades["Axel"])

# I can change the value as well
grades["Axel"] = 6.0
print(grades)

# I can also add a completely new person to the dictionary
grades["Kenyan Drake"] = 5.0
print(grades)

# Create an empty dictionary
empty_dictionary = {}


# **Exercise: Create a dictionary with keys "year", "month" and "day" and initialize values to today's date. Then, increment the day by 1.**

# In[49]:


mydict = {"Year": 2021, "Month": "Oktober", "Day": 1}

print("Datum: ",mydict["Day"],". ",mydict["Month"]," ",mydict["Year"])


# ## 5. Conditionals
# ### if, elif, else
# The syntax for if-else statements is very simple. **However**, notice that unlike C++, there are no brackets enclosing the block of code belonging to the if-statement! Instead, there is only indentation. This is true in general and not only for if-statements. **In Python, indentation plays the role of brackets. Make sure your indentations are aligned properly so that code belonging to the same block doesn't end up in the wrong block.** The if-statement ends when at the first line of **unindented** code.

# In[54]:


x = 1

# if
if x == 10:
    print("You will only see this if x was 10")
# if else
if x > 0:
    print("You will only see this if x is positive")
else:
    print("You will only see this if x is zero or negative")
    
# if, else if, and else
if x > 100:
    print("x is over 100")
elif x == 5:
    print("x is 5")
else:
    print("x is neither 5 nor over 100")


# ### Operations valid in conditionals
# Below is a table with operations that can be used in conditionals.
# 
# | **Symbol** | **Operation** | **Example (Value)** |
# |----:|---------------:|-----------:
# | == | is equal to | 5 == 5 (True) |
# | **is** | is equal to (NOTE: single = is assignment, double == is 'equal to') |
# | < | less than | |
# | >= | greater or equal than | |
# | <= | less or equal than | |
# | **or** | logical OR | True or False (True) |
# | **and** | logical AND | True and False (False) |
# | **in** | checks whether something is inside a container | "james" in list_of_names (True if James is in the list of names) |

# Below is an example of ```and``` and ```or```.

# In[61]:


this = False
that = False

print("What is the truth value for this/that?")
if this and that:
    print("both are true")
elif this or that:
    print("one is true")
else:
    print("neither are true")

fruits = ["apple", "banana", "peach"]

print("\nIs 'apple' in the fruit list?", "apple" in fruits)


# ### Exercise: Define a variable x = 3038 write a conditional that will print whether x is divisible by 7 or not

# In[74]:


x = 3038
y = 7
d1 = x
d2 = y
d1 %=d2

if d1 >0:
    print("x ist nicht ohne Rest durch",y,"teilbar")
else:
          print("X ist durch",y,"teilbar")


# ## 6. Loops
# There are two types of loops in Python: ```for``` and ```while```. Use the For loop when you know how many times you want to iterate the loop. Use the While loop when you don't know how many times you want to iterate the loop.
# 
# In C++ you use brackets {} to indicate the block of code belonging to a loop. In Python we use **indentation**.

# ### For loops
# In Python For loops iterate over elements in a sequence (either a list, a tuple, a dictionary, a set, or a string). Unlike C++, you do not need to define an incrementing indexing variable (such as ```i```).

# In[75]:


# create a list
fruits = ["apple", "banana", "feijoa"]

# iterate through the items of the list and print them
for f in fruits:
    print(f)


# When iterating through dictionaries, your iterator will be the keys of the dictionary.

# In[76]:


# create a dictionary
scores = {"Hanna": 4, "Markus": 3, "Amat": 5}

# iterate through its keys
for key in scores:
    print("Key:", key, "Value:", scores[key])


# To iterate through two containers at once, use the ```zip()``` function.

# In[77]:


cities = ["Chicago", "London", "Zuerich"]
countries = ["USA", "England", "Switzerland"]

for city, country in zip(cities, countries):
    print(city, "is in", country)


# ### Exercise: Increment each value in the car brand dictionary by 1 using a for loop

# In[106]:


# the dictionary
my_dictionary = {"honda": 0, "volvo": 5, "saab": 14}
print(my_dictionary)

# enter your code here to increment each car brand by 1

# the addition
for f in my_dictionary:
    my_dictionary[f] = my_dictionary[f]+1
print(my_dictionary)


# ### Using range() to get indexing variable
# If we *do* want an incrementing indexing variable we will use the ```range()``` function, which creates a sequence of numbers to iterate through. By default, ```range(x)``` will contain 0 to x-1 in integer steps. We can also add more parameters to define *start, stop, step size*: ```range(start, stop, step)```. Note that *start* is inclusive, while *stop* is not. *Step* can either be positive or negative, but needs to be integer.
# 
# It's common to combine ```range()``` and ```len()``` to iterate through the indices of a container.

# In[107]:


# iterate i from 0 to 9
for i in range(10):
    print(i)


# In[108]:


# using an index to iterate through the fruit list
for i in range(len(fruits)):
    print(fruits[i], "is at position number", i, "in the list.")


# In[109]:


# iterate from 10 to 50 in steps of 5
for i in range(10,50,5):
    print(i)


# ### Exercise: Print all integers from 100 to 80 backwards in steps of 2

# In[118]:


for i in range(100,80,-2):
    print(i)


# ### While loops
# ```while(condition)``` loops will keep iterating until the given condition is no longer true. For example, ```while(x < 5)``` will keep executing its block of code until x is NOT less than 5.
# 
# The condition is checked before each time the block in the loop is run.

# In[120]:


x = 0

while(x < 5):
    print("inside the loop, and x is", x)
    # increment x
    x += 1
print("outside the loop, and x is",x)


# A simple use of a while loop is to check that user input satisfies certain criteria. A for loop would not be very suitable for this, since we don't know how many tries it would take before the user gets it correctly.
# 
# Below is an example of entering the correct name for a roman emperor. *Note that if you get it correctly the first try, you will not even enter the loop!*
# 
# The ```input("some message")``` function will prompt the user for an input in the console, and then return that input as its return value.

# In[122]:


emperor_name = input("Please enter the name of the Roman Emperor ruling between 27 BC - AD 14: ")
while(emperor_name != "Augustus Caesar"):
    emperor_name = input("Wrong name, please try again: ")
print("That is correct!")


# ### Avoiding infinite loops
# When you write a while loop, you *NEED* to make sure that the loop has an **exit condition**. If there is no chance for the condition to be false, then you will have an infinite loop, and the rest of your code will not run. For example, ```while(True): doSomething()``` would run infinitely since True is never False (duh).

# ### Exercise: Create a variable x = 2 and create a while loop with condition x <= 1024. In the loop, update x by squaring it. Count how many times the loop runs before exiting.
# 
# **Hint:** Use a variable i to keep track of how many times the loop has executed.

# In[128]:


x = 2
c = 0
while(x<=1024):
    x = x**2
    c += 1
print(c)


# ## 7. Functions

# In the class saw all the main elements composing a function. Let's see an example of it.

# In[133]:


def my_function(param1, param2 = 3):
    if param1 == param2: 
        print("The 2 parameters have the same value")
        return None
    else: 
        summe = param1 + param2
        print(summe)
        return summe


# In[149]:


my_function(1)
my_function(1.4, 5.6)
my_function(3)
my_function(3,3)


# ### Exercise: Define your own function which accepts 1 string input (default being "Annina"). If the string ends with letter "a" or "e", function will print "Dear Mrs" and the input, otherwise will print "Dear Mr" and the input. Return the number of letters in the input. 

# In[188]:


name = input("Please enter your name: ")

if name[-1] == "a":
    print("Dear Mrs "+name)
    
elif name[-1] == "e":
     print("Dear Mrs "+name)
    
else:
    print("Dear Mr "+name)

counter = 0
for c in name:
    counter +=1
print(counter)


# ## 8. Challenges
# 
# #### 1. Print all numbers between 0-99 divisible by 7

# In[255]:


for i in range(100):
    if i % 7 == 0:   
        print(i)
    


# #### 2. Roll a dice 1000 times and store the results in a dictionary
# Use the following code to simulate a dice roll. To ask for user's input, use input() https://www.w3schools.com/python/ref_func_input.asp)

# In[282]:


from random import randint as dice
# call dice(1,6) to get a random number between 1 and 6 (inclusive)

r = input('How manny times should the dice be rolled? ')

dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(int(r)):
    value=dice(1,6)
    dict[value] += 1    
    
print(dict)


# **HINTS**
# * What should the keys and the values be of the dictionary?
# * Print the dictionary, does the distribution make sense?
# 

# #### 3. Do you want to play Rock, Paper, Scissors?

# Make a Rock-Paper-Scissors game against your computer. (Hint: Ask for player choice (using input, https://www.w3schools.com/python/ref_func_input.asp), let the computer choose a random element from the 3 possible plays (https://docs.python.org/3/library/random.html), compare the two choices, print out a message of congratulations to the winner)
# 
# Remember the rules:
# 
# Rock beats scissors <br>
# Scissors beats paper  <br>
# Paper beats rock <br>

# In[53]:


from random import choice 

print('Enter your name:')
n = input()
print()

print('Hello, ' + n)
print('What is your choice?')
print('a: Rock, b: Scissor, c: PAPER')

mensch = {"Rock": 0, "Scissor": 0, "Paper": 0}
computer = {"Rock": 0, "Scissor": 0, "Paper": 0}

x = input()

if (x == "a"):
    mensch["Rock"] +=1
    x = "Rock"
    
elif (x == "b"):
    mensch["Scissor"] +=1
else:
    mensch["Paper"] +=1

y = choice(["Rock", "Scissor", "Paper"])

if (y == "Rock"):
    computer["Rock"] +=1
    y = "Rock"
    
elif (y == "Scissors"):
    computer["Scissors"] +=1
elif (y == "Paper"):
    computer["Paper"] +=1

print("Mensch: ",mensch)  
print("Computer: ",computer)

print(x)  
print(y)
    


# In[81]:


#UNFORTUNATELY THE PROGRAMM IS NOT WORKING

from random import choice 

m = 0
c = 0

print('Enter your name:')
n = input()
print()
print('Hello, ' + n)

while (m+c != 1):    
    print('What is your choice?')
    print('1: Rock, 2: Scissor, 3: Paper')

#Mensch
    x = input()
    if (x == "1"):
        x = "Rock"
    elif (x == "2"):
        x = "Scissor"   
    elif (x == "3"):
        x = "Paper" 
    print("Mensch: ",x)  

#Maschine
    y = choice(["Rock", "Scissor", "Paper"])
    if (y == "Rock"):
        y = "Rock"    
    elif (y == "Scissors"):
        y = "Scissors"   
    elif (y == "Paper"):
        computer["Paper"] +=1
        y = "Paper"
    print("Computer: ", y)      

#Logik
    if (x == "Rock"):
        if (y == "Scissors"):
            m = 1
    elif (x == "Scissors"):
        if (y == "Paper"):
            m = 1
    elif(x == "Paper"):
        if (y == "Rock"):
            m = 1

    elif (y == "Rock"):
        if (y == "Scissors"):
            c = 1
    elif (y == "Scissors"):
        if (x == "Paper"):
            c = 1
    elif (y == "Paper"):
        if (x == "Rock"):
            c = 1
    
    if (x == y):
        print("Beide sind gleich stark, bitte noch einmal wählen...")
if (m == 1):
    print("Du hast gewonnen, hezrliche Gratulation.")
if (c == 1):
    print("Der Computer hat gewonnen.")


#Rock beats scissors
#Scissors beats paper
#Paper beats rock


# In[83]:


#sOLUTION

from random import choice
import sys

moves = ["paper", "scissors", "rock"]

user1 = input("What's your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = choice(moves)
print("The computer chose to play", user2_answer)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Congrats "+ user1+ "! Rock wins!")
        else:
            return("Unfortunately, paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Congrats "+ user1+ "! Scissors wins!")
        else:
            return("Unfortunately, rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Congrats "+ user1+ "! Paper wins!")
        else:
            return("Unfortunately, scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))

