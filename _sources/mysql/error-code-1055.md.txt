# Error Code: 1055 

Expression #2 of SELECT list is not in GROUP BY clause ...

이런 에러가 날 때가 있다.

MySQL5.7에서 `@@sql_mode`는 `ONLY_FULL_GROUP_BY,NO_AUTO_CREATE_USER,STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION`로 기본값이 셋팅되어 있기 때문이다.

## [`ONLY_FULL_GROUP_BY`](https://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#sqlmode_only_full_group_by)
`SELECT`, `HAVING`, `ORDER BY` 목록에 있는 컬럼 중 `GROUP BY`에 없어서 집계할 수 없는 컴럼이 있다면 그 쿼리를 실행하지 않는다.

## 해결 방법

아래 쿼리로 `sql_mode`를 바꾸면 된다.

```
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
```

또는 쿼리를 수정하면 되겠지...
