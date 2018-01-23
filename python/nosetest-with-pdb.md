# nosetest와 pdb

nose는 python testing libary이다.

개발할 때 보통 `import pdb; pdb.set_trace()`를 많이 쓰는데

Test Code에서도 사용하고 nosetest로 해보니 뭐 아무런 변화가 없었다.

알고보니 이런 옵션이 있었다.

```
  -s, --nocapture       Don't capture stdout (any stdout output will be
                          printed immediately) [NOSE_NOCAPTURE]
```

디버깅을 위해 `nosetests`를 `nosetests -s`로 alias해서 쓰고 있다.

