def Son_paralelos(v1,v2): 
    (a,b)=v1
    (c,d)=v2
    result1= (a/c)
    result2= (b/d)
    
    if result1==result2 : 
        print("Los vectores,", v1, v2 ,"son paralelos")
    if result1!=result2: 
        print("Los vectores,", v1, v2 ,"no son paralelos")

Son_paralelos((3,-5),(-6,10))
Son_paralelos((3,2),(-6,9))
