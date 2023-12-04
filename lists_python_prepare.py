"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of 
commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding 
operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    start = []
    new = []
    
    for i in range(N):
        x = input().split()
        start.append(x)
    
    for i in range(len(start)):
        if start[i][0] == 'insert':
            x = int(start[i][1])
            y = int(start[i][2])
            
            new.insert(x,y)
    
        elif start[i][0] == 'print':
            print(new)
        
        elif start[i][0] == 'remove':
            new.remove(int(start[i][1]))
            
        elif start[i][0] == 'append':
            new.append(int(start[i][1]))
            
        elif start[i][0] == 'sort':
            new.sort()
            
        elif start[i][0] == 'pop':
            new.pop()                
        
        elif start[i][0] == 'reverse':
            new.reverse()
