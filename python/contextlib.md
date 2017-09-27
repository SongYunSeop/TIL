# contextlib

`Python`에서 `with`라는 키워드를 사용하면뭔가의 시작과 끝을 제어할 수 있다.

보통 파일을 열때 많이 쓰는데 다음과 같다.

```python
with open('test.txt', 'r') as txt:
    txt.read()
    ...
```

이렇게 사용하면 txt라는 변수에 할당된 파일을 `with` 구문이 끝나면 자동으로 닫아준다.

`Python`의 `contextlib`을 사용하면 저것과 비슷한 역할을 하는 함수를 만들 수 있다.

```python
from contextlib import contextmanager

def get_database_connection():
    try:
        conn = db_client.connect()
        yield conn
    finally:
        conn.close()

with get_database_connection() as conn:
    conn.execute(query)
    ...
```
