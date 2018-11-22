# utf8과 utf8mb4?

`utf8`과 `utf8mb4` 모두 MySQL에서 지원하는 Charset이다.

UTF-8은 원래 4 bytes로 문자를 표현하는 문자 인코딩 방식이다.

예전에는 모든 전세계 모든 문자들이 3 bytes로 저장되었다고 한다.

그리하여 MySQL은 성능상의 이유로 `utf8`을 3 bytes 기반의 자료형으로 설계하여 UTF-8을 지원하게 된다.

하지만 최근에는 4 bytes 문자열(예를 들어 Emoji 😀)이 쓰이곤 하는데 기존의 `utf8`로 저장할 수 없게 되었다.

그리하여 [2010년 3월 24일 패치로](https://dev.mysql.com/doc/relnotes/mysql/5.5/en/news-5-5-3.html) MySQL은 4 bytes 기반의 문자열을 지원하기 위해 `utf8mb4`라는 Charset을 추가한다.

utf8 -> utf8mb4로 자료형을 변환하면 값의 손실은 없다함.


## Refer

- [https://blog.lael.be/post/917](https://blog.lael.be/post/917)
