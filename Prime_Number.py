"""
入力した整数が素数であるかを判別
"""

def Divisor(n):
    divisor = []
    for i in range(1,n+1):
        if(len(divisor) == 2):
            break
        r = n % i
        if(r == 0):
            divisor.append(i)       
    Judge(divisor)
    
def Judge(list):        
    if(list[0] == 1 and list[1] == n):
        print(n,"は素数です")
    else:
        print(n,"は素数ではありません")
        
n = int(input("整数を入力："))
Divisor(n)
