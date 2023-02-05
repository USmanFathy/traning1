#find Missing Number



def findmissingnumber(list):

    numbers = set(list)
    missingnumbers = []
    
    for num in range ( 1,list[-1]):
        if num  not in numbers :
            missingnumbers.append(num)

    return missingnumbers


listofnumbers = [ 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]


print(findmissingnumber(listofnumbers))