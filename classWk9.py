# def message(number):
#     print("Here: ", number)

# num = int(input("int: "))
# number = num
# message(number)
# print(number)
# print(message(number))

# a=1
# b=2
# c=3
# d=99

# def adding(a,b,c):
#     d=(a+b+c)
#     return d

# e=adding(a,b,c)
# print(e)
# print(d)

# def intro(a="James Bond", b="Bond"):
#     print(f"My name is {b}. {a}.")
# intro("Susan")

# def add_numbers(a, b=2, c):
#     print(a+b+c)
# add_numbers(a=1, c=3)

def happyNewYear(wishes=True):
    print("Three")
    print("Two")
    print("One")
    if not wishes:
        print("Loser")
        return
    print("Happy New Year")
happyNewYear(False)