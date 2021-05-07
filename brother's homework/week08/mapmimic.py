def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 


def mapmimic(func, iter):
    for elem in iter:
        yield(func(elem))




numbers2 = (1, 2, 3, 4) 
result2 = mapmimic(addition, numbers2) 
print(list(result2)) 