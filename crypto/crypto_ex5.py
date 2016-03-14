import gmpy2
from gmpy2 import mpz
import time
import bisect
N=mpz(11**8*2)
my_div = gmpy2.f_div
powmod = gmpy2.powmod
def isinlist(l,x):
    ind = bisect.bisect_left(l,x)
    if ind<len(l):
        return l[ ind ] ==x
    return False
def run(p,g,h):
    B=mpz(2**20)
    limit = B+1
    g = gmpy2.f_mod(g,p)
    hashd={}
    st = time.time()
    for x1 in xrange(limit+1):
        hashd[ gmpy2.f_mod( h* gmpy2.powmod(g,-x1,p) ,p) ] =x1
    #        if gmpy2.f_mod( h* gmpy2.powmod(g,-x1,p) ,p) <> 
    #gmpy2.f_mod( gmpy2.f_div( h, gmpy2.powmod(g,x1,p) ),p):
    #            print x1
    g_pow_B = gmpy2.powmod(g,B,p)
    print 'finished stage A',time.time()-st
    print len(hashd)
    st = time.time()
    for x0 in xrange(limit+1):
        rhs = gmpy2.powmod(g_pow_B,x0,p)
        if  rhs in hashd:
            x1=hashd[rhs]
            x0,x1 = mpz(x0),mpz(x1)
            print x0,x1,gmpy2.f_mod(x0*B+x1,p),x0*B+x1
    print 'finished stage B',time.time()-st
p=3407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g=11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h=3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
p,g,h = mpz(p),mpz(g),mpz(h)
if __name__ == '__main__':
    
    run(p,g,h)


