# MySQL에서 FULL OUTER JOIN 하는 방법

MySQL에서는 FULL OUTER JOIN을 지원하지 않는다.
UNION으로 FULL OUTER JOIN을 흉내낼 수 있다.

```sql
(SELECT ... FROM t1 LEFT JOIN t2 ON t1.name = t2.name)
UNION
(SELECT ... FROM t2 LEFT JOIN t1 ON t1.name = t2.name)
```
