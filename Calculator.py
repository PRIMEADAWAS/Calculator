str = input ('input : ')
#print (str)
num=0
sign =[]
number = []
#create stack of sign and number
def tiersign(sign):
  tier=0
  if( (sign =='+')or(sign =='-')):
    tier = 1
  elif( (sign =='*')or(sign =='/')):
    tier = 2
  print(tier)
  return tier

  
for i in range(len(str)):
 #print (c)
 if (str[i].isnumeric()):
  num=num*10+int(str[i])
  #print(num)
 if (not(str[i].isnumeric())):
  # print ('plus')
  number.append(num)
  num=0
  sign.append(str[i])
 if (i==len(str)-1 and str[i].isnumeric()):
  number.append(num)
  num=0
  # print (i)
 print (i,number,sign)
print(len(sign))
tiersign(sign[-2])







