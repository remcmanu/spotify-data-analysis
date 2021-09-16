# spotify-data-analysis
Tools to analyze personal Spotify data. (I'm also storing my data here, which is probably not useful for anyone else)

## To Use

1. Place `spotify.py` into the "MyData" directory Spotify provides upon request. 

2. Rename the streaming history files (I usually only have at max two of them (0 and 1)) to historyN, where N starts at 0. 

3. Remove duplicate entries from between the different files. I'll briefly describe how I did this: Given I had two data requests each with two files, I found the last element of the first download (located in `history1`)
```
  {
    "endTime" : "2021-02-04 19:02",
    "artistName" : "Angèle",
    "trackName" : "Ta reine",
    "msPlayed" : 38160
  }
```
I found this same entry in `history2`, and deleted it and everything that came before it.

4. If running `spotify.py` directly, change `count` to be equal to the number of files you have.

## Functions

**sum_logs(count):** *calculates total stream time of a given song in miliseconds (ms), minutes (m), hours (h), and total listen time in days (d).*

Example Output:
```
It Gets Easier by Kalandra
18795794ms 313.26323333333335m 5.221053888888889h
Borders by Kalandra
19618716ms 326.9786m 5.449643333333333h
Slow Motion by Kalandra
19727845ms 328.79741666666666m 5.479956944444444h
Brave New World by Kalandra
21810758ms 363.5126333333333m 6.058543888888889h
Helvegen by Kalandra
26543828ms 442.39713333333333m 7.373285555555555h
TOTAL:  44.603921712962965d
```

**sum_artist(count, artist):** *calculates total stream time of a given artist in miliseconds (ms), minutes (m), hours (h), and days (d).*

Example Output:
```
394604740ms 6576.745666666667m 109.61242777777778h 4.567184490740741d
```
