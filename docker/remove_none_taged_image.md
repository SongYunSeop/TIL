# <none> Tag Image 지우기

```sh
$ docker rmi $(docker images | grep '^<none>' | awk '{print $3}')
```
