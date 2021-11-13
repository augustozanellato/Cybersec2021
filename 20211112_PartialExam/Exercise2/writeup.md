# Second exercise

## Challenge description

In this game, you can already see the flag.
The question is: how to get there? You need to provide two inputs that allow you to reach it.

Your final solution can be a text file, where you explain your trials/reasonings and the inputs you used to reach the flag.

## Rules

- You cannot use online tools for solving the challenge automatically
- You can modify the python code we provide you as you desire … however: the solutions you provide us must work with the original python code.

## Writeup

The first level checks if the sum of the ascii values of the two characters around an `a` is > 180.
It looks like the input `zaz` satisfies this condition.
The second level is a little bit trickier, it changes the third letter of the input with the letter that's two letter before it in the alphabet and then it removes `RI` from the string.
The first step of the second level is passed with the input `SPPITZ`
The second step can be passed by exploiting the fact that `str.replace` in python doesn't recursively replace stuff using the input `SPPRIITZ`

## Flag

`SPRITZCTF={webgame2020_03}`
