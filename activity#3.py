import array as arr

#create an arr
arr_num = arr.array('i', [1,3,5,3,7,9,3])
print("original arr:"+str(arr_num))

# count number or occurences
print("number of occurrences of the number 3 in the said arr:"+str(arr_num.count(3)))

# reverse the arr
arr_num.reverse()
print("reverse the order of the items:")
print(str(arr_num))

