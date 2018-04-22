# PATCH Method

이름에서도(PATCH) 유추할 수 있겠지만 자원을 업데이트 하는 Methos이다.

PUT Mtehod와 유사하지만 자원의 전체가 아닌 일부만 변경을할 때 쓰인다.

요청 문서에 지정된 특성은 업데이트 되고, 지정되지 않은 특성들은 업데이트 하지 않는다.

PATCH Method는 Safe하지도 Idempotent하지도 않다.



## Refer

- https://tools.ietf.org/html/rfc5789

- https://tools.ietf.org/html/rfc7231#section-4.2
