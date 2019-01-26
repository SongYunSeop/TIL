# Got permission denied while trying to connect to the Docker daemon socket...!!!

docker를 설치하고 나서 `docker` 명령어로 뭔가를 하려고 하면 다음과 같이 메세지가 나올 때가 있다.

```
$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.38/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```

지금 접속한 유저를 docker 유저 그룹에 추가해주면 된다.

```sh
$ sudo usermod -a -G docker $USER
$ sudo service docker restart
# logout and re-login
$ docker ps

# It work!
```
