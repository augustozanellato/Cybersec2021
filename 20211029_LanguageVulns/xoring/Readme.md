# Build

```bash
docker build -t registry.insecurity-insa.fr/insecurity/xoring .
```

# Run

```bash
docker run -it \
           -d --restart=always \
           --name xoring \
           -p 2052:8081 \
           --cpu-period="100000" --cpu-quota="90000" \
           --ulimit nproc=1024:1024 \
           --ulimit fsize=10000:10000 \
           --ulimit data=1000000:1000000 \
           registry.insecurity-insa.fr/insecurity/xoring
docker stop xoring && docker rm -v xoring
docker exec -u 0 -it xoring bash
```

## Solution
* the challenge is ultimately just reversing some obfuscated js
* the js (see `script_deobfuscate.js` in this directory) is ultimately just some xoring (as the challenge name implies)
* by calling `x("_NeAM+bh_saaES_mFlSYYu}nYw}", "6")` we get back the original plaintext which is the flag

## Flag
```
iNSA{+ThisWasSimpleYouKnow+}
```
