# Multiprocessing Pool과 함꼐 tqdm 사용하기

```python
import time
from multiprocessing import Pool
from tqdm import tqdm


def func(x):
    time.sleep(1)
    return 

pool = Pool()
total = 1000
with tqdm(total=total) as pbar:
    for _ in tqdm(pool.imap_unordered(func, range(total))):
        pbar.update()
pool.close()
pool.join()
```
