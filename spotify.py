# created 9-16-21 while procrastinating much work

import json

def sum_logs(count):
  sums = {}
  total = 0
  # for each file
  for n in range(0, count):
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
  
  sorted_sum = sorted(sums.items(), key = lambda x: x[1], reverse = False) # https://careerkarma.com/blog/python-sort-a-dictionary-by-value/
  
  for i in sorted_sum:
    print(i[0])
    print(str(i[1]) + "ms", str(i[1] / 60000) + "m", str(i[1] / 3600000) + "h")
  print("TOTAL: ", str(total / 86400000) + "d")


def sum_artist(count, artist):
  total = 0
  # for each file
  for n in range(0, count):
    f = open('history' + str(n) + '.json', 'r') # https://www.tutorialspoint.com/file-objects-in-python
    data = json.load(f) # https://www.geeksforgeeks.org/read-json-file-using-python/
    # for each json entry
    for i in data:
      if (i['artistName'] == artist):
        total += i['msPlayed']
  print(str(total) + "ms", str(total / 60000) + "m", str(total / 3600000) + "h", str(total / 86400000) + "d")

sum_logs(4)
sum_artist(4, "Kalandra")