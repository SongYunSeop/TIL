# 프로세스 죽이기

```bash
$ kill $(ps aux | grep migrate | awk '{print $2}')
```
