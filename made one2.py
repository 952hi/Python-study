import math
import sys
def madeonedigit():
    x = int(input())
    result= [0,1,1,1,2,1]
    
    for i in range(6,x+1):
        case = result[i-1]
        case1,case2,case3 = math.inf,math.inf,math.inf
        
        if i % 2 == 0:
            case1 = result[i//2]
        if i % 3 == 0:
            case2 = result[i//3]
        if i % 5 == 0:
            case3 = result[i//5]
        compare = 1+min(case,case1,case2,case3)
        
        result.append(compare)
    
    print(result[x])

madeonedigit()    

      
        

    

