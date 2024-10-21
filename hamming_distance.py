str1 = input("Input the first string: ")
str2 = input("Input the second string: ")
distance = 0
length = len(str1)
for i in range(length):
        char1 = str1[i]
        char2 = str2[i]
        if char1 != char2: 
            distance += 1  
            
if len(str1) == len(str2):
    print ("The hamming distance between ", str1, "and ", str2, "is ", distance)
else:
    print("Strings must be in the same length.")
    
