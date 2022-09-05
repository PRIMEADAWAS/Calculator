from asyncio.windows_events import NULL
import re

# str = '(1)(2)(1.1)+1(2)3+0.-1'
# str = '.1--1+1+(12)(12)(12.123)+-2-2*-(-2+3-2)-1/0.1+1/.1+1/.1+1/-11(12)+3(12)3*-12--12+1/-11.1+.1'
str = input('Input Equation :')

curValue = 0
IsParenthesisSyntaxError = False
IsSyntaxError = False

# create stack of sign and number
sign = []  # OperatorList
number = []  # numberList

# regexList
regNum = '\d+'
regFloat = '\d+\.\d+'
regSign = '[+-/*()]'

errorDivideZero = 'Error found can not divine by zero value'


def strToEquationList(str):
    regCombine = regFloat + '|' + regSign + '|' + regNum
    return re.findall(regCombine, str)


def floatIntCheck(checkVal):
    value = 0
    if(bool(re.search(regFloat, checkVal))):
        value = float(checkVal)
    elif(bool(re.search(regNum, checkVal))):
        value = int(checkVal)
    return value


def parenSyntaxCheck(str):
    IsError = False
    # check syntax equationList
    parCheck = 0  # parenthesis check by count

    for i in range(len(str)):
        # parenthesis check
        if(str[i] == '('):
            parCheck += 1
        if(str[i] == ')'):
            parCheck -= 1
        if(parCheck < 0):
            IsError = True
            break

    # parCheck and IsError after complete loop
    if(parCheck != 0 or IsError):
        IsError = True
        print("Wrong syntax of parenthesis ()")
    return IsError


def insertStr(strOriginal, strInsert, index):
    return strOriginal[:index]+strInsert+strOriginal[index:]


def syntaxModifier(str):
    if(str[0] != '-'):
        str = '0+'+str
    # CASE I : [')(', '1(2)', '(2))3'] Ex (1)(2)(3)  1(2)3
    # just insert * between (1)*(2)*(3)  1*(2)*3
    if(re.findall('\)\(', str)):
        # use revere loop due to prevent index shift by insertion
        for defect in reversed(list(re.finditer('\)\(', str))):
            str = insertStr(str, '*', defect.start()+1)
    if(re.findall('\d\(', str)):
        for defect in reversed(list(re.finditer('\d\(', str))):
            str = insertStr(str, '*', defect.start()+1)
    if(re.findall('\)\d', str)):
        for defect in reversed(list(re.finditer('\)\d', str))):
            str = insertStr(str, '*', defect.start()+1)
    # CASE II : ['+-2', '(-2', ')-1', '.-1', '/-1', '*-1', '--1']
    # easy insert 0 ['+-(2'] +0-(2 -0-(2
    if(re.findall('[-+]\-\(', str)):
        for defect in reversed(list(re.finditer('[-+]\-\(', str))):
            str = insertStr(str, '0', defect.start()+1)
    # easy insert 0 ['+-2', '(-2'] +0-2 (0-2
    if(re.findall('[(+]\-\d', str)):
        for defect in reversed(list(re.finditer('[(+]\-\d', str))):
            str = insertStr(str, '0', defect.start()+1)
    # change -- to +
    if(re.findall('\-\-\d', str)):
        for defect in reversed(list(re.finditer('\-\-\d', str))):
            index = defect.start()+1
            symbol = '+'
            # check starting index
            if(index == 1):
                symbol = ''
            str = str[:index-1]+symbol+str[index+1:]

    # insert 0 between +-*/(.1 -> +-*(0.1
    if(re.findall('\D\.\d+', str)):
        for defect in reversed(list(re.finditer('\D\.\d+', str))):
            str = insertStr(str, '0', defect.start()+1)
    # start with .1
    # if(re.findall('^\.\d+', str)):
    #     for defect in reversed(list(re.finditer('^\.\d+', str))):
    #         str = insertStr(str, '0', defect.start())

    # /*-1.1
    if(re.findall('[/*]\-\d+\.\d+', str)):
        for defect in reversed(list(re.finditer('[/*]\-\d+\.\d+', str))):
            str = insertStr(str, ')', defect.end())
            str = insertStr(str, '(0', defect.start()+1)
    # /*-1
    if(re.findall('[/*]\-\d+', str)):
        for defect in reversed(list(re.finditer('[/*]\-\d+', str))):
            str = insertStr(str, ')', defect.end())
            str = insertStr(str, '(0', defect.start()+1)

    # start with -(
    # if(re.findall('^\-\(', str)):
    #     for defect in reversed(list(re.finditer('^\-\(', str))):
    #         str = insertStr(str, '1)*', defect.end()-1)
    #         str = insertStr(str, '(0', defect.start())

    # *-(
    if(re.findall('[*/]\-\(', str)):
        for defect in reversed(list(re.finditer('[*/]\-\(', str))):
            str = insertStr(str, '1)*', defect.end()-1)
            str = insertStr(str, '(0', defect.start()+1)

    return str


def getTierSign(sign):
    tier = 0
    if((sign == '+') or (sign == '-')):
        tier = 1
    elif((sign == '*') or (sign == '/')):
        tier = 2
    # elif((sign == '^') or (sign == 'sqrt')):
    #     tier = 4
    elif((sign == '(') or (sign == ')')):
        tier = 5
    return tier


def compute(firstNum, operator, secondNum):
    result = 0
    # check divine by zero value
    if(firstNum == errorDivideZero or secondNum == errorDivideZero):
        return errorDivideZero

    match operator:
        case '+':
            result = firstNum + secondNum
        case '-':
            result = firstNum - secondNum
        case '*':
            result = firstNum * secondNum
        case '/':
            if(secondNum == 0):
                return errorDivideZero
            result = firstNum / secondNum

    return result


def clearParenthesis(curValue):
    while ((len(sign) >= 1) and (len(number) >= 1)):
        prevSign = sign.pop()
        if((prevSign == '(')):
            break
        prevNumber = number.pop()
        curValue = compute(prevNumber, prevSign, curValue)
    # prevent bug error from len number = 0 but sign = 1 and have '('
    if(len(sign) >= 1):
        if(sign[-1] == '('):
            sign.pop()
    return curValue


# use regex to converse str to equationList

if(re.findall('\(\)', str)):
    IsParenthesisSyntaxError = True
    print("Wrong syntax of parenthesis ()")
if(re.findall('\.\-\d', str)):
    IsSyntaxError = True
    print("Wrong syntax of float number")


str = syntaxModifier(str)
equationList = strToEquationList(str)

if(IsParenthesisSyntaxError == False):
    IsParenthesisSyntaxError = parenSyntaxCheck(equationList)

if(IsParenthesisSyntaxError == False and IsSyntaxError == False):
    for i in range(len(equationList)):  # loop equationList
        isAppend = False
        # equationList[i][0].isnumeric()
        if (bool(re.search(regNum, equationList[i]))):
            curValue = floatIntCheck(equationList[i])
        # not(equationList[i][0].isnumeric())
        elif (bool(re.search(regSign, equationList[i]))):
            if((equationList[i] == ')')):
                if(equationList[i-1] == ')'):  # prevent (1+(1+1))
                    curValue = number.pop()
                curValue = clearParenthesis(curValue)
                isAppend = True

            while ((len(sign) >= 1) and (len(number) >= 1)):
                curTier = getTierSign(equationList[i])
                prevTier = getTierSign(sign[-1])  # get tier from top stack
                if((prevTier >= curTier) and (prevTier != 5)):
                    if(curValue == 'null'):  # prevent (1*2)+(1*3)+1
                        curValue = number.pop()
                    prevNumber = number.pop()
                    prevSign = sign.pop()  # pop it  out
                    curValue = compute(prevNumber, prevSign, curValue)
                    isAppend = True

                else:
                    break
            if(equationList[i] != ')'):
                sign.append(equationList[i])
            # prevent +( and  )+ append 0 [((equationList[i-1] and (equationList[i-1] != ')')) or len(number) == 0)]
            if(isAppend or ((equationList[i] != '(') and (bool(re.search(regNum, equationList[i-1]))))):
                number.append(curValue)
                curValue = 'null'
                isAppend = False

        if(curValue == errorDivideZero):
            print(curValue)
            break
        if (i == len(equationList)-1 and (bool(re.search(regNum, equationList[i])))):
            number.append(curValue)
            curValue = 'null'
    # after De-tier equation
    curValue = number.pop()

    # clear simple equation
    while ((len(sign) >= 1) and (len(number) >= 1)):
        prevNumber = number.pop()
        prevSign = sign.pop()  # pop it  out
        if((prevSign == '(') or (prevSign == ')')):
            prevSign = sign.pop()
        curValue = compute(prevNumber, prevSign, curValue)

    number.append(curValue)
    print('[Result :', number[0], "]")
