# Build

```bash
docker build -t registry.insecurity-insa.fr/insecurity/python .
```

# Run

```bash
docker run -it \
           -d --restart=always \
           --name python \
           -p 2052:5000 \
           --cpu-period="100000" --cpu-quota="90000" \
           --ulimit nproc=1024:1024 \
           --ulimit fsize=10000:10000 \
           --ulimit data=1000000:1000000 \
           registry.insecurity-insa.fr/insecurity/python
docker stop python && docker rm -v python
docker exec -u 0 -it python bash
```

## Solution
* we can see the app source code
* at line 28 there's an unsafe string interpolation
* by submitting host `%s` and any valid int for port number we get back the whole `allowed` dict
## Flag
```
INSA{Y0u_C@n_H@v3_fUN_W1Th_pYth0n}
```
