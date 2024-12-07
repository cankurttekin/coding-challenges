def is_leap_year(year):
  # "extra leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400"
  if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    return True
  return False

def days_of_month(month, year):
  # 1:31 2:28 3:31 4:30 5:31 6:30 7:31 8:31 9:30 10:31 11:30 12:31
  if month == 2:
    return 29 if is_leap_year(year) else 28
  if month in [1, 3, 5, 7, 8, 10, 12]:
    return 31
  elif month in [4, 6, 9, 11]:
    return 30
  else:
    return 0

def find_first_sundays(start, end):
  # 0:Mon Tue:1 ... 6:Sun
  sunday_months = []
  day = 0

  for year in range(start, end+1):
      for month in range(1, 13):
          if day == 6:
            sunday_months.append(f"{month}/{year}")

          # TO FIRST DAY OF NEXT MONTH
          days_in_current_month = days_of_month(month, year)
          day = (day + days_in_current_month) % 7

  return sunday_months

def test_find_sundays():
    print("1.1.1900 - 31.12.2000:\n",find_first_sundays(1900, 2000))
test_find_sundays()
