# python-falcon-docker
Minimal Docker image for Falcon Framework Python3 app on Alpine Linux


## How to use 

We assume your application code is in the directory `./falcon-app` and your 
*Falcon* application is the `falcon-app` object in `./falcon-app/main.py`.

```bash
.
├── Dockerfile
└── falcon-app
    └── main.py
```


Example:
```bash
docker build -t python-falcond .
docker run -it -p 3499:3499 python-falcond
```

Docker Hub Link: https://hub.docker.com/r/makseli/python-falcon-docker