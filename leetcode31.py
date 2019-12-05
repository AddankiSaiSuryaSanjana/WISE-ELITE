nums = [6,7,5,3,5,6,2,9,1,2,7,0,9]
k  = []
k.extend(nums)
nums.sort()
targetList = list(permutations(nums , len(nums)))
print(targetList)
targetList.reverse()
index = targetList.index(tuple(k))
nums.clear()
if index == 0:
  nums.extend(list(targetList[len(targetList)-1]))
else :
  nums.extend(list(targetList[index - 1]))
print(targetList)
print(nums)
