# MySQL에서 localhost != 127.0.0.1

MySQL Client는 mysqld 서버로 접속할 떄 2가지 방법이 있다.

Unix socket file을 사용하는 방법과 TCP/IP 를 사용하는 방법이 있다.

보통 `localhost`나 `host`를 지정하지 않는다면 기본적으로 Unix Socker File을 사용해서 연결을 시도한다.

그래서 Dockerize된 MySQL에 접속하려고 할때 host를 따로 입력하지 않거나 `localhost` 라고 명시하면 접속하지 못할 수 있다.

다음과 같이 `127.0.0.1` 로 접속을 시도해야한다.

```
mysql -h 127.0.0.1
```

## Refer 

- [https://dev.mysql.com/doc/refman/5.5/en/can-not-connect-to-server.html](https://dev.mysql.com/doc/refman/5.5/en/can-not-connect-to-server.html)
