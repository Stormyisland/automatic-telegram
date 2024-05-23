# ask user name
name = input("What is your name? ") .strip().title()

#remove white space
#name = name.strip().title()

first, middle, last, = name.split(" ")



print(f"hello {last}")