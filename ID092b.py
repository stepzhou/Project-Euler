# Better cache solution from the PE forums

def digsum(limit): 
    sqsum=0
    while limit:
        dig =limit%10
        limit/=10
        sqsum+=dig*dig
    return sqsum

e89=set([89])
e1=set([1])
count=0
for n in range(1,7*9*9+1):
    trail=set([n])
    while True:
        if n in e89:
            count+=1
            e89.update(trail)
            break
        if n in e1:
            e1.update(trail)
            break
        n=digsum(n)
        trail.add(n)
        
for n in range(568,10000000):
    if digsum(n) in e89: count+=1
                       
print count