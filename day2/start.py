# if 3 in list return true
def isthreeinlist(l):
    
    for n in l:
        if n==3:
            return True
    
    return False


print(isthreeinlist([1,3,7,4,5]))