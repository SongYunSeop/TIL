# URL & URN & URI

## URL(Uniform Resource Locator)

리소스(Resource)의 위치(Locator)를 표시하는 형식.

```
https://google.com
https://github.com
```

## URN(Uniform Resource Name)

리소스(Resource)의 이름(Name)을 표현하는 형식.  
urn으로 시작하고 콜론(:)으로 구분한다.

```
urn:isbn:9780141036144
urn:ietf:rfc:7230
```

위 두개의 URN은 다음을 나타낸다.

- George Orwell이 쓴 1984년이라는 책
- IETF 스펙 문서 7230, Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing.

## URI(Uniform Resource Identifier)

리소스(Resource)를 식별할 수 있는 식별자(Identifier)라고 할 수 있겠다.

URI는 URL과 URN을 포함하는 개념이다.

### URL 구조

아래 URL을 예로 들어 구조를 파악해보자.

`
http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#Section1
`

- 스키마 혹은 프로토콜

제일 앞의 `http://`부분은 프로토콜을 나타낸다. 브라우저에서는 일반적으로 HTTP, HTTPS 2개를 사용한다.  

- 도메인 이름(Authority)

`www.example.com` 이 부분은 도메인 이름을 나타낸다. 

- 포트

`:80` 이 부분은 포트를 말한다. HTTP 표준 포트는 80, HTTPS 표준 포트는 443인데 이 프로토콜을 사용한다면 보통 포트는 생략된다.

- 경로

`/path/to/myfile.html` 

그 다음으로는 자원의 경로를 나타낸다. 

- 쿼리

`?key1=value1&key2=value2` 웹 서버에 제공되는 추가적인 정보를 `key`와 `value`형태로 전송한다.

- 프래그먼트

`#Section1`

보통 리소스내의 어떠한 위치를 나타낸다. 
