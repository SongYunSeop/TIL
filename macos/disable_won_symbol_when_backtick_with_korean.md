# 한글 키보드에서 won symbol(₩) 대신 backtick(`)를 입력하고 싶다면

맥의 한글 키보드에는 backtick(`)이 없고 그 자리에 원화 기호(₩)가 있다. 

거의 쓸 일이 없는 원화 기호는 없애고 더 자주 쓰는 backtick으로 바꿔버리자.

`~/Library/KeyBindings/DefaultkeyBinding.dict` 경로에 파일이 없다면 생성하고 아래 내용을 넣자.

```
{
    "₩" = ("insertText:", "`");
}
```

그리고 재부팅하고나면 한글 키보드에서도 backtick을 쓸 수 있다.
