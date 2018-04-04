# Updating Existing Data

Ingestion된 데이터를 저장하고 사용하다가 데이터를 업데이트하고 싶을 때

## Updating Dimension Values

Dimension 값을 자주 바꾸길 원한다면 [Lookup](http://druid.io/docs/latest/querying/lookups.html)을 사용할 수 있다.

## Rebuilding Segments(Reindexing)

특정 기간에 대해서 세그먼트를 다시 저장할 수 있다.
기존 세그먼트에 컬럼을 추가하거나, 롤업 granularity를 바꾸고 싶을 때 사용한다.

이 방법을 사용할 경우에 대비하여 원시 데이터의 사본을 보관해야한다.

## Dealing with Delayed Events(Delta Ingestion)

Batch Ingestion이 되었지만 그 후에 지연된 이벤트가 들어왔을 때 새로 인덱싱을 하는것 대신, `Delta Ingestion`을 사용해 기존 세그먼트에 추가할 수 있다.





