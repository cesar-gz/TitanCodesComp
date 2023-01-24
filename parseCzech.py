"""
Kolik času celkem strávil zaměstnanec 9 a zaměstnanec 4 odbavením? Sečtěte jejich celkový čas odbavení a odešlete jej pro označení. 
Dejte odpověď během několika sekund. Číslo nebude obsahovat žádná desetinná místa, pokud je provedeno správně

czech translated to english:

How much total time did employee 9 and employee 4 spend checking in? 
Add up their total clearance time and submit it for marking. 
Give an answer in seconds. The number will not contain any decimal places if done correctly
"""

import csv

rows = []

listOf9s = []
listOf4s = []


with open("checkincheckout.csv", 'r') as file:
  csvreader = csv.reader(file)

  header = []
  header = next(csvreader)

  for row in csvreader:
    #print(row)
    rows.append(row)

  bigList = [item[0] + " " + item[2] + " " + item[3] for item in rows]
  for x in bigList:
    #print(x)
    temp = []
    temp = x
    if temp[0][0] == '9':
      #print(x)
      listOf9s.append(x)
    if temp[0][0] == '4':
      listOf4s.append(x)

totalClearanceFor9 = 0
totalClearanceFor4 = 0

for i in range(len(listOf9s)):
  #print(listOf9s[i])
  temp2 = listOf9s[i]
  temp2 = temp2[13:21]
  temp2 = int(temp2[0:2])

  temp3 = listOf9s[i]
  temp3 = temp3[40:48]
  temp3 = int(temp3[0:2])
  if temp2 == 00:
    temp2 += 12
  if temp3 == 00:
    temp3 += 12
  if temp2 > 12:
    temp2 -= 12
  if temp3 > 12:
    temp3 -= 12
  #print(temp3)
  result = temp3 - temp2
  if(result < 0):
    result = abs(result)
  totalClearanceFor9 += result
  #print(result)
  #print(totalClearanceFor9)

for i in range(len(listOf4s)):
  #print(listOf4s[i])
  temp2 = listOf4s[i]
  temp2 = temp2[13:21]
  print(temp2)
  temp2 = int(temp2[0:2])

  temp3 = listOf4s[i]
  temp3 = temp3[40:48]
  print(temp3)
  temp3 = int(temp3[0:2])
  
  if temp2 == 00:
    temp2 += 12
  if temp3 == 00:
    temp3 += 12
  if temp2 > 12:
    temp2 -= 12
  if temp3 > 12:
    temp3 -= 12
  result = temp3 - temp2
  if(result < 0):
    result = abs(result)
  print(result)
  print("")
  totalClearanceFor4 += result

print((totalClearanceFor9 + totalClearanceFor4)*3600)
#