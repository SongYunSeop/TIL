# INSERT 시에 중복(Duplicate) 키 에러가 난다면...

다음 쿼리를 실행했더니 에러가 난다.

```sql
mysql> INSERT INTO `user`(`email`, `name`) VALUES('dbstjq91@gmail.com', '송윤섭');
ERROR 1062 (23000): Duplicate entry 'dbstjq91@gmail.com' for key 'user_email_unique'
```

이유는 `user` 테이블에 `email` 필드가 `UNIQUE INDEX`로 걸려있기 때문이다.

이럴 때는 3가지 옵션이 있다.

## 1. INSERT IGNORE

```sql
mysql> INSERT IGNORE INTO `user`(`email`, `name`) VALUES('dbstjq91@gmail.com', '송윤섭');
Query OK, 0 rows affected (0.00 sec)
```

만약 중복이 발생한다면 지금 삽입하려는 ROW를 무시한다.

결국 원래의 ROW만 남는다.

## 2. REPLACE INTO

```sql
mysql> REPLACE INTO `user`(`email`, `name`) VALUES('dbstjq91@gmail.com', '송윤섭');
Query OK, 2 rows affected (0.00 sec)
```
 
`INSERT INTO ...` 형태의 쿼리를 `REPLACE INTO ... `로 바꿔서 사용하면되는데

이 때 기존의 ROW는 삭제되고 지금 실행하는 ROW가 삽입된다.(이 때문에 `2 rows affected` 가 나온다.)

따라서 Primary Key로 Auto Increment 옵션을 사용하고 있다면 값이 증가된 ROW가 남는다.

## 3. ON DUPLICATE KEY UPDATE

```sql
INSERT INTO `user`(`email`, `name`) VALUES('dbstjq91@gmail.com', '송윤섭1')
    ON DUPLICATE KEY UPDATE `name`=VALUES(`name`);
Query OK, 2 rows affected (0.01 sec)
```

말 그대로 DEPLICATE KEY일 때는 UPDATE를 하라는 쿼리이다.

UPDATE할 필드를 지정할 수 있다.

원래의 ROW에 해당 필드만 UPDATE하기 때문에 Auto Increment 값은 변하지 않는다.
