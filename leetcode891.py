import numpy
def combinationSum(candidates, target):
  tarList, newList = [], []
  for i in candidates:
    newList.extend(numpy.repeat(i, target // i))
  newList = newList + newList + newList + newList
  print(newList)
  for i in range(len(newList)):
    temp = []
    temp.append(newList[i])
    for j in range(i + 1, len(newList)):
      if sum(temp) < target:
        temp.append(newList[j])
    if sum(temp) == target and sorted(temp) not in tarList :
      print(temp)
      tarList.append(sorted(temp))
  return tarList
        
