# 화살표 키가 안먹을 때

갑자기 인터프리터에서 화살표 키가 안먹을 때가 있었다.

pdb를 자주 쓰는데 상당히 불편했다.

```
>>> ^[[A^[[D
```

인터프리터에서 방향키를 누르면 저렇게 나오고 동작을 안했다.

`readline` 패키지를 설치하면 되는 것 같다.

```
pip install readline

or

easy_install -a readline
```

이러면 되는듯!
