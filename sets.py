# Set Functions in Python Using List Comprehensions

def union(A, B):
    return [e for e in A if e not in B] + B

def intersection(A, B):
    return [e for e in A if e in B]

def setdiff(U, A):
    return [e for e in U if e not in A]

def symdiff(A, B):
    return setdiff(union(A, B), intersection(A, B))

def cartprod(A, B):
    return [(a, b) for a in A for b in B]

# Testing
a = [1, 2]
b = [2, 3, 4]
print union(a, b)
print intersection(a, b)
print setdiff(a, b)
print symdiff(a, b)
print cartprod(a, b)
