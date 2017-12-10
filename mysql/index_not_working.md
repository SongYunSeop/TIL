# Index를 타지 않는 쿼리

## 인덱스 컬럼을 변형하는 경우

```sql
SELECT * FROM `table` WHERE DATE_FORMAT(`date`, '%Y%m%d') = '20171122';
```

컬럼을 바꾸기보다는 값을 바꿔주자.

```sql
SELECT * FROM `table` WHERE `date` = STR_TO_DATE('20171122', '%Y%m%d');
```

## 내부적으로 데이터 타입 전환이 이뤄지는 경우

```sql
SELECT * FROM `table` WHERE `date` = '20171122';
```

데이터 타입 전환이 이루어지면 위처럼 컬럼이 변형되는 것과 비슷한 매커니즘으로 동작한다.

```sql
SELECT * FROM `table` WHERE `date` = STR_TO_DATE('20171122', '%Y%m%d');
```

## NOT 이나 IN 연산을 사용할 경우

```sql
SELECT * FROM `table` WHERE `name` != 'yunseop';
```

```sql
SELECT * FROM `table` WHERE `name` in ('yunseop', 'song', 'yun', 'seop');
```

## LIKE 연산을 사용할 경우

```sql
SELECT * FROM `table` WHERE `name` like '%yun%';
```

## OR 조건을 사용할 경우

```sql
SELECT * FROM `table` WHERE `name` = 'yunseop' or `name` = 'song';
```
