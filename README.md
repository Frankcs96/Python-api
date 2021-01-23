# RUN PROJECT WITHOUT DOCKER

1. Install dependencies
```console
pip install fastapi uvicorn
```
2. Run the server on localhost
```console
uvicorn app.main:app --reload

```

# BUILD AND RUN DOCKER IMAGE

1. for building the image use the following command
```console
docker build -t [YOUR_IMAGE_NAME] .
```

2. for running the docker image use the following command
```console
docker run -p 15500:15500 --name [CUSTOM_NAME] [YOUR_IMAGE_NAME]
```

the api will be up and running on localhost port 15500
