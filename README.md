# Calculator

for my Msc python homework

## Algorythm

input equation in string type

check error syntax in string and string modification
Ex: Error
1/0.-1 throw float error
)( close parenthesis before open
((()) non complete pair of parenthesis

EX: String modification
.1--1+1+(12)(12)(12.123)+-2-2*-(-2+3-2)-1/0.1+1/.1+1/.1+1/-11(12)+3(12)3*-12--12+1/-11.1+.1
fill .1 -> 0.1
insert multiply between (12)(12)(12.123) and 3(12)3

separate string by reg ex split it into list

get list data and loop check list one by one

first check it was number or not

and put number to stack, operator to sign

then check symbol and give it a tier number

compare with previous sign in stack

and De-tier that equation

find first close parenthesis and clear or simplify it to number

finally you get a simply equation with out any tier order problem and solve the last one
