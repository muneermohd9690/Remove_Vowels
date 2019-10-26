# This website is for losers LOL!" would become "Ths wbst s fr lsrs LL
import re
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')


def find_vowels(s, v):
    #s = s.casefold()
    newstring = s
    for x in s:
        if x in v:
            newstring = newstring.replace(x, "")
    print("Optimized string is :", newstring)


string = input("Please enter the string: ")
find_vowels(string, vowels)

