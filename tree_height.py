# python3
import sys
import threading

def compute_height(n, parents):
    
    depths = [0] * n
    queue = [-1]
    while queue:
        parent = queue.pop(0)
        children = [i for i in range(n) if parents[i] == parent]
        for child in children:
            depths[child] = depths[parent] + 1
            queue.append(child)
            
    return max(depths)

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
