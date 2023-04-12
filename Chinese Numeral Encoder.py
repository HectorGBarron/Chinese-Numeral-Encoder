numerals = {
"-":"负",
".":"点",
0:"零",
1:"一",
2:"二",
3:"三",
4:"四",
5:"五",
6:"六",
7:"七",
8:"八",
9:"九",
10:"十",
100:"百",
1000:"千",
10000:"万"}


def splitFirstAndRemaining(n)->int:
    n=str(n)
    return  (n[0],n[1:]) 

def to_chinese_numeral(n)->str:
    print(n)
    if n==None or n==0:
        return '零'
    if n<0:
        negativeSymbol='负'
        n=n*-1
    else:
        negativeSymbol=None
        
    integer, decimal =split(n)
    integer=integerToNumeral(int(integer))
    returnValue=''
    
    #Transforming the decimals to Numeral
    if decimal!=None:
        decimal= decimalsToNumeral(decimal)
        returnValue= str(integer)+decimal
    else:
        returnValue=integer
         
    if negativeSymbol !=None:
        return negativeSymbol+returnValue
    return returnValue
    

def integerToNumeral(n)->str:    
   if type(n)==str:
       n=str(n)
   i=0
      
   
 
def split(n)->list():
    n=str(n)
    returnList=n.split('.')
    if len(returnList)==1:
        returnList.append(None)
    
    return returnList
 
def decimalsToNumeral(n)->str:
    ''''Method that receives a number and return it as a decimals in Chinese numeral'''
    if type(n)==int:
        n=str(n)   
    dot='点'
    returnStr=''.join([ numerals[int(char)] for char in n])
    return dot+returnStr


print(to_chinese_numeral(-54321))



