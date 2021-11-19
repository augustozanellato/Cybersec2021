break *0x0040090f
run
printf "%s", (char**)flag_buf
