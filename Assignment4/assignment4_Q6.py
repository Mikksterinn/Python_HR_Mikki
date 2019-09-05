top_num = int(input("Upper number for the range: ")) # Do not change this line
a=0
for i in range(1,top_num):
    
    for j in range(1, i):
        if i%j == 0:
            a=a+j
    if a == i:
        print(a)
        
    a=0
        
