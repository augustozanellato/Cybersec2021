# UE

## Description

We retrieved an important message.
However, we cannot understand the language used ...
can you help us?

The flag is in spritzCTF{} format.

## Solution

* The provided `secret.txt` looks like it's just something encoded in base64
* The decoded contents look like they're in base64 too
* After base64 decoding `secret.txt` 15 times we get the flag

## Flag

```plain
spritzCTF{ultraencoded}
```
