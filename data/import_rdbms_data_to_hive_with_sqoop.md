# Sqoop으로 MySQL 데이터 Hive로 Import 하기

[Sqoop](http://sqoop.apache.org/)은 Hadoop과 RDBMS간에 데이터를 주고받기 위해 사용되는 툴이다.

## Table을 Import

```sh
sqoop import --connect jdbc:mysql://localhost:3306/sqoop 
--username root 
-P 
--split-by id 
--columns id,name 
--table customer  
--target-dir /user/cloudera/ingest/raw/customers 
--fields-terminated-by "," 
--hive-import 
--create-hive-table 
--hive-table sqoop_workspace.customers
```
## Query 결과를 Import

WHERE 절에 `$CONDITIONS`를 꼭 넣어주어야 함
```sh
sqoop import --connect jdbc:mysql://localhost:3306/sqoop 
--username root 
-P 
--split-by id 
--columns id,name 
--target-dir /user/cloudera/ingest/raw/customers 
--fields-terminated-by "," 
--hive-import 
--create-hive-table 
--hive-table sqoop_workspace.customers
--query 'SELECT * FROM customer WHERE $CONDITIONS'
```

## Refer

- [http://sqoop.apache.org/](http://sqoop.apache.org/)