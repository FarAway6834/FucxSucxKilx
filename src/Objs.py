#나머지 부분은 다 씨* 장식이기 때문에 요건 윈도용으로 씨* 존*대충 가능하다는거 보이는거다.

def __invert__(self):
    return self.format('mersen') - self

def __and__(self, x):
    return sum([(self[i]*x[i])<<i for i in range(self.format('bit', x))])

def __or__(self, x):
    return sum([(self[i]+x[i]-(self[i]*x[i]))<<i for i in range(self.format('bit', x))])

def __xor__(self, x):
    return sum([(self[i]+x[i]-(2*(self[i]*x[i])))<<i for i in range(self.format('bit', x))])

def __lshift__(self, x):
    return (2**x)*self - (2**self.format('bit'))*(self//(2**(self.format('bit') - x)))

def __rshift__(self, x):
    return self // (2 ** x)

def __getitmem__(self, x): #기분나빠서 lsb유사 시스템 가정 ㅋㅋㅋ
    return (self<<x)>>self.format('bit') #슬라이스 미룸
