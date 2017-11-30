# GROUP BY 최적화

GROUP BY 절을 보통 테이블을 스캔하고 결과를 임시 테이블에 넣어서 집계하는 과정을 거친다. 그래서 데이터 양에 따라서 매우매우 느린 쿼리가 될 수도 있다. 그래도 인덱스를 잘 설정한다면 임시 테이블을 생성하지 않고 빠르게 데이터를 가져올 수 있다.

관건은 GROUP BY 에 있는 모든 컬럼들이 바라보는 Index가 동일하고 순서도 맞아야 한다.

두가지 방법이 있는데

1. The grouping operation is applied together with all range predicates (if any)
2. 범위 스캔 후 결과를 집계하는 방법(First performs a range scan, and then groups the resulting tuples)

MySQL에서 GROUP BY는 Sorting을 위해 사용되는데 ORDER BY 를 최적화 할 수도 있다.

## Loose Index Scan

- Query는 하나의 테이블에서 동작한다.

- GROUP BY 는 인덱스의 컬럼의 가장 왼쪽부터 지정한다.
    에를 들면 `t1` 테이블에 인덱스가 `(c1, c2, c3)` 이렇게 3 개의 컬럼으로 지정되어 있다면
    `GROUP BY c1, c2`는 Loose Index Scan이 되지만, `GROUP BY c2, c3` 이나 `GROUP BY c1, c2, c4`는 사용할 수 없다.

- SELECT 절에서 `MIN()`, `MAX()` 를 제외하고 다른 집계함수는 사용할 수 없음. 그리고 그 컬럼은 인덱스 안에 들어가 있어야함.

- SELECT 절에서 `MIN()`, `MAX()` 를 제외하고 다른 컬럼들은 상수여야만함.

- For columns in the index, full column values must be indexed, not just a prefix. For example, with c1 VARCHAR(20), INDEX (c1(10)), the index cannot be used for loose index scan.

만약 Loose Index Scan이 사용된다면 `EXPLAIN`의 결과로 `Extra` 컬럼에  `Using index for group-by` 를 볼 수 있다.

테이블 t1(c1, c2, c3, c4) 에 (c1, c2, c3)으로 인덱스가 걸려있다면 다음 쿼리에서 Loose Index Scan이 된다.

```sql
SELECT c1, c2 FROM t1 GROUP BY c1, c2;
SELECT DISTINCT c1, c2 FROM t1;
SELECT c1, MIN(c2) FROM t1 GROUP BY c1;
SELECT c1, c2 FROM t1 WHERE c1 < const GROUP BY c1, c2;
SELECT MAX(c3), MIN(c3), c1, c2 FROM t1 WHERE c2 > const GROUP BY c1, c2;
SELECT c2 FROM t1 WHERE c1 < const GROUP BY c1, c2;
SELECT c1, c2 FROM t1 WHERE c3 = const GROUP BY c1, c2;
```

하지만 다음 쿼리는 만족하지 못하는 경우다.

- `MIN()`, `MAX()` 가 아닌 다른 집계 함수가 들어가 있는 경우:

```sql
SELECT c1, SUM(c2) FROM t1 GROUP BY c1;
```

- Group by 요소 중 맨 왼쪽의 요소가 들어가있지 않은 경우:

```sql
SELECT c1, c2 FROM t1 GROUP BY c2, c3;
```

- Group By 부분에 컬럼들이 충분하지 않을 때:

```sql
SELECT c1, c3 FROM t1 GROUP BY c1, c2;
```

`WHERE c3 = 'c3'` 구문을 추가하면 Loose Index Scan을 사용할 수 있다.

Loose Index Scan은 `MIN()`, `MAX()`가 아닌 다른 형태의 집계 함수에도 사용가능하게 지원한다.

- `AVG(DISTINCT)`, `SUM(DISTINCT)`, `COUNT(DISTINCT)`가 지원된다. `AVG(DISTINCT)`, `SUM(DISTINCT)`는 하나의 인자를 받고, `COUNT(DISTINCT)`는 두개 이상의 인자를 받는다.

- GROUP BY, DISTINCT 절이 없어야 한다.

- 앞에서 설명한 Loose Index Scan의 제한사항이 여전히 적용된다.

다음 쿼리는 Loose Index Scan을 사용할 수 있다.

```sql
SELECT COUNT(DISTINCT c1), SUM(DISTINCT c1) FROM t1;
SELECT COUNT(DISTINCT c1, c2), COUNT(DISTINCT c2, c1) FROM t1;
```

## Tight Index Scan

Tight Index Scan은 쿼리의 상태에 따라 Full Index Scan이 이루어질지 Range Index Scan이 이루어질지 결정된다.

다음 쿼리는 Loose Index Scan으로는 되지 않지만 Tight Index Scan으로 되는 쿼리다.

```sql
SELECT c1, c2, c3 FROM t1 WHERE c2 = 'a' GROUP BY c1, c3;
SELECT c1, c2, c3 FROM t1 WHERE c1 = 'a' GROUP BY c2, c3;
```

## Refer
- https://dev.mysql.com/doc/refman/5.7/en/group-by-optimization.html
