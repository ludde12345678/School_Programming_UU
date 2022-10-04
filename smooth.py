
def smooth_a(a:list, n:int):
    returnlist = []; # Skapar en tom lista, Det är denna lista som ska fyllas och ges tillbaka av funktionen
    for y in range(0,len(a)): # Loopar mellan 0 och längden på listan
        val = 0; # skapar variablen som ska läggas in i listan 
        for x in range(-n, n+1): # loopar från -n till n+1, så om n=2 så loppar den från -2 till 3 eller 5 ggr
            val += a[max(0, min(y+x+1, len(a))-1)] # adderar val med värdet på listan vid index max(0, min(y+x+1, len(a))-1). om n = 2 så adderar alla värden från 2 steg till vänster i listan till 2 steg till höger i listan. Om någon av dessa värden skulle vara utanför listan(utanför 0 till len(list)) så tar den antingen 0 om den är utanför till vänster eller len(list) om den är utanför till höger för alla de värden som är utanför
        returnlist.append(val/( 2*n + 1)) # Val är nu summan av -n till n+1 värden(om n =2 så är val summan av 5 värden) och delas därför med 2*n + 1(om n=2 så är 2n+1 = 5) för att få medelvärdet av alla adderade siffror. Detta resultat läggs sedan in sist på den nya return listan
    return returnlist
        
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