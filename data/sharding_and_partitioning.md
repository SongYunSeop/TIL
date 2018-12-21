# Sharding 과 Partitioning

먼저 요약하자면 Sharding은 Partitioning의 하위 개념이라고 생각해도 된다.

## Partitioning

파티셔닝은 성능, 가용성, 유지보수를 위해 하나의 논리적인 테이블을 여러 개의 물리적인 테이블로 쪼개는 행위이다.

다음과 같은 테이블을 파티셔닝 한다고 하자.

| id   | name  | email          |
| ---- | ----- | -------------- |
| 1    | name1 | test1@test.com |
| 2    | name2 | test2@test.com |
| 3    | name3 | test3@test.com |
| 4    | name4 | test4@test.com |
| 5    | name5 | test5@test.com |
| 6    | name6 | test6@test.com |


### Horizontal Partitioning

**Sharding**과 같은 개념이라고 생각하면 된다.

Shard key를 기준으로 데이터의 물리적인 저장소가 나누는 것을 생각하면 된다.

여기서 Shard key는 id를 사용했고 id가 1~3, 4~6 인 데이터가 분류되었다.

Shard Key를 기준으로 데이터의 저장소가 나뉘기 때문에 Shard Key를 잘 결정해야 한다.

| id   | name  | email          |
| ---- | ----- | -------------- |
| 1    | name1 | test1@test.com |
| 2    | name2 | test2@test.com |
| 3    | name3 | test3@test.com |

| id   | name  | email          |
| ---- | ----- | -------------- |
| 4    | name4 | test4@test.com |
| 5    | name5 | test5@test.com |
| 6    | name6 | test6@test.com |

### Vertical Partitioning

하나의 엔티티에 저장된 데이터들을 다수의 엔티티들로 분리하는 것을 의미한다.

DB의 제 3정규화 느낌


| id   | name  |
| ---- | ----- |
| 1    | name1 |
| 2    | name2 |
| 3    | name3 |
| 4    | name4 |
| 5    | name5 |
| 6    | name6 |


| id   | email          |
| ---- | -------------- |
| 1    | test1@test.com |
| 2    | test2@test.com |
| 3    | test3@test.com |
| 4    | test4@test.com |
| 5    | test5@test.com |
| 6    | test6@test.com |
