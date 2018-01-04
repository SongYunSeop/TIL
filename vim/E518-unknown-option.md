# E518: Unknown option 에러가 날때

```
Error detected while processing modelines:
line  262:
E518: Unknown option: #
Press ENTER or type command to continue
```

어떤 파일을 열면 이런 에러 메세지가 나올떄가 있었다.

`modeline`을 처리하는데 에러가 난것 같다.  
하지만 난 `modeline`이라는 것이 뭔지도 모르는데...?

조금 알아보니 vim의 설정을 하는 방법중의 하나이고 그것에서 문제가 생긴 것 같다.

## auto-setting

`:help auto-setting`를 실행하면 다음을 확인할 수 있다.

> 2. Automatically setting options                        auto-setting
> 
> Besides changing options with the ":set" command, there are three alternatives
> to set options automatically for one or more files:
> 
> 1. When starting Vim initializations are read from various places.  See
>    initialization.  Most of them are performed for all editing sessions,
>    and some of them depend on the directory where Vim is started.
>    You can create an initialization file with :mkvimrc, :mkview and
>    :mksession.
> 2. If you start editing a new file, the automatic commands are executed.
>    This can be used to set options for files matching a particular pattern and
>    many other things.  See autocommand.
> 3. If you start editing a new file, and the 'modeline' option is on, a
>    number of lines at the beginning and end of the file are checked for
>    modelines.  This is explained here.

요약해보면 option을 바꾸고 싶을 때 `set` 커맨드를 사용하는 방법말고 다른 방법이 있다한다.  
그 방법은 `initialization`, `autocommand`, `modeline` 이정도가 있다한다.k

1. `initialization`은 `vimrc`를 사용하는 방법이다.
2. `autocommand`는 `autocmd`라는 설정으로 파일을 읽기, 쓰기 등 이벤트가 일어날 때 어떤 명령을 실행할 지 설정할 수 있다.
3. `modeline`은 어떤 파일을 열때 파일 처음부터 몇줄까지 이 파일에 대해서 vim 설정을 할 수 있는 방법이다.

이것에 대한 더 자세한 내용은 `:help auto-setting`을 실행하서 보거나 [다음페이지](http://vimhelp.appspot.com/options.txt.html#auto-setting)에 들어가서 보자.

## 해결 방법

`vimrc`에 `set nomodeline`을 추가하면 된다.

## Refer

- [https://stackoverflow.com/questions/8583028/vim-e518-unknown-option](https://stackoverflow.com/questions/8583028/vim-e518-unknown-option)
- [http://vimhelp.appspot.com/options.txt.html#auto-setting](http://vimhelp.appspot.com/options.txt.html#auto-setting)

