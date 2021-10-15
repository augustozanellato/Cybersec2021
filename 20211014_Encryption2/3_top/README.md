The encryption scheme can be cracked by abusing the fact that it's XOR-based
and we know a piece of the plaintext (last ~18 bytes are all 0x88), from that
we can retrieve the encryption time which also servers as the random seed used
to generate the key.

## Plaintext
```
Here is your flag: 34C3_otp_top_pto_pot_tpo_opt_wh0_car3s
```
