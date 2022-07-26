def data_distribute(input_data):
    a = input_data.split(',')
    a= list(a)
    indexi = []
    num  =[]
    present = 0 
    current = 0
    for i in range(len(a)) :
        if a[i] != "_" :
            indexi.append(a[i])  
            num.append(i)
    for i in range(len(num)) :
        
        present = num[i]
        if present == 0 :
            pass
        else :
            if a[current] == '_' :
                p = 0
            else :
                p = a[current]
            a[current:present+1] = [int((  int(a[present]) +   int(p)) /   (present -current+1)   )]  *  (present -current+1)


        current = present
    if a[-1] == '_':
        a[present:]= [int(int(a[present])/((len(a)-present)))]*(len(a)-present) 
    return a
    