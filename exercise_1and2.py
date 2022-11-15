# Question 1
# Filter list with nums less than 10
list = [1,11,14,5,8,9]
for item in list:
  if item < 10:
    print(item)



# Question 2
# Merge and sort two list
def mergeSort(l_1, l_2):
    final_list = l_1 + l_2
    final_list.sort()
    return(final_list)
  
# Num lists
l_1 = [25, 18, 9, 41, 26, 31]
l_2 = [25, 45, 3, 32, 15, 20]
print(mergeSort(l_1, l_2))