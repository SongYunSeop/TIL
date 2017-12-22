# Datetime과 Timestamp

Python에서 Datetime과 Timestamp를 사용할 때가 많은데 맨날 헷갈린다.

보통 Datetime은 `datetime` 모듈을, Timestamp는 `time` 모듈을 사용한다.

## 알아두면 편한 몇가지 방법

일단 import 하자
```python
from datetime import datetime
from time import time, mktime
```

- String을 datetime으로 변환

```python
datetime.strptime('2017-12-25', '%Y-%m-%d')
```

- datetime을 String으로 변환

```python
datetime.strptime('2017-12-25', '%Y-%m-%d')
```

- datetime을 timestamp로 변환
```python
mktime(datetime.now().timetuple())
```

- timestamp를 datetime으로 변환
```python
datetime.fromtimestamp(time())
```
