from functools import reduce

digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def fn(x,y):
    return x*10+y

def char2num(char):
    return digits[char]

def str2num(string):
    return reduce(fn,map(char2num,string))

result=str2num("123457839")
print(result)

    
