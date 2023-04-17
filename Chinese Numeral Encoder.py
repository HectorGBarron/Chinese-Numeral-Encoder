def to_chinese_numeral(n)->str:
    print(n)
    if n==None or n==0:
        return '零'
    negativeSymbol=None

    if n<0:
        negativeSymbol='负'
        n=n*-1
            
    integer, decimal =split(n)
    integer=integerToNumeral(integer)
    returnValue=''
    
    #Transforming the decimals to Numeral
    if decimal!=None:
        decimal= decimalsToNumeral(decimal)
        returnValue= integer+decimal
    else:
        returnValue=integer
         
    if negativeSymbol !=None:
        return negativeSymbol+returnValue
    return returnValue

numeralsKeys = {
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
positionKeys={2:10,3:100,4:1000,5:10000}    
 
def numerals(x, pos=0):
    if type(x)==str:
        x=int(x)
    
    
    if pos<=1:
        return numeralsKeys[x]    
        
    return numerals(x)+ numerals(positionKeys[pos])
        
def integerToNumeral(n)->str:
   ''''This method receive a number either as a string type or an int type
       It generates a list ot tuples breaking down the number an its position
       **Note the list is in reverse order such as the first digit has the first position***
   '''     
   if type(n)==str:
       n=int(n)
   if n==0:
       return numerals(n)
   
   if n<=10:
       return numerals(n,1)
   if n<=19:
       
       return numerals(10,1) + numerals(n-10,1)
   
   n=str(n) 
   numbersBreakDown=[(pos,int(val) )for pos, val in  enumerate(list( num for num  in n)[::-1],start=1)]   
   listWithoutTrailingZeros= [number for number in numbersBreakDown if not(number[1]==0 and number[0]>0)]
   returnValue=''
   for element in listWithoutTrailingZeros[::-1]:
       returnValue=returnValue+numerals(element[1],element[0])        
   return returnValue

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
    if len(n)>1:
        returnStr=''
        for element in [char for char  in n]:
            returnStr=returnStr+numerals(element)
            
    else:
        returnStr=numerals(int(n))
    return dot+returnStr


print (to_chinese_numeral(9))