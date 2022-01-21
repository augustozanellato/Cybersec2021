# BB

## Description

We retrieved an important message.
However, we cannot understand the language used ...
can you help us?

In the writeup, explain carefully why and how we can break the algorithm.

The flag is in spritzCTF{} format.

## Solution

* `message.txt` looks again like random garbage so it's probably another XOR-based challenge.
* The provided `students.py` confirms our idea.
* It's just some fancy XOR-based algorithm using numpy.
* The `mixer` function uses the `key` argument as a seed for numpy's rng.
* We can exploit the fact that we know the flag format to automatically bruteforce the key.
* One issue with the keygen is that it's output is theoretically unbounded because `np.random.randn` generates random number using a standard normal disribution. Generally the output is between -3 and 3 but nothing guarantees that it's actually in that range. In fact there's a 0.26% probability that the used key is outside that.
* The `keygen` function uses `np.abs` on the `randn` output so it effectively halves our search space.
* By trying all the integers between 0 and 3500 we should be able to find the key if we are lucky (or maybe if we aren't unlucky)
* The key came out to be `107`

## Flag

```plain
spritzCTF{blusky}
```
