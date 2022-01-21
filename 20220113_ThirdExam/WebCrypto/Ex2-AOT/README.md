# AOT

## Description

We retrieved an important message.
However, we cannot understand the language used ...
can you help us?

The flag is in spritzCTF{} format.

## Solution

* The input looks like random data, probably there's some XOR-based encryption involved
* After checking `students.py` we can confirm our idea, it's just some basic XOR encryption with some other code around to confuse us.
* In the `mixer` function only `message` and `x1` are actually used for encryption purposes, `x2` and `x3` are there just to waste our time.
* Due to the fact that the input is being XORed with text we can assume that `x1` is between 0 and 127; using this assumption we can decrease the search space for our bruteforce attempt.
* `mixer` uses some asserts to check for the validity of `x1`, `x2` and `x3`.
* Specifically `x1 % 731` must be equal to `(x2 + x3) % 731`, none of `x1`, `x2` and `x3` can be equal to one another and finally `x1` must be different to `x2 + x3`
* We know that `x1 < 731` so we can just make `x2` to be `x + 731` and `x3` to be `731 * 2` so that `f(x1)` is always equal to `x1`, `f(x2)` is always equal to `x1` and `x3` is always `0` so `f(x1 + x2)` is equal to `x1`.
* While bruteforcing we can exploit the fact that we know part of the ciphertext because the flag format is known; if during bruteforce we find a string that contains `spritzCTF{` we know that we got the flag

## Flag

```plain
spritzCTF{sasageyo}
```
