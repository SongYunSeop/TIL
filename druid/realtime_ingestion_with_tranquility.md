# RealTime Ingestion with Tranquility

[Tranquility](https://github.com/druid-io/tranquility)는 실시간 이벤트 스트림을 Druid에서 처리하는 것을 도와준다.
Partitioning, Replication, Service Discovery, Scheme Rollover 등 

## 설치

http://druid.io/downloads.html 에서 다운로드

## 설정

## 적당한 설정 파일을 만든다.

```json
{
    "dataSources": {
        "myDataSource": {
            "spec": {
                "dataSchema": {
                    "dataSource": "myDataSource",
                    "granularitySpec": {
                        "queryGranularity": "none",
                        "segmentGranularity": "hour",
                        "type": "uniform"
                    },
                    "metricsSpec": [
                        {
                            "name": "count",
                            "type": "count"
                        }
                    ],
                    "parser": {
                        "parseSpec": {
                            "dimensionsSpec": {
                                "dimensions": [
                                    "dimension1"
                                ]
                            },
                            "flattenSpec": {
                                "fields": [
                                    {
                                        "expr": "$.data.dimension1",
                                        "name": "dimension1",
                                        "type": "path"
                                    },
                                    {
                                        "expr": "$.data.event_timestamp",
                                        "name": "event_timestamp",
                                        "type": "path"
                                    }
                                ],
                                "useFieldDiscovery": true
                            },
                            "format": "json",
                            "timestampSpec": {
                                "column": "event_timestamp",
                                "format": "auto"
                            }
                        },
                        "type": "string"
                    }
                },
                "ioConfig": {
                    "type": "realtime"
                },
                "tuningConfig": {
                    "intermediatePersistPeriod": "PT10M",
                    "maxRowsInMemory": "1000000",
                    "type": "realtime",
                    "windowPeriod": "PT10M"
                }
            },
            "properties": {
                "druidBeam.firehoseChunkSize": "100000",
                "task.partitions": "2",
                "task.replicants": "1",
                "topicPattern": "kafka_topic"
            }
        }
    },
    "properties": {
        "commit.periodMillis": "15000",
        "consumer.numThreads": "2",
        "druid.discovery.curator.path": "/druid/discovery",
        "druid.selectors.indexing.serviceName": "druid/overlord",
        "kafka.group.id": "tranquility",
        "kafka.zookeeper.connect": "zk1:2181,zk2:2181,zk3:2181",
        "zookeeper.connect": "zk1:2181,zk2:2181,zk3:2181"
    }
}
```

## 실행

```sh
$ ./bin/tranquility kafka -configFile {CONFIG_FILE_PATH}
```

## 이슈

1. `Failed to create directory within 10000 attempts`

```
2018-04-27 02:18:32,010 [finagle/netty3-1] ERROR com.metamx.common.scala.control$ - Non-retryable response for uri[/druid/indexer/v1/task] with content: {"error":"Instantiation of [simple type, class io.druid.segment.indexing.RealtimeTuningConfig] value failed: Failed to create directory within 10000 attempts (tried 1524795511982-0 to 1524795511982-9999)"}
```

드루이드 모든 컴포넌트의 jvm.config에 `-Djava.io.tmpdir=/tmp/druid` 로 설정