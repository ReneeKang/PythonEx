import random

n = random.randint(1,30)

while True:
    
    x = input("맞춰보세요")
    
    g = int(x)

    if(g)==n:
        
        print("정답")
        
        break
    if g<n :
        
        print("작아")
        
    if g>n :
        
        print("커요")
        
