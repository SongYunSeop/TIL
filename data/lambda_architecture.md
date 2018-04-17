# Lambda Architecture

실시간 분석을 지원하는 빅데이터 아키텍쳐
대량의 데이터를 실시간으로 분석하기 위해서 Batch로 만든 데이터와 실시간 데이터를 혼합해서 사용하는 방식

![](http://lambda-architecture.net/img/la-overview_small.png)

## 데이터 파이프 라인

1. 데이터가 시스템으로 들어감.
   이 때 Batch Layer와 Speed Layer로 둘다 들어가게 됨
2. Batch Layer는 두가지 기능을 해야함
   1. Immutable, Append-only한 raw data를 저장하고 관리함
   2. Batch View를 만들기 위해 사
3. Serving Layer는 Batch View의 인덱스를 생성해 Query가 빠른 속도록 데이터를 가져갈 수 있게 해야함
4. Speed Layer는 Real-time View를 생성해 최근 데이터에 대해서 Query를 할 수 있음
5. Query는 Batch View와 Real-time View에 질의해 두 결과를 합쳐야함

## Layer

이 아키텍쳐에는 총 3개의 레이어가 존재함

- Batch Layer
  새로운 데이터가 들어와서 저장되는 곳.
- Serving Layer
  Batch Job으로 만들어진 Batch View가 저장되어 있음
  Query 가 Batch View로 부터 데이터를 가져감
- Speed Layer
  새로운 데이터가 들어와 Real-time View를 저장함
  Query 가 Real-time View로 부터 데이터를 가져감

Batch Layer와 Speed Layer에서 가지고 있는 View의 데이터가 중복이 되지 않기 관리해야함

## Refer

[Lambda Architecture](http://lambda-architecture.net/)