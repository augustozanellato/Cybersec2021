## Description
How is the Josh?
## Solution
`gets` is used to read the string, it's deprecated because it doesn't check string bounds.
We can exploit this fact to overwrite the `josh` variable with the required string `H!gh`.
