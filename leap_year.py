# When a function gets a year, the code detects if it ia a leap  year or not.
# A leap year is exactly divisible by 4 exept for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400.
#
# 2000 is a leap year
# 2012 is a leap year
# 1900 is not a leap year
# 2017 is not a leap year

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} is NOT a leap year')
        else:
            print(f'{year} is a leap year')
    else:
        print(f'{year} is NOT a leap year')


print(is_leap_year(2017))