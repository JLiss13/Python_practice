
def ContainsCommonItem(array_1, array_2):
    commonItemDict = {}
    for i in range(len(array_1)):
        commonItemDict[array_1[i]] = True
    
    for j in range(len(array_2)):
        if array_2[j] in commonItemDict:
            print("true")
            return True
    print("false")      
    return False
    

# Use case 1
array_1 = ['a','b','c','x']
array_2 = ['z','y','i']

ContainsCommonItem(array_1,array_2)

#Use case 2
array_1 = ['a','b','c','x']
array_2 = ['z','y','x']
     
ContainsCommonItem(array_1,array_2)
        