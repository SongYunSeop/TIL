# Filter groupBy Query Results

GroupBy Query에 대한 결과에 대해서 필터링을 할 수 있다. 우리가 흔히 아는 `having` 조건이다.

``` json
{
    "type": "groupBy",
    "having": {
    
	},
    ...
}
```

Druid에서는 다음과 같은 Having 조건을 사용할 수 있다.

## Query Filter

Query filter는 [Druid에서 사용하는 Filter들](http://druid.io/docs/latest/querying/filters.html)을 그대로 사용할 수 있다. 기본 문법은 다음과 같다.

```json
{
    "type": "filter",
    "filter": <any Druid query filter>
}

// example
{
    "type": "filter",
    "filter": {
        "type": "selector",
        "dimension": "name",
        "value": "yunseop"
    }
}
```

`__time` 을 사용해서 타임스탬프에 대한 필터링도 가능하다.



## Numeric Filter

집계 결과에 대해서 필터링 하는 것이다. 

#### Equal To

`equalTo`을 사용하고,  `HAVING <aggregate> = <value>`과 같다.

```json
{
    "type": "equalTo",
    "aggregation": "<aggregate_metric>",
    "value": "<numeric_value>"
}
```

#### Greater Than

`greaterThan`을 사용하고.  `HAVING <aggregate> > <value>`과 같다.

```json
{
    "type": "greaterThan",
    "aggregation": "<aggregate_metric>",
    "value": "<numeric_value>"
}
```

#### Less Than

`lessThan`을 사용하고 다음.  `HAVING <aggregate> < <value>`과 같다.

```json
{
    "type": "lessThan",
    "aggregation": "<aggregate_metric>",
    "value": "<numeric_value>"
}
```

## Dimension Selector Filter

####  dimSelector

`dimension` 값을 비교해서 같은 것만 가져오는 것인데, Query Filter와 내부적으로 동작이 다른건지 뭔지 잘 모르겠다.

```json
{
    "type": "dimSelector",
    "dimension": "<dimension>",
    "value": "<dimension_value>"
}
```

## Logical Expression Filter

#### AND

`havingSpecs`에 있는 Having 절들을 모두 만족해야 한다.

```json
{
    "type": "and",
    "havingSpecs": [
        {having clause},
        {having clause},
        {having clause},
    ]
}
```

#### OR

`havingSpecs`에 있는 Having 절들중 하나를 만족해야 한다.

```json
{
    "type": "or",
    "havingSpecs": [
        {having clause},
        {having clause},
        {having clause},
    ]
}
```

#### NOT

`havingSpec`의 Having 절을 만족하지 않아야 한다.

```json
{
    "type": "not",
    "havingSpec": {having clause}
}
```

## Refer

- http://druid.io/docs/latest/querying/having.html