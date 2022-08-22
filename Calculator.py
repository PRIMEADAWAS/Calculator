str = input('input : ')
# print (str)
curValue = 0
# create stack of sign and number
sign = []
number = []


def getTierSign(sign):
    tier = 0
    if((sign == '+') or (sign == '-')):
        tier = 1
    elif((sign == '*') or (sign == '/')):
        tier = 2
    elif((sign == '^') or (sign == 'sqrt')):
        tier = 4
    elif((sign == '(') or (sign == ')')):
        tier = 5
    return tier


def compute(firstNum, operator, secondNum):
    result = 0
    match operator:
        case '+':
            result = firstNum + secondNum
        case '-':
            result = firstNum - secondNum
        case '*':
            result = firstNum * secondNum
        case '/':
            result = firstNum / secondNum
    return result


def display(curValue, curSign, index=False):
    for i in range(len(number)):
        print(number[i], sign[i], end=' ')

    print(curValue, end=' ')
    if(index):
        print(curSign, str[index+1:-1] + str[-1])


def clearParenthesis(curValue):
    while ((len(sign) >= 1) and (len(number) >= 1)):
        prevSign = sign.pop()
        if((prevSign == '(')):
            print('already pop ( out')
            break
        prevNumber = number.pop()
        print(prevNumber, prevSign, curValue)
        print('compute', compute(prevNumber, prevSign, curValue))
        curValue = compute(prevNumber, prevSign, curValue)
        print('clearParenthesis', number, sign)
        # display(curValue, prevSign)
        print('')
    if(len(sign) >= 0):
        if(sign[-1] == '('):
            print('clear (')
            sign.pop()
    return curValue


for i in range(len(str)):  # loop str
    # print (c)
    if (str[i].isnumeric()):
        curValue = curValue*10+int(str[i])
        # print(curValue)
    elif (not(str[i].isnumeric())):
        # if((len(sign) >= 1) and (len(number) >= 1)):
        if((str[i] == ')')):
            print('find )')
            if(str[i-1] == ')'):  # prevent (1+(1+1))
                curValue = number.pop()
            curValue = clearParenthesis(curValue)

        while ((len(sign) >= 1) and (len(number) >= 1)):
            curTier = getTierSign(str[i])
            prevTier = getTierSign(sign[-1])  # get tier from top stack
            if((prevTier >= curTier) and (prevTier != 5)):
                print('prev:', prevTier, 'cur:', curTier)
                if(str[i-1] == ')'):  # prevent (1*2)+(1*3)+1
                    curValue = number.pop()
                prevNumber = number.pop()
                prevSign = sign.pop()  # pop it  out
                print(prevNumber, prevSign, curValue)
                print(compute(prevNumber, prevSign, curValue))
                curValue = compute(prevNumber, prevSign, curValue)
                # number.append(curValue)
                print(number, sign)
                # display(curValue, str[i], i)

            else:
                break
        if(str[i] != ')'):
            print('append ', str[i])
            sign.append(str[i])
        # prevent +( and  )+ append 0
        if((str[i] != '(') and ((str[i-1] != ')')) or len(number) == 0):
            print('append ', curValue)
            number.append(curValue)
            curValue = 0

    if (i == len(str)-1 and (str[i].isnumeric())):
        number.append(curValue)
        curValue = 0
    print(number, sign)

print('Simplify', number, sign)
curValue = number.pop()
while ((len(sign) >= 1) and (len(number) >= 1)):
    # curTier = getTierSign(str[i])
    # prevTier = getTierSign(sign[-1])
    # if(prevTier <= curTier):
    # print('prev:', prevTier, 'cur:', curTier)
    prevNumber = number.pop()
    prevSign = sign.pop()  # pop it  out
    if((prevSign == '(') or (prevSign == ')')):
        prevSign = sign.pop()
    print(prevNumber, prevSign, curValue)
    print(compute(prevNumber, prevSign, curValue))
    curValue = compute(prevNumber, prevSign, curValue)
    # number.append(curValue)
    # print(number, sign)
    display(curValue, prevSign)
    print('')
number.append(curValue)
print('[Result :', number[0], "]")
# getTierSign(sign[-2])
