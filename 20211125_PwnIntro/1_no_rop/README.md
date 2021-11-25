## Description
A password is required to access. Do we really need it?
## Solution
`gets` is used to read the string, it's deprecated because it doesn't check string bounds.
We can exploit this fact to overwrite the `pass` flag with a non-zero value.
