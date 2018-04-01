

# Loading Data

## Ingestion Method

1. File
   HDFS, S3, Local File System 에 저장되어 있는 Data를 가져오는 방법
2. Stream Push
   [Tranquility](https://github.com/druid-io/tranquility)를 사용해서 Stream 데이터를 Druid로 보내는 방법
   Stream(Kafka, Spark Streaming...) -> Tranquility -> Druid
3. Stream Pull
   Druid Real-time Node가 바로 Stream으로부터 데이터를 가져오는 방법

## Hybrid batch/streaming

실시간성을 위해 Streaming Ingestion
데이터 정합성을 위해 Batch Ingestion

Streaming ingestion은 메세지 유실, 중복 메세지 가능성이 있음 -> Batch Ingestion으로 보정작업이 필요함

## Tutorials

- [Loading From Files](http://druid.io/docs/latest/tutorials/tutorial-batch.html)
- [Loading From Streams](http://druid.io/docs/latest/tutorials/tutorial-streams.html)
- [Loading From Kafka](http://druid.io/docs/latest/tutorials/tutorial-kafka.html)