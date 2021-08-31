#1.Write a Python script to count number of identical chars in a given string with same special case handling,
#and return the number with highest count, eg: given string 'coffee tuffee',should returns 4.
'''
s=input('enter a string')
c=0

for i in s:
    if(s.count(i)>1):
        if s[i]==s[i+1]:
            c=c+1
print(c)

'''









####################################################################################################

#2.Write a program that accepts sequence of lines as input and prints the lines after making all characters
#in the sentence capitalized. Suppose the following input is supplied to the program.
#Hello world Practice makes perfect
#Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

'''
a=input('enter a sequence of line')
print(a.upper())

'''


####################################################################################################

#3.Write a program to determine whether an input string x is a substring of another input string y.
#(For example, "bat" is a substring of "abate" but not of "beat".)??

'''
y=input('enter y string')
x=input('enter x string')

if x in y:
    print('it is part of substring')
else:
    print('it is not a part of substring')
    
'''







####################################################################################################


#4.write a Python program to get a string from a given string where all occurrence of its first char
#have been changed to $, except the first char itself.
#eg:-'restart'
#Expected Result:-'resta$t'
'''
a=input('enter a integer')
print(a[0]+a[1:len(a)].replace(a[0],'$'))
'''
'''
a='rahul'
b=print(a[0])
print(b)
c=a[1:len(a)]
print(c)
d=c.replace(c[0],'$')
print(d)

'''





####################################################################################################

#5.Remove white spaces from the string SN="aaa bbb ccc ddd eee FFF JJJ KKK LLL"
'''
a=input('enter a string')
b=a.replace(' ','')
print(b)

'''





####################################################################################################

#6.Give a string,return a new string where the first and last chars have been exchanged.
'''
a=input('enter a string')
b=a[1:-1]
c=a[0]
d=a[-1]
print(d+b+c)

'''

'''
a=input('enter a string')
b=a[0].replace(a[0],a[-1],1)
c=a[1:(len(a)-1)]
d=a[-1].replace(a[-1],a[0],1)
print(b+c+d)

'''



####################################################################################################

#7.give a string,we'll say that the front is the first 3 chars of the string.if the string length is less
#than 3,the front is whatever is there.Return a new string which is 3 copies of front.
#eg:java o/p:-javjavjav ,eg:chocolate o/p:-chochocho
'''
a=input('enter a string')

if(len(a)>=3):
    print(3*(a[0:3]))
else:
    print(a)

'''
 
####################################################################################################

#8.give two strings a and b,return the result of putting them together in the order
#eg:'Hi' and 'Bye' returns 'HiByeByeHi'.

'''
a=input('enter a string')
b=input('enter a string')
c=a+2*b+a
print(c)

'''

#9.write a program to find the number of vowels,consonents,digits and white spaces charcters in a string.
'''
a=input('enter a string')
b=0
d=0
c=0
e=0
for i in a:
    if i in 'aeiouAEiou':
        b=b+1
    elif i.isspace():
        d=d+1
    elif i.isdigit():
        e=e+1
    elif i not in 'AEIOUaeiou':
        c=c+1
print(b)
print(c)
print(d)    
print(e)   

'''



    
#10.write a programm to make a new string with all the consonents deleted from the string
# "HELLO have a good day"
'''
a=input('enter a string')

for i in a:
    if i not in 'aeiouAEIOU':
        
        print(i.replace(' ',''),end='')

'''
#11. write a programm that takes your full name as input as input and displays the abbreviations
#of the first and middle names except the last name which is displayed as it is.
#for example,if your name is Robert Brett Roser,then output:-should be R.B.Roser
'''
a=input('enter a string')
b=a.split()
print("{}.{}.{}".format(b[0][0],b[1][0],b[2]))
'''






