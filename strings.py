txt = "She said \"Never let go\"."
print(txt)


game = "Popular Nintendo Game: Mario Kart"
print("l" in game)
print("x" in game)


str = 'yellow'
print(str[1])
print(str[-1])
print(str[4:6])
print(str[:4])
print(str[-3:])


x = 'One fish,'
y = 'two fish.'
z = x + y
print(z)


fruit = "Berry"
print(fruit[2])


#  iterate
str = "hello"
for c in str:
    print(c)


length = len("Hello")
print(length)


greeting = "Welcome To The World"
print(greeting.lower())


greeting = "Welcome To The World"
print(greeting.upper())


# splitting
text = "Silicon Valley"
print(text.split())   #['Silicon', 'Valley']
print(text.split('i'))  #['S', 'l', 'con Valley']


x = "_".join(["Codecademy", "is", "awesome"])
print(x)


# to remove empty spaces
text1 = ' apples and oranges '
print(text1.strip())
text2 = '   +   lemons and limes   -   '
print(text2.strip())


# to replace
fruit = "Strawberry"
print(fruit.replace('r', 'R'))  # StRawbeRRy


mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o"))   # 1


msg1 = 'Fred scored {} out of {} points.'
print(msg1.format(3, 10))    # Fred scored 3 out of 10 points


str3 = 'abcde'
print(str3[:2])