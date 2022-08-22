str = input('input : ')
# print (str)
curValue = 0
sign = []
number = []
# create stack of sign and number


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
    # print(tier)
    return tier


def compute(firstNum, operator, secondNum):
    result = 0
    match operator:
        case '+':
            # print(firstNum, 'plus')
            result = firstNum + secondNum
        case '-':
            # print(firstNum, 'plus')
            result = firstNum - secondNum
        case '*':
            # print(firstNum, 'plus')
            result = firstNum * secondNum
        case '/':
            # print(firstNum, 'plus')
            result = firstNum / secondNum
    return result


def display(curValue, curSign, index=False):
    for i in range(len(number)):
        print(number[i], sign[i], end=' ')

    print(curValue, end=' ')
    if(index):
        print(curSign, str[index+1:-1] + str[-1])


for i in range(len(str)):  # loop str
    # print (c)
    if (str[i].isnumeric()):
        curValue = curValue*10+int(str[i])
        # print(curValue)
    elif (not(str[i].isnumeric())):
        # if((len(sign) >= 1) and (len(number) >= 1)):
        while ((len(sign) >= 1) and (len(number) >= 1)):
            curTier = getTierSign(str[i])
            prevTier = getTierSign(sign[-1])  # get tier from top stack
            if(prevTier >= curTier):
                # print('prev:', prevTier, 'cur:', curTier)
                prevNumber = number.pop()
                prevSign = sign.pop()  # pop it  out
                # print(prevNumber, prevSign, curValue)
                # print(compute(prevNumber, prevSign, curValue))
                curValue = compute(prevNumber, prevSign, curValue)
                # number.append(curValue)
                # print(number, sign)
                display(curValue, str[i], i)

            else:
                break

        sign.append(str[i])
        if((str[i] != '(')):
            number.append(curValue)
            curValue = 0

    if (i == len(str)-1 and (str[i].isnumeric())):
        number.append(curValue)
        curValue = 0
    # print(number, sign)

print(number, sign)
curValue = number.pop()
while ((len(sign) >= 1) and (len(number) >= 1)):
    # curTier = getTierSign(str[i])
    # prevTier = getTierSign(sign[-1])
    # if(prevTier <= curTier):
    # print('prev:', prevTier, 'cur:', curTier)
    prevNumber = number.pop()
    prevSign = sign.pop()  # pop it  out
    # print(prevNumber, prevSign, curValue)
    # print(compute(prevNumber, prevSign, curValue))
    curValue = compute(prevNumber, prevSign, curValue)
    # number.append(curValue)
    # print(number, sign)
    display(curValue, prevSign)
    print('')

print('Result :', curValue)
# getTierSign(sign[-2])
