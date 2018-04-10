# JSON Beautify

아래와 같은 JSON은 보기가 힘들다.

이것을 보기좋게 만들어보자.

```
{"a":"a","b":"b","c":"c"}
```

## 1. Beautify

python의 json.tool을 사용해서 Beautify를 하자.

`:execute '%!python -m json.tool'`

```
{
    "a": "a",
    "b": "b",
    "c": "c"
}
```

## 2. Syntax Highlighting

`:set syntax=json` 으로 Syntax Highlighting까지하면 예뻐진다.

```json
{
    "a": "a",
    "b": "b",
    "c": "c"
}
```

## 3. Key mapping

아래처럼 function을 만들고 키를 맵핑해서 사용하면 편리하다.

```vim
nmap <leader>jb :call JsonBeautify()<CR>

function! JsonBeautify()
    execute '%!python -m json.tool'
    set syntax=json
endfunction
```

함수를 사용하는 방법을 더 알아봐야겠다.