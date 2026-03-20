def number():
    while True:
        n=int(input("give a number"))
        if n>0:
            return n
def strecture(n,f1,f2):
    f1=open(f1,"a")
    f2=open(f2,"a")
    e={"cycle":"","period":0}
    f2.write(str(n)+"\n")
    test=True
    ch=""
    p=0
    while test:
        ch+=str(n)+"#"
        b=base_2(n)
        b=b[::-1]
        x=base_10(b)
        x+=2
        if str(x) in ch:
            test=False
            ch+=str(x)+"#"
        n=x
        p+=1
    e["cycle"]=ch
    e["period"]=p    
    f1.write(str(e)+"\n")
    f1.close()
    f2.close()
    
def base_2(n):
    if n == 0:
        return "0"
    ch = ""
    while n != 0:
        r = n % 2
        ch = str(r) + ch
        n = n // 2
    return ch

def base_10(b):
    d=0
    p=1
    for i in range(len(b)-1,-1,-1):
        d=d+int(b[i])*p
        p=p*2
    return d

def result(f1,f2):
    f1=open(f1,"r")
    f2=open(f2,"r")
    print(f2.read())
    print(f1.read())
    f1.close()
    f2.close()
    

n=number()
f1="amplitude.txt"
f2="depart.txt"
strecture(n,f1,f2)
result(f1,f2)