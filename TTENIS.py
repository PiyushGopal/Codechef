# cook your dish here
t=int(input())
for i in range(t):
    a=input()
    chef,flag=0,0
    opponent=0
    for j in a:
        if(j=='1'):
            chef+=1 
        else:
            opponent+=1 
            
        if chef == 11:
            print("WIN")
            break
        elif opponent == 11:
            print("LOSE")
            break
        
        elif chef == 10 and opponent == 10:
            chef = 0
            opponent = 0
            flag = 1
        
        elif flag ==  1:
            if chef:
                if opponent:
                    chef = 0
                    opponent = 0
                elif chef == 2:
                    print("WIN")
                    break
            else:
                if chef:
                    chef = 0
                    opponent = 0
                elif opponent == 2:
                    print("LOSE")
                    break
