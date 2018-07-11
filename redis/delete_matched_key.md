# 매칭된 Key 지우기

```sh
$ redis-cli KEYS "prefix:*" | xargs redis-cli DEL
```

## Refer

- https://stackoverflow.com/questions/4006324/how-to-atomically-delete-keys-matching-a-pattern-using-redis?answertab=votes#tab-top
