# python3
import sys
import threading
import numpy as np

def compute_height(n, parents):
   
    max_height = 0
    height = np.zeros(n, dtype=np.int32)
    
    for i in range(n):
        heightA = 0
        current = i
        while current!=1:
            if height[current]!=0:
                heightA= heightA+height[current]
                break
            else:
                heightA = heightA + 1
        height[i]=heightA
        max_height = max(max_height, heightA)
                
        
    return max_height
 

def main():

    i = input()
    if 'i' in i.lower():   
        n = int(input())
        parents = list(map(int, input().split()))
        
    elif 'f' in i.lower():  
        file_name = input()
        if 'a' in file_name:
            return
        try:
            with open("./test/"+file_name, mode='r',encoding="utf8") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            return
    else:
        return
    height = compute_height(n, parents)
    print(height)
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
