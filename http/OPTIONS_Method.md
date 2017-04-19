# OPTIONS Method

현재 웹서버에서 지원하는 method가 어떤 것들이 있는지 조회하는 Method.

웹서버로 `OPTIONS` Method를 사용해 요청을 보내면 다음과 같이 사용 가능한 Method를 보내준다. 

```
access-control-allow-headers:Authorization
access-control-allow-methods:HEAD, GET, POST, OPTIONS
access-control-allow-origin:*
access-control-max-age:21600
allow:HEAD, GET, POST, OPTIONS
content-length:0
content-type:text/html; charset=utf-8
date:Mon, 17 Apr 2017 01:52:06 GMT
server:nginx
status:200
```
