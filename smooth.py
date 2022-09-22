
def smooth_a(a:list, n:int):
    returnlist = [];
    for y in range(0,len(a)):
        val = 0;
        for x in range(-n, n+1):
            val += a[max(0, min(y+x+1, len(a))-1)]
        returnlist.append(val/( 2*n + 1))
    
        
def smooth_b(a:list, n:int):
    returnlist = [];
    for y in range(0,len(a)):
        val = 0;
        valcounter = 0;
        for x in range(-n, n+1):
            if(not(y+x < 0 or x+y > len(a)-1)):
                val += a[max(0, min(y+x+1, len(a))-1)]
                valcounter += 1;
        returnlist.append(val/valcounter)
    return returnlist;


def math(x):
    k=2
    m=1
    return k*x+m
        
list = [1,2,3,4]
val = smooth_a(list, 2)
print(val)

print(math(5))