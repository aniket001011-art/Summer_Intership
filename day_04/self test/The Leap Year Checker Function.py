year=int(input("\n Enter the year which you want to check it is a leap year or not--"))
def is_leap_year(year):
        if (year%400==0):
            return True
        else:
            return False
x = is_leap_year(year)
print(f"{year} is a leap year...",x)