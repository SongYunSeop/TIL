# 왜 Primary Key는 Auto Increment로 쓸까?

사실 거의 그냥 당연하게 습관적으로 Auto Increment값으로 넣었는데, 왜 그런지 이유를 몰랐다.

## 1. Insert 시 재정렬  

Primary Key를 (UUID와 같은) 랜덤한 값으로 사용하게 된다면, Row가 Insert 될 때마다 재정렬을 해야한다. 하지만 알다시피 Auto Increment는 그럴필요가 없다.

## 2. Storage  

INT(11), BIGINT(20)에 비해 UUID4 형식은 길이가 36(VARCHAR(36))인데 공간적을 더 차지하기 마련이다.

## 3. 보기쉬운 정렬?  

Insert 순서대로 볼 수 있으니까...

# 하지만 단점도 있다

## 1. 분산환경이라면 Auto Increment는 사용할 수 없다.

## 2. Primary Key를 Insert 후에 알 수 있다.  

DB에 디펜던시가 생김. 하지만 UUID를 사용한다면 Insert 전에도 우리는 어떤 값을 가질지 알 수 있다.


## Refer

- [Auto increment ids vs. UUID, what is better](https://medium.com/@Mareks_082/auto-increment-keys-vs-uuid-a74d81f7476a)