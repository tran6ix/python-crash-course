#using variables in string
#this is used combine values to display full name
first_name = "jordan"
last_name = "tran"
full_name = f"{first_name} {last_name}"
print(full_name)

#by using f immediately before open quote, Python will replave each variable with its value within the string displayed
#these are called f strings, the f is for format because Python formats the string by replacing the name of any vairable in braces with its value

#Example 1

first_name = "jordan"
last_name = "tran"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Example 2
first_name = "jordan"
last_name = "tran"
full_name = f"{first_name} {last_name}"
message = f"Hello this is a new message, {full_name.title()}!"
print(message)

#Exercise
title = "Sorcer's Stone"
author = "J.K Rowling"
message = f"{title} by {author} is a great book!"
print(message)
#Whitespaces to strings with Tabs or new lines

#Tabs
print("\tPython")

#NewLines
print("Languages:\nPython\nC#\nJavaScript")

print("\n")

#Tabs and New Lines
print("Languages:\n\tPython\n\tC#\n\tJavascript")

#Stripping whitespace using a function
#right strip
language = 'python '
print("Jordan likes",language,"very much")

language = 'python '
language =language.rstrip()
print("Jordan likes",language,"very much")

#left strip
language = ' python'
print("Jordan likes",language,"very much")

language = ' python'
language = language.lstrip()
print("Jordan likes",language,"very much")

#strip both sides
language = ' python ' 
language = language.strip()
print("Jordan likes",language, "very much")

