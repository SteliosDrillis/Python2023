 

def recursion_function(n):
    if n == 0:
        return 1
    else:
        return n * recursion_function(n-1) 
    

x = int(input("dose arithmo gia paragontiko: "))
print(recursion_function(x))