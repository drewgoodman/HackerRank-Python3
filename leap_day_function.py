# WRITE A FUNCTION: LEAP DAY


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          leap = True
      else:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))