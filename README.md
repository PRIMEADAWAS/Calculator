# Calculator

for my Msc python homework

## Algorythm

- Input equation in string type

> Check error syntax in string and string modification
> Ex: Error
> 1/0.-1 throw float error
> )( close parenthesis before open
> ((()) non complete pair of parenthesis

> EX: String modification
> .1--1+1+(12)(12)(12.123)+-2-2*-(-2+3-2)-1/0.1+1/.1+1/.1+1/-11(12)+3(12)3*-12--12+1/-11.1+.1
> Fill .1 -> 0.1
> Insert multiply between (12)(12)(12.123) and 3(12)3
> String syntaxModifier: 0+0.1+1+1+(12)_(12)_(12.123)+0-2-2*(0-1)*(0-2+3-2)-1/0.1+1/0.1+1/(0-11)_(12)+3_(12)_3_(0-12)+12+1/(0-11.1)+0.1

> Separate string by reg ex split it into list
> ['0', '+', '0.1', '+', '1', '+', '1', '+', '(', '12', ')', '*', '(', '12', ')', '*', '(', '12.123', ')', '+', '0', '-', '2', '-', '2', '*', '(', '0', '-', '1', ')', '*', '(', '0', '-', '2', '+', '3', '-', '2', ')', '-', '1', '/', '0.1', '+', '1', '/', '0.1', '+', '1', '/', '(', '0', '-', '11', ')', '*', '(', '12', ')', '+', '3', '*', '(', '12', ')', '*', '3', '*', '(', '0', '-', '12', ')', '+', '12', '+', '1', '/', '(', '0', '-', '11.1', ')', '+', '0.1']

- Get list data and loop check list one by one

- First check it was number or not

- Then put number to stack, operator to sign

- Then check symbol and give it a tier number

- Compare with previous sign in stack

- And De-tier that equation to simple equation

- Find first close parenthesis and clear or simplify it to number

- Finally you get a simply equation with out any tier order problem and solve the last one
