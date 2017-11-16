# 실행 중인 쿼리 보기

다음 명령어로 현재 실행중인 프로세스를 확인할 수 있다.

```shell
mysql> SHOW PROCESSLIST;
+------+------+-----------------+------+---------+------+-------+------------------+
| Id   | User | Host            | db   | Command | Time | State | Info             |
+------+------+-----------------+------+---------+------+-------+------------------+
|   15 | root | localhost:50028 | udl  | Sleep   |  389 |       | NULL             |
|   16 | root | localhost:50030 | udl  | Sleep   |  389 |       | NULL             |
|   24 | root | localhost:50030 | udl  | Query   | 3123 | init  | UPDATE ..        |
|  256 | udl  | localhost       | udl  | Sleep   | 3707 |       | NULL             |
|  439 | udl  | localhost       | udl  | Sleep   |    1 |       | NULL             |
```

만약 저 중 어떤 쿼리가 데드락이 걸렸거나 너무 오래걸리는 쿼리라서 죽이고 싶을 떄는 kill 해버리면 된다.

```shell
mysql> kill 24
```


