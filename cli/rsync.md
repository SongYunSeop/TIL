# rsync

Rsync(Remote Synchronization)
원격에 있는 파일과 디렉토리를 동기화하는 툴

## Usage

```sh
rsync [OPTION]... SRC [SRC]... DEST
rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
rsync [OPTION]... [USER@]HOST:SRC [DEST]
rsync [OPTION]... [USER@]HOST::SRC [DEST]
rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]
```

## Options

| Option                | Description                                                  |
| :-------------------- | ------------------------------------------------------------ |
| -v / --vervose        | 정보 출력                                                    |
| -a / --archive        | -rtlpgoD 옵션을 사용한 것과 동일, 보통 이 옵션을 사용해서 동기화함 |
| -r / --recursive      | 하위 디렉토리까지 동기화                                     |
| -t / --times          | 파일의 타임스탬프를 동기화                                   |
| -l / --links          | 심볼릭 링크 파일도 동기화함                                  |
| -g / --group          | 그룹 정보를 동기화함                                         |
| -o / --owner          | 소유자 정보를 동기화함                                       |
| -D / --devices        | 동기화할 디바이스를 재작성함. root권한을 가진 유저만 가능    |
| -z / --compress       | 압축해서 동기화                                              |
| -h / --human-readable | 결과를 읽기편하게 출력                                       |
| --progress            | 진행상황을 표시                                              |
| --exclude             | 패턴과 일치한 파일을 제외함                                  |
