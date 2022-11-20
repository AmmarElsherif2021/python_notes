
def exampleFunction():
    x=input("Enter your num")
    y=int(x)
    print("your num is: ",y)
# exampleFunction()
# Try / except----------------------------------------------------------------------
def intAstr():
    x=input("Typen your num: \n")
    try:
        y=int(x)
    except:
        y=-1
    print(y)
# intAstr()
#break-----------------------------------------------------------------------
def exampleFun2(x):
    while x>=0:
        x+=1
        print(x)
        if x==5:
            break
        elif x==5:
            continue
        elif x<0 or x>7:
            print("error")
    return x
# exampleFun2(10)
# for  --> in-----------------------------------------------------------------
A=[1,2,3,4,5,6,7,8]
# for i in A:
    # print(i)
# print('done')
#Strings ops-----------------------------------------------------------------------------
str_op='Aaaammar'
# print(len(str_op))
def sliceStr(str):
    if len(str)>5:
        print("fun does not work")
    else:
        print(str[0:3])


    return "a" in str
def strMethods(str):
    print(dir(str))                            #all str class methods in python
    print(str.lower())
    print(str.replace('a','m',2))              #the 3rd arg is the num of what will be replaced
    print(str.rfind('a',0,5))                      #maximum index of the sub str in the range
    print('index --->\t', str.index('a', 3))
    print(str.rindex('a',0,5))                     #same as above but throws error not -1
    print(str.partition('a'))                     # split str to the 1st sep! ammar --> a,m, mar
    print(str.rpartition('a'))                     #split str to the last sep! ammar --> am, m ,ar
    print(str.rsplit())                            # split into spaces
    print(str.split(None,2))
# strMethods("Ammar's python cheat sheet")

# print(sliceStr(str_op))
#DEAL WITH FILES---------------------------------------------------------------------------------------
import os
# print (os.path.abspath(os.curdir))

# print(os.listdir(r"C:\Users\ahmed\CheatSheet\\"))

error_to_catch = getattr(__builtins__,'FileNotFoundError', IOError)
fhandle = open(r'Ammar.txt', 'r', encoding='latin-1')  # 3rd arg is the encoding mode
# print(fhandle)
# try:
#     print(fhandle.readlines())
# except error_to_catch:
#     print('!')



# print(type(fhandle.readline()))
fstr=fhandle.readlines() # it is a list
fchars=fhandle.read()    #it is a str
count=0
for line in fstr:
    count+=1

# print("count of lines: ",count)

# print('lines --->',fstr)  #prints a list

# print("lines num--->  ",len(fstr))
# print('chars ---->',len(fchars))  #prints a str
# print("words --->  ",fchars.split())
# print("str splitting --->  ",fstr)
# print("char splitting --->  ",fchars)
# print("manifest title --->  :",fstr[0])
# print("str words --->  ",fchars)
# print("file characters num --->  ",len(fchars))
fhandle.close()
#Lists-------------------------------------------------------------
fruits=['banana','apple','pinaple','orange']
fruits[0]=1 #Lists are mutable
# print(fruits)
# for i in range(5):
#     print(i)
# food=fruits+['potato','tomato','carrot']  ---------->can be concatenated
# print(food)
a=list()
a.append(1)
a.append(10)
# print(10 in a)
# print(max(a),min(a),sum(a))
# print(a)
# print(dir(a))
#DICTIONARIES----------------------------------------------------------------------
b=dict()
b['ammar']=12
b['ali']=20
b['hazem']=30
# print(b)
names=['ammar','ali','ammar','ali','ziad','fayed','zaki','yasser']
c=dict()
for name in names:
    c[name]=c.get(name,0)+1
# print(c.get('ahmed','not found')) #--------------> dict get()
# print(c.get('ammar','not found'))
# print(c)

counter=dict()
# line=input('typn your line:\n')
# words=line.split()
# for word in words:
#     counter[word]=counter.get(word,0)+1
# print(counter)
# print(list(counter))
# print(counter.keys())
# print(counter.values())
# print(counter.items())
#Tuples--------------------------------------------------------------------------------------
tuple=(1,2,3,4,5) #immutable
(x,y,z)=(1,2,3)
# print(y)
#REGEX---------------------------------------------------------------------------------------

import re


#same as ..
hand=open(r'Ammar.txt', 'r', encoding='latin-1')
i=0
# for line in hand :
#     line = line.rstrip()

#     if line.find('spectre')>0:    #----> string op.
#         print(line,'\t')
#         print(bool(re.search('spectre', line)),'----->regex found or not') #------->equivelent regex

#     if line.startswith('A spectre'): #----> string op.
#         # print(line,'\t')
#         print(bool(re.search('^A spectre',line)),'--->regex start with A spectre') #--------->eq. regex

#     if re.search('^A.*',line):
#         print('line',i,'\t --->this starts with A') #---->regex lines start with A

#     if re.search('^A\s+',line): #------> + referes to on or more, * referes to 0 or many, \s for spaces \S for non-space
#         print('line',i,'\t this line begins with A followed by a space')
#     if re.search('[0-9]+',line):
#         print('numbers in line',i, 'are:\t',re.findall('[0-9]+', line))
#     if re.search('[AEIOU]',line):
#         print('line',i,'contains A,E,I,O or U')
#         print(re.findall('[AEIOU]',line))

#     if re.search('b\S+s',line):
#          print(re.findall('b\S+?s',line))
#          print('line',i,': congrats comrade you caught the bourgeois, now send them to gulag ! ! ! ! ! ! ! ! ! ! ! !')
#     if re.search('\sin([^ ]+)',line):
#         print('line',i,' have some words starts with in... ')
#         print(re.findall('\sin(\S+)',line))
#     if re.search('\$[0-9]+',line):
#          print(re.findall('\$[0-9]+'),line) #----------->make the $ sign act normal not a regex
#     print('---------------------------------------------------')
#     i += 1

# print('i=\t',i)
# ------------------------------------------------------------------------------------------------
#Objects Oriented......................................................
class Animal:
    legs=2
    type=''
    name=''
    #constructor
    def __init__ (self,x,y,z):
        self.legs=x
        self.type=y
        self.name=z
    #get
    def get_attributes(self):
        print('name: ',self.name,'\n'
            ,  'type: ',self.type,'\n'
            ,'num of legs: ',self.legs)

    
    #deconstructor
    def __del__ (self):
        print(" died")

# alex=Animal(4,'dog','Alex')
# alex.get_attributes()
national_id=1
class Human(Animal):
    id=national_id
    type='Human'
    gender=''
    def __init__(self,x,y):
        self.name=x
        self.gender=y
        
        call1='he' if self.gender=='m' else 'she'
        call2='his' if self.gender=='m' else 'her'
        print('A human created !',call1,'is a ','male' if self.gender=='m' else 'female' ,
             'and',call2,'name is :',self.name,'>>national id:',self.id)

Ammar=Human('Ammar','m')
Aya=Human('Aya','f')

