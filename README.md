## How to use (macOS)
- First you need to install XQuartz `brew install --cask xquartz`
- Launch XQuartz `xquartz`
- Run `xhost + ${YOUR_IP}`

### Run the project with docker compose
- Get your ip and replace it in the `.env` file
```
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
```

- Run with docker compose
```shell
docker compose run --build python ${PATH_TO_FILE}
``` 
(PATH_TO_FILE can be a URL or the name of a file located at the root of the project).

### Run the project with docker
```shell
docker run --rm -v $(pwd):/tmp -w /tmp -e DISPLAY="$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}'):0" ghcr.io/te4g/opencv-docker-gui ${PATH_TO_FILE} (can be a URL)
```
