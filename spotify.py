# created 9-16-21 while procrastinating much work
# updated 1-12-22 while on break, procrastinating some work

import json
from datetime import date


def songs_sum(year1, mode="lifetime", decimal_place=2):
  """Find the amount of time you listened to given songs in Spotify (total/per year).\n  mode="lifetime" (where year1 is first file's year)\n  mode="year" (where year1 is single year)\n decimal_place=#s after decimal"""
  
  today = date.today() # https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/
  current_year = today.year

  sums = {}
  total = 0
  
  if (mode == "lifetime"): # year1 = first file's year
    year2 = current_year + 1
  elif (mode == "year"): # year1 = year to analyze
    year2 = year1 + 1
  
  # for each year file
  for n in range(year1, year2):
    f = open('history' + str(n) + '.json', 'r') # https://www.tutorialspoint.com/file-objects-in-python
    data = json.load(f) # https://www.geeksforgeeks.org/read-json-file-using-python/
    # for each json entry
    for i in data:
      total += i['msPlayed']
      combinedStr = i['trackName'] + " by " + i['artistName']
      # add to existing, or create new entry
      if (combinedStr in sums):
        sums[combinedStr] = sums[combinedStr] + i['msPlayed']
      else:
        sums[combinedStr] = i['msPlayed']
    f.close() # https://www.tutorialspoint.com/python/file_close.htm
  
  sorted_sum = sorted(sums.items(), key = lambda x: x[1], reverse = False) # https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
  
  for i in sorted_sum:
    print(i[0])
    print("    " + str(round(i[1], decimal_place)) + "ms", str(round(i[1] / 60000, decimal_place)) + "m", str(round(i[1] / 3600000, decimal_place)) + "h")
  print("TOTAL: ", str(round(total / 86400000, decimal_place)) + "d")


def artists_sum(year1, mode="lifetime", decimal_place=2):
  """Find the amount of time you listened to given artists in Spotify (total/per year).\n  mode="lifetime" (where year1 is first file's year)\n  mode="year" (where year1 is single year)\n decimal_place=#s after decimal"""
  
  today = date.today()
  current_year = today.year

  sums = {}
  total = 0

  if (mode == "lifetime"): # year1 = first file's year
    year2 = current_year + 1
  elif (mode == "year"): # year1 = year to analyze
    year2 = year1 + 1
  
  # for each file
  for n in range(year1, year2):
    f = open('history' + str(n) + '.json', 'r')
    data = json.load(f)
    # for each json entry
    for i in data:
      total += i['msPlayed']
      artistName = i['artistName']
      # add to existing, or create new entry
      if (artistName in sums):
        sums[artistName] = sums[artistName] + i['msPlayed']
      else:
        sums[artistName] = i['msPlayed']
    f.close()
  
  sorted_sum = sorted(sums.items(), key = lambda x: x[1], reverse = False)
  
  for i in sorted_sum:
    print(i[0])
    print("    " + str(round(i[1], decimal_place)) + "ms", str(round(i[1] / 60000, decimal_place)) + "m", str(round(i[1] / 3600000, decimal_place)) + "h")
  print("TOTAL: ", str(round(total / 86400000, decimal_place)) + "d")

songs_sum(2020)