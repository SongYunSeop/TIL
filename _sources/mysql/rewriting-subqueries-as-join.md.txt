# Subquery는 Join으로 바꿉시다!

서브 쿼리를 사용해 필터링을 하는 경우가 있는데, 이는 성능저하를 야기한다.
LEFT [OUTER] JOIN은 서브쿼리 보다 Optimizer가 더 최적화 하기 쉬워서 빠를 수 있다.

## Examples

```sql
SELECT * FROM t1 WHERE id IN (SELECT id FROM t2);
```

위 쿼리는 다음과 같이 바꿀 수 있다.

```sql
SELECT DISTINCT t1.* FROM t1, t2 WHERE t1.id=t2.id;
```

---

```sql
SELECT * FROM t1 WHERE id NOT IN (SELECT id FROM t2);
SELECT * FROM t1 WHERE NOT EXISTS (SELECT id FROM t2 WHERE t1.id=t2.id);
```

위 쿼리는 다음과 같이 바꿀 수 있다.

```sql
SELECT table1.*
FROM table1 LEFT JOIN table2 ON table1.id=table2.id
WHERE table2.id IS NULL;
```

## Refer
- [13.2.10.11 Rewriting Subqueries as Joins](https://dev.mysql.com/doc/refman/5.7/en/rewriting-subqueries.html)
