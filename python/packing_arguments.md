# Packing Arguments

다른 사람의 코드를 보다보면 종종 보이는 `*args`와 `**kwargs`가 있었다.

대강 어떤 것인지 느낌은 알고 있었지만 정확히 어떻게 동작을 하는지 몰라서 찾아봤다.

## `*args`

보통 어떤 함수의 인자로 몇개가 들어올지 모를 때 사용된다.

함수 내부에서는 `tuple` type으로 동작하게 된다.

```python
def func(*args):
	print type(args)
	print args

func(1,2,3)
# type<'tuple'>
# (1,2,3)
```

또한 함수를 호출할 때도 `*`를 사용해 list나 tuple을 넣을 수 있다.

```python
list_data = ['a','b','c']

tuple_data = ('d','e','f')

func(*list_data)
# type<'tuple'>
# ('a','b','c')

func(*tuple_data)
# type<'tupel'>
# ('d','e','f')

```

인자로 list를 넣어도 함수 내부에서는 `tupel`로 동작하는 것을 확인할 수 있다.

## `**kwargs`

`*args`와 비슷하지만 이름이 있는 인자로 사용된다.

함수 내부에서는 `dict` type으로 동작하게 된다.

```python
def func2(**kwargs):
	print type(kwargs)
	print kwargs

func2(a=1,b=2,c=3)
<type 'dict'>
{'a': 1, 'c': 3, 'b': 2}
```

`**`를 사용해 함수를 호출할 때 dictionary를 넣을 수 있다.

```python
dict_data = {'a':4, 'b':5, 'c':6}

func2(**dict_data)
<type 'dict'>
{'a': 4, 'c': 6, 'b': 5}
```

## 추가로

보통 `*args`, `**kwargs`를 사용할 때 네이밍을 이대로 쓴다.

물론 `*tuple_datas`, `**dict_datas` 이런식으로 다르게 사용이 가능하지만  
코드를 읽을 때 혼란을 줄 수 있으므로 위의 네이밍을 그대로 사용하자.
