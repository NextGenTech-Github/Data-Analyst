def removeDuplicatesArray(X,n):
    duplicateCount = 0
    for i in range(1,n):
        if X[i] == X[i-1]:
            duplicateCount += 1
        else:
            X[i-duplicateCount] = X[i]
    return list(set(X)), duplicateCount


# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# printing list after removal
# distorted ordering
result, count = removeDuplicatesArray(test_list,len(test_list))

print ("The list after removing duplicates : "
		+ str(result))

print ("Duplicate Count : "
		+ str(count)) 


X = [2,2,2,3,3,3,4,4,5,6,6,8,7,7,9,0]
n = len(X)

             