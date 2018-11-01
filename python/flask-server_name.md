# Flask의 SERVER_NAME 설정에 관하여

실험을 위해 `/etc/host` 파일에 다음과 같이 추가하자.

```
# /etc/host
127.0.0.1       localhost
127.0.0.1       test.localhost
127.0.0.1       test_localhost
```

우선 `SERVER_NAME`을 `localhost:5000`으로 설정해보자.


```python
from flask import Flask, url_for

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```


위 코드처럼 `SERVER_NAME` 설정을 하면 호스트가 설정한 값으로 들어온 요청이 아니면 404를 떨군다.

```sh
$ curl localhost:5000
Hello, World!

$ curl test.localhost:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

$ curl test_localhost:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

```

여기에 `subdomain`을 사용해서 라우팅이 추가되면 또 이상해진다.

```python
from flask import Flask, url_for

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/subdomain', subdomain='test')
def subdomain():
    return 'Hello, Subdomain!'

if __name__ == '__main__':
    app.run()
```

뜨악...

```
$ curl localhost:5000/subdomain
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>

$ curl test.localhost:5000/subdomain
Hello, Subdomain!

$ curl test_localhost:5000/subdomain
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```

`SERVER__NAME`을 사용할 땐 주의합시다.

## Refer 

- https://github.com/pallets/flask/issues/998
