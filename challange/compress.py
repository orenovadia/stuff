STOP = '|'
class Node(object):
    def __init__(self, char, parent=None):
        self.char = char
        self.parent = parent
        self.childs = {}
        self.is_word = False
    def create_child(self, char):
        if char in self.childs:
            return
        self.childs[char] = Node(char, self)

    def propogate(self, word):
        if not word:
            # self.create_child('|')
            self.is_word = True
            return
        c = word[0]
        word = word[1:]
        self.create_child(c)
        self.childs[c].propogate(word)
    def speak(self, word_above):
        if self.is_word:
            print word_above + self.char
        for child in self.childs.values():
            child.speak(word_above + self.char)

class Reader(object):
    def __init__(self):
        self.filename = 'words.txt'
        self.root_node = Node('')
    def main(self):
        for word in self._iter_words():
            self.root_node.propogate(word)
        self.recreate()
    def recreate(self):
        self.root_node.speak('')
    def _iter_words(self):
        filename = self.filename

def _iter_words(filename='words.txt'):
    with open(filename, 'rb') as f:
        for i, row in enumerate(f):
            yield row.strip('\n\r\t ')
            # if i > 100000:
            #     break
if __name__ == '__main__':
    Reader().main()