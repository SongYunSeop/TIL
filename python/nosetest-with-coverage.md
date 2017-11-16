# nosetest와 coverage

nosetest에는 기본적으로 coverage를 측정할 수 있는 기능이 있어서 몇가지 옵션만 추가로 넣어주면 바로 사용가능하다.

일단 nose, coverage를 설치하자

```bash
$ pip install nose
$ pip install coverage
$ nosetests --with-coverage --cover-package=app --cover-html --cover-html dir=cover tests/test_coverage.py
```

옵션에 대한 상세한 내용은 [공식문서](http://nose.readthedocs.io/en/latest/plugins/cover.html)에서 확인할 수 있다.

|           옵션            |               설명                |
| ------------------------- | --------------------------------- |
| --with-coverage           | 테스트 시 coverage를 측정하겠다.  |
| --cover-package           | coverage를 측정할 패키지          |
| --cover-earse             | 이전에 측정한 coverage 통계 삭제  |
| --cover-tests             | |
| --cover-min-percentage    | |
| --cover-inclusive         | |
| --cover-html              | 결과를 html 형태로 저장           |
| --cover-html-dir          | html 파일이 저장될 디렉토리(default=cover) |
| --cover-branch            | |
| --cover-xml               | 결과를 xml 형태로 저장            |
| --cover-xml-file          | xml 파일이 저장될 디렉토리        |
| --cover-config            | coverage 설정 파일 위치           |
| --cover-no-print          | coverage 정보를 출력안함          |
