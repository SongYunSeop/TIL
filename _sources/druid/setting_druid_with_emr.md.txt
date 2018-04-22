# EMR과 함께 Druid를 셋팅해보자!

## Versions

- `Druid 0.12.0`
- `Java 1.8.0_161`

## 과정

1. Java 설치

```sh
sudo yum install -y java-1.8.0-openjdk-devel.x86_64
```

2. druid User 추가 & druid 다운로드 & unzip

3. mv druid-0.12.0 /opt/druid/druid-0.12.0 

4. 설정 파일들 수정(jvm.config, runtime.properties)

5. metadata storage 설정(MySQL)

   ```sh
   # /opt/druid/druid-0.12.0/conf/druid/_common/common.properties
   druid.extensions.loadList=["druid-kafka-eight","mysql-metadata-storage", "druid-s3-extensions"]
   druid.metadata.storage.type=mysql
   druid.metadata.storage.connector.connectURI=jdbc:mysql://{host}:{port}/{database}
   druid.metadata.storage.connector.user=user
   druid.metadata.storage.connector.password=password
   ```

6. 실행

   ```sh
   $ ./bin/historical.sh start
   $ ./bin/overlord.sh start
   $ ./bin/middleManager.sh start
   $ ./bin/broker.sh start
   $ ./bin/coordinator.sh start
   ```

   다운 타임없이 재실행을 하고 싶은 경우 다음과 같이 추천함

   1. Historical
   2. Overlord (if any)
   3. Middle Manager (if any)
   4. Standalone Real-time (if any)
   5. Broker
   6. Coordinator (or merged Coordinator+Overlord)

## EMR과 같이 사용하고 싶다면

다른 하둡 버젼을 사용하는 것이기 때문에 그 하둡 설정관련 파일들이 필요합니다.
[Working with different versions of Hadoop](http://druid.io/docs/latest/operations/other-hadoop.html) 참고

1. EMR 하둡 config파일 가져오기
   EMR의 `/etc/hadoop/conf` 안에 있는 `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, `yarn-site.xml` 파일을 가져와서 드루이드의 `conf/druid/_common/` 안에 넣어줍니다.


2. S3 extension 추가 및 Deep Storage 설정
   `cont/druid/_common/common.runtime.properties`

   ```sh
   druid.extensions.loadList = ["druid-s3-extensions"]

   druid.storage.type=s3
   druid.storage.bucket=druid-bucket
   druid.storage.baseKey=druid/segments
   druid.s3.accessKey=XXXXXXXXXXXXXXX
   druid.s3.secretKey=XXXXXXXXXXXXXXX
   ```

3. 라이브러리 추가

   ```sh
   $ cp -r /usr/lib/hadoop/client/* /opt/druid/druid-0.12.0/hadoop-dependencies/hadoop-client/emr/*
   $ cp -r /usr/share/aws/emr/emrfs/* /opt/druid/emrfs
   $ cp -r /usr/share/aws/aws-sdk-java/* /opt/druid/aws-sdk-java

   ```

4. bin/node.sh 수정
   middleManager를 실행할 때 library를 추가함

   ```sh
   JAVA_HOME=/usr/lib/jvm/java
   if [ "$nodeType" == "middleManager" ]; then
   	LIB_DIR=$LIB_DIR/*:/opt/druid/emrfs/conf:/opt/druid/emrfs/lib/*:/opt/druid/emrfs/auxlib/*:/opt/druid/aws-java-sdk
   fi
   ```

5. middleManager 재시작

6. index 파일에 s3 accessKey, secretKey 추가 && `hadoopDependencyCoordinates` emr로 설정

   ```json
   {
       ...
       "spec": {
           "tuningConfig": {
               "jobProperties": {
                   "fs.s3.awsAccessKeyId" : "XXXXXXXXXXXXXXX",
                   "fs.s3.awsSecretAccessKey" : "XXXXXXXXXXXXXXX"
               }
           }
   	},
   	"hadoopDependencyCoordinates": ["org.apache.hadoop:hadoop-client:emr-client"]
   }
   ```

## Refer

- http://druid.io/docs/latest/operations/other-hadoop.html
- http://aipkds.tistory.com/136