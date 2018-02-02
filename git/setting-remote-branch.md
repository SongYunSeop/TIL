# 브랜치의 Remote Branch 설정하기

`test`라는 브랜치를 `upstream/test` 라는 Remote 브랜치를 바라보게 만들고 싶다.

## 브랜치를 새로 만드는 경우

`--track` 옵션을 사용하면 브랜치를 만들어준다.

```
git branch --track test upstream/test
```

## 이미 브랜치가 있는 경우

`--set-upstream-to`, `-u` 옵션을 사용하자.

```
git branch --set-upstream-to test upstream/test
```

만약 `upstream/test` 브랜치가 없으면 에러를 뿜는다.

```
fatal: branch 'upstream/test' does not exist
```

그러면 Push를 해주자.

```
git push -u upstream test
```
