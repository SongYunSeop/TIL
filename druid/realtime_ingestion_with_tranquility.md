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

## Troubleshootings

[Github Trable Page](https://github.com/druid-io/tranquility/blob/master/docs/trouble.md)

### 이벤트가 성공적으로 보내졌지만 드루이드에서는 데이터가 보이지 않음.

가장 일반적인 이유는 이벤트의 타임스탬프가 설정한 `windowPeriod` 밖에 있기 때문이다. 기본적으로 10분으로 설정되어 있는데, 이는 이벤트의 타임스탬프가 10분 전보다 더 이전의 데이터들은 드랍시킨다. 다음을 확인하자.

1. `windowPeriod` 안의 이벤트를 보내는지 확인.  [Overview](https://github.com/druid-io/tranquility/blob/master/docs/overview.md#segment-granularity-and-window-period)를 보면 어떻게 동작하는지 알 수 있다.
2. 적절한 `Timstamper`와 `TimestampSpec`를 사용하고 있는지 확인. 

### Task가 종료되지 않음.

가장 일반적인 이유는 `handoff`가 발생하지 않아서 그렇다. `historical` 노드가 realtime task로 생성된 세그먼트를 로드하지 않아서.([Overview](https://github.com/druid-io/tranquility/blob/master/docs/overview.md)를 보면 어떻게 동작하는지 알 수 있다.)

`Coordinator`와 `Historical` 노드가 올라와 있는지 확인하고, `Historical` 노드에 새로운 세그먼트를 저장할 충분한 용량이 있는지 확인. 만약 그렇지 않다면 `Coordinator` 로그에 warning이나 error 메세지가 출력됨.

또 다른 가능성은 `windowPeriod`가 너무 길기 때문. `segmentGranularity`의 interval이 넘고 `windowPeriod`가 지나야만 `Hand-Off`가 일어난다.

### Jackson이나 Curator Exception이 발생함.

Most of Tranquility uses com.fasterxml.jackson 2.4.x, but Curator is still built against the older org.codehaus.jackson.
It requires at least 1.9.x, and people have reported strange errors when using older versions of Jackson (usually
1.8.x). Tranquility tries to pull in Jackson 1.9.x, but this may be overridden in your higher-level project file. If
you see any strange Jackson or Curator errors, try confirming that you are using the right version of Jackson. These
errors might include the following:

- java.io.NotSerializableException: org.apache.curator.x.discovery.ServiceInstance
- org.codehaus.jackson.map.exc.UnrecognizedPropertyException: Unrecognized field "name" (Class org.apache.curator.x.discovery.ServiceInstance), not marked as ignorable

To force a particular Jackson version, you can use something like this in your POM:

```xml
<dependency>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-jaxrs</artifactId>
    <version>1.9.13</version>
</dependency>
<dependency>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-xc</artifactId>
    <version>1.9.13</version>
</dependency>
<dependency>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-core-asl</artifactId>
    <version>1.9.13</version>
</dependency>
<dependency>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-mapper-asl</artifactId>
    <version>1.9.13</version>
</dependency>
```