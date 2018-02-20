def FilterImplementation(x,*d): #Basic MapImplementation
    deneme=[]
    for t in list(zip(*d)):
        if bool(x(*t)):
            deneme.append(*t)
    return deneme
FilterImplementation(lambda x:x%2==0,[1,2,3,4,5])
