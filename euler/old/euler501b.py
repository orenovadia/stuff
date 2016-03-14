from eulertools import Dn,primeFactors
from itertools import groupby,combinations
from math import log,sqrt,factorial

N=1000
minimal = N
'''from eulertools import primes
prm = primes(N/6)
print prm 
exit(0)
'''
filename = 'primes%d.txt' % (N/6)
#prm =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163]
#with open (filename,'rb') as f:
#    prm = eval(f.read())
prm =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163]

'''
Allowed Permutations:
1,1,1
3,1
7
'''
#print prm

nPrm =  len ( prm )
import sys
sys.setrecursionlimit(nPrm*2 +1)

def calcNum(l,prm):
    s=1
    for i,pows in enumerate(l):
        s*=prm[i]**pows
    return s


def powerCheck(n):
    global prm,minimal,nSols,goal,itm,dontpass,ll
    
    if n==itm: return
    d = Dn(ll[:n+1])
    while d<goal and ll[n]<dontpass:
        ll[n]+=1
        d= Dn(ll[:n+1])
        if d==goal:
            #print d , l[:n+1]
            dn = calcNum(ll[:n+1],prm)
            if dn<= minimal:
                #print dn #,l[:n+1]
                nSols+=1
            else:
                break
        else:
            powerCheck(n+1)
    l[n]=0
    powerCheck(n+1)
 
 
def nC2(n):
    return (n)*(n-1)/2
def nC3(n):
    return (n)*(n-1)*(n-2)/6


def powerCheckThree1s(n):
    return 0
    mul = lambda x,y: x*y
    global prm,minimal,nSols,goal,itm,l,N
    nPrm = len (prm)
    mu,j=0,0
    while mu <N:
        j+=1
        mu = reduce( mul , prm[j:j+3])
    i,j= j, j+1 #j is the third, i the second  
    nSols += nC3(j+1)
    #print nSols,i,j
    j+=1
    while j<nPrm:
        while (prm[i]*prm[i-1]*prm[j])>N and i>0:
            i-=1
        nSols+=nC2(i+1)
        print nSols,nC2(i+1),'j:',j,'i:',i
        j+=1
    return

    
   

def p1p2_p1pow3_nSols(factors):
    s = 0
    #factors = primeFactors(n)
    counts = [len(list(group)) for key, group in groupby(factors)]
    for x in counts: 
        if x==3: s+=1 
    factors = set(factors)
    nprmimes = len(factors)
    
    if nprmimes>=2:
        s+= factorial(nprmimes)/(2*factorial(nprmimes-2))
    #print factors,nprmimes,s
    return s

def count7s(n,plist):
    s=0
    for i in plist:
        if i**7<=n:
            s+=1
            #print i,i**7
        else: break
    return s

nSols = 0
'''
l=[]
for i in prm:
    l.append(N/i)
print l 
exit(0)
for i in xrange(len(prm)-1,len(prm)-50,-1):
    print prm[i] , N/prm[i]
    
exit(0)
for i in range(10**6,10**6-200,-1):
    print i,max(primeFactors(i)),primeFactors(i)
'''
def numberOfThirdPowers(prm,divisor):
    s=0
    for i in prm:
        if i**3<=divisor:
            s+=1
        else: break
    return s

nSols = 0
divisor=0
prevDivisor =0
prevDivisorSet = set()
oldDivisorSets_p1xp2 = set()
gag=int(sqrt(N)*2)
step=0
step11Combo=0

print 'nPrm' , nPrm
print 'after bigOnes' , nSols
nPrm = len(prm)
print 'nPrm' , nPrm
l=[0]*nPrm
goal =8
ll=l
itm = nPrm
dontpass=1
powerCheckThree1s(0)

print 'after powerCheckThree1s' , nSols

nSols+=count7s(N, prm)
print 'after count7s' , nSols
for i in prm:
    i3=i**3
    for j in prm:
        if i3*j>N: break
        elif i!=j: 
            nSols+=1
            #print i,j

print 'after i3*j' , nSols
print 'nsols:',nSols
