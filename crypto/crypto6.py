import gmpy2
from math import ceil
import time

def find_sqrt(N):
    n =gmpy2.floor(
                  gmpy2.sqrt(
                             gmpy2.mpfr(N,precision = len(str(N))+50  )
                             )
                  )
    n = gmpy2.mpz(n)
    for i in xrange(-2**10,2**20,1):
        #print (n+i)**2>N
        if (n+i)**2>N:
            print 'found'
            return n+i
    assert False,'bla'
def main(N):
    c=gmpy2.context()
    c.precision=len(str(N))+20
    c.real_prec=len(str(N))+20
    gmpy2.set_context(c)
    assert N==gmpy2.mpz(N)
    N=gmpy2.mpz(N)
    A=find_sqrt(N)
    A = gmpy2.mpz(A)
    assert ( (A-1)**2<N<A**2 ),'not found'
    Atag = A
    for iA in xrange(-2**20,2**20):
        A = Atag + iA
        s =A**2-N
        x = gmpy2.sqrt(s)
        try:
            x = gmpy2.mpz(x)
        except:continue
        print x**2 > s ,  x**2 < s
        '''while x**2>s:
            x-=1
            print 1,'''
        print x**2 > s ,  x**2 < s

        p = A-x
        q = A+x
        q = N/p

        if p*q==N:
            print gmpy2.is_prime(q)
            print gmpy2.is_prime(p)
            print min(p,q)
            break
def main23(N):
    c=gmpy2.context()
    c.precision=len(str(N))+20
    c.real_prec=len(str(N))+20
    gmpy2.set_context(c)
    assert N==gmpy2.mpz(N)
    N=gmpy2.mpz(N)
    A=find_sqrt(6*N)
    A = gmpy2.mpz(A)
    assert ( (A-1)**2<6*N<A**2 ),'not found'
    Atag = A
    for iA in xrange(-2**20,2**20):
        A = Atag + iA
        s =A**2-N
        x = gmpy2.sqrt(s)
        try:
            x = gmpy2.mpz(x)
        except:continue
        '''print x**2 > s ,  x**2 < s
        while x**2>s:
            x-=1
            print 1,
        print x**2 > s ,  x**2 < s'''
        for p in [(A-x)/2,(A-x)/3,(A+x)/2,(A+x)/3   ]:
            q = N/p
            
            if p*q==N:
                print gmpy2.is_prime(q)
                print gmpy2.is_prime(p)
                print min(p,q)
                assert False,'bla'
N=720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929
st = time.time()
main23(N)
print 'time %.3f'%(time.time()-st)