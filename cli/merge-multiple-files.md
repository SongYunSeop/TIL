# 여러 파일 하나로 합치기

```sh
$ ll  | grep {pattern} | awk '{print $9}' | xargs cat >> {output_filename}
```
