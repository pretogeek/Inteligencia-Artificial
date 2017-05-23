import math

lista1 = [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
newlista = []
for i in range(20):
 newlista.append(i)

#LISTA r=3
def r3(listarule1):
    u = 0
    for item in newlista:
        if(u==0):
            o = [lista1[len(lista1) - 3],lista1[len(lista1) - 2],lista1[len(lista1) - 1], lista1[u], lista1[u + 1], lista1[u + 2],lista1[u + 3]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
        if (u == 1):
            o = [lista1[len(lista1) - 2],lista1[len(lista1) - 1], lista1[u - 1], lista1[u], lista1[u + 1], lista1[u + 2],lista1[u + 3]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
        if (u == 2):
            o = [lista1[len(lista1) - 1],lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1], lista1[u + 2],lista1[u + 3]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
        if (u>2 and u<(len(lista1)-3)):
            o = [lista1[u - 3],lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1], lista1[u + 2],lista1[u + 3]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        if (u==(len(lista1)-3)):
            o = [lista1[u - 3],lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1],lista1[u + 2], lista1[0]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
        if (u==(len(lista1)-2)):
            o = [lista1[u - 3],lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1], lista1[0], lista1[1]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        if (u==(len(lista1)-1)):
            o = [lista1[u - 3],lista1[u - 2], lista1[u - 1], lista1[u], lista1[0], lista1[1],lista1[2]]
            r = magic(o)
            y = bin_to_int_7(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        u=u+1

#LISTA r=2
def r2(listarule1):
    u = 0
    for item in newlista:
        if(u==0):
            o = [lista1[len(lista1) - 2],lista1[len(lista1) - 1], lista1[u], lista1[u + 1],lista1[u + 2]]
            r = magic(o)
            y = bin_to_int_5(r)
            newlista[u] = listarule1[y]
        if (u == 1):
            o = [lista1[len(lista1) - 1], lista1[u - 1], lista1[u], lista1[u + 1], lista1[u + 2]]
            r = magic(o)
            y = bin_to_int_5(r)
            newlista[u] = listarule1[y]
        if (u>1 and u<(len(lista1)-2)):
            o = [lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1], lista1[u + 2]]
            r = magic(o)
            y = bin_to_int_5(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        if (u==(len(lista1)-2)):
            o = [lista1[u - 2], lista1[u - 1], lista1[u], lista1[u + 1], lista1[0]]
            r = magic(o)
            y = bin_to_int_5(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        if (u==(len(lista1)-1)):
            o = [lista1[u - 2], lista1[u - 1], lista1[u], lista1[0], lista1[1]]
            r = magic(o)
            y = bin_to_int_5(r)
            newlista[u] = listarule1[y]
            #print("**: %s" % newlista[u])
        u=u+1

# ULTIMO r=1
def ultimo(i,listarule):
    lt = (lista1[i - 1], lista1[i], lista1[0])
    w = magic(lt)
    a = bin_to_int_3(w)
    newlista[i] = listarule[a]

# PRIMEIRO r=1
def primeiro(i,listarule):
    o = [lista1[len(lista1) - 1], lista1[i], lista1[i + 1]]
    r = magic(o)
    y = bin_to_int_3(r)
    newlista[i] = listarule[y]
   #print("primeiro nova lista: %s" % newlista[i])

def rotate(number):
    newl=[]
    a = list(str(number))
    for b in reversed(a):
        newl.append(b)
    s = ''.join(map(str, newl))
    return s

# ELEMENTS LIST TO INT
def magic(myList):
    s = ''.join(map(str, myList))
    return str(s)

# BIN TO DEC r=1
def bin_to_int_3(x):
   i=2
   r=0
   a=list(str(x))
   for item in a:
       r=r+((int(item))*(2**i))
       i=i-1
   return r

# BIN TO DEC r=2
def bin_to_int_5(x):
   i=4
   r=0
   a=list(str(x))
   for item in a:
       r=r+((int(item))*(2**i))
       i=i-1
   return r

# BIN TO DEC r=3
def bin_to_int_7(x):
   i=6
   r=0
   a=list(str(x))
   for item in a:
       r=r+((int(item))*(2**i))
       i=i-1
   return r

# DEC TO BIN
def dec_to_bin(x):
    return int(bin(x)[2:])

# REVERSE NUMBER
def reverse(number):
    res = 0;
    while(number>0):
        res=res<<1
        res = res|(number & 1)
        number=number>>1
    return res

# ADD ZERO'S r=1
def addzero(number):
    number1=number.__str__()
    e=number1.zfill(8)
    return e

# ADD ZERO'S r=2
def addzero1(number):
    number1=number.__str__()
    e=number1.zfill(32)
    return e

# ADD ZERO'S r=3
def addzero2(number):
    number1=number.__str__()
    e=number1.zfill(128)
    return e

def program(lista1, rule, r):
   if r==1:
       rule1 = dec_to_bin(rule)
       rule2 = addzero(rule1)
       print("Regra original (%d) (antes de invertida): %s"%(rule,rule2))
       rulefinal = rotate(rule2)
       print("Regra invertida: %s"%rulefinal)
       listarule=list(str(rulefinal))
       primeiro(0, listarule)
       ultimo((len(lista1)-1), listarule)
       j=1
       while j<(len(lista1)-1):
           u = [lista1[j - 1], lista1[j], lista1[j + 1]]
           k = magic(u)
           t = bin_to_int_3(k)
           newlista[j] = listarule[t]
           j=j+1
       for ig in newlista:
           print(" %s"% ig)

   if r==2:
       rule11 = dec_to_bin(rule)
       rule22 = addzero1(rule11)
       print("Regra original (%d) (antes de invertida): %s" % (rule, rule22))
       rulefinal1 = rotate(rule22)
       print("Regra invertida: %s" % rulefinal1)
       listarule1=list(str(rulefinal1))
       r2(listarule1)
       for ig in newlista:
           print("*%s"% ig)

   if r == 3:
       rule111 = dec_to_bin(rule)
       rule222 = addzero2(rule111)
       print("Regra original (%d) (antes de invertida): %s" % (rule, rule222))
       rulefinal11 = rotate(rule222)
       print("Regra invertida: %s" % rulefinal11)
       listarule11 = list(str(rulefinal11))
       r3(listarule11)
       for ig in newlista:
         print("*%s" % ig)
program(lista1,444555, 3)


