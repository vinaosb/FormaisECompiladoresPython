class Tree:
    childs = []
    value = ''
    

    def __init__(self):
        self.childs = [None, None]
        self.value = ''


    def setLeft(self, left):
        self.childs[0] = left

    def setRight(self, right):
        self.childs[1] = right

    def getLeft(self, left):
        return self.childs[0]

    def getRight(self, right):
        return self.childs[1]

    def to_string(self):
        if self.childs[0] == None and self.childs[1] != None:
            return self.value + self.childs[1].to_string()
        elif self.childs[0] != None and self.childs[1] == None:
            return self.childs[0].to_string() + self.value
        elif self.childs[0] == None and self.childs[1] == None:
            return self.value
        else:
            return '(' + self.childs[0].to_string() + ')' + self.value + '(' + self.childs[1].to_string() + ')'

    def is_nullable(self):
        if self.value == '*' or self.value == '':
            return True
        elif self.value == '+':
            return self.childs[0].is_nullable() and self.childs[1].is_nullable()
        elif self.value == '|':
            return self.childs[0].is_nullable() or self.childs[1].is_nullable()
        else:
            return False

    def firstpos(self):
        if self.value == '*':
            return self.childs[0].firstpos()
        elif self.value == '+':
            if self.childs[0].is_nullable():
                return self.childs[0].firstpos().union(self.childs[1].firstpos())
            else:
                return self.childs[0].firstpos()
        elif self.value == '|':
            return self.childs[0].firstpos().union(self.childs[1].firstpos())
        else:
            return set(self.value)

    def lastpos(self):
        if self.childs[1] is None or self.childs[0] is None:
            return ''
        if self.value == '*':
            return self.childs[1].lastpos()
        elif self.value == '+':
            if self.childs[1].is_nullable():
                return self.childs[1].lastpos().union(self.childs[0].lastpos())
            else:
                return self.childs[1].lastpos()
        elif self.value == '|':
            return self.childs[1].lastpos().union(self.childs[0].lastpos())
        else:
            return set(self.value)

    