import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
            print 'We got %s'%f.code
            return f.code
        except urllib2.HTTPError, e:
            print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding
class Work(object):
    original_ct = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'
    ct_bytes = original_ct.decode('hex')
    ct = bytearray(ct_bytes)
    ct_length = len(ct_bytes)
    block_size_bit = 128
    block_size = 128/8
    number_of_blocks =  ct_length / block_size
    iv_length = ct_length % block_size or block_size
    
    plain_text_dict = {}
    po = PaddingOracle()
    
    def random_block(self):
        return 'a'.decode('hex')*self.block_size
    def block_list_to_result(self,block_list):
        msg = (''.join(block_list)).encode('hex')
        print 'requesting %s'%msg
        return self.po.query(msg)
    def make_block_with_padding_guesses(self,block_array,index,pad_len
                                        ,n_block_to_change):
        block_array = bytearray(block_array)
        for ind,val in self.guesses.items():
            if not index <= ind <= n_block_to_change*self.block_size:
                continue
            block_array[ind] = block_array[ind]^val^pad_len
        return block_array
    def q(self,block_list):
        r =  str(block_list).encode('hex')
        return self.po.query(r)
    def work_on_block(self, block_n):
        relevant_blocks = bytearray(self.ct)
        relevant_blocks = relevant_blocks[: block_n*self.block_size ]
        print 'Working on bytestr len of',len(relevant_blocks),'block n:',block_n
        n_block_to_change = block_n-1
        print 'Modifying block %s'%n_block_to_change
        start_from = self.block_size*n_block_to_change -1
        end_in = self.block_size*(n_block_to_change -1)
        pad_len = 1
        for i in range( start_from,end_in,-1):
            sys.stdout.flush()
            found = False
            for g in range(8,256):
                print 'i',i,'g',g,'pad',pad_len
                self.guesses[i] = g
                
                new_block = self.make_block_with_padding_guesses(
                        relevant_blocks,i,pad_len,n_block_to_change
                    )

                pad_okay =  self.q(new_block)
                if pad_okay and pad_okay!=200:
                    pad_len += 1
                    print self.guesses
                    found = True
                    break
            if not found:
                pad_len += 1
                self.guesses[i] = pad_len
                print self.guesses
            
                

    def run(self):
        print 'CT = %s'%self.ct_bytes
        print 'CT length = %s'%self.ct_length
        print 'IV len %s'%self.iv_length
        print 'number_of_blocks %s'%self.number_of_blocks
        print '='*30
        self.guesses = {}
        for working_on_block_n in range(self.number_of_blocks,self.number_of_blocks-2,-1):
            print 'working on block %s'%working_on_block_n
            self.work_on_block(working_on_block_n)
            print self.guesses
if __name__ == "__main__":
    #po = PaddingOracle()
    #print po.query(sys.argv[1])       # Issue HTTP query with the given argument
    Work().run()



'''
    if self.iv_length == self.block_size:
    block_list = [self.ct_bytes[i*self.block_size:i*self.block_size +self.block_size] for i in range(self.number_of_blocks)  ]
    else:
    block_list = [self.ct_bytes[:self.iv_length]] +[self.ct_bytes[self.iv_length + i*self.block_size:self.iv_length +i*self.block_size +self.block_size] for i in range(self.number_of_blocks)  ]
'''