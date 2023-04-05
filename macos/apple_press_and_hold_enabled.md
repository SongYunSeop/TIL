# 키를 누르고 있어도 입력이 안될 때

![apple_press_and_hold_enabled](/static/images/apple_press_and_hold_enabled.png)

다른 곳에서는 괜찮았는데, Pycharm 포함 Jetbrains 사의 IDE에서 해당 문제가 있었음.

```sh
defaults write -g ApplePressAndHoldEnabled -bool false
```

위 명령어 실행 후 IDE 재시작 하면 잘 됨.

## Refer

- https://apple.stackexchange.com/questions/332769/macos-disable-popup-showing-accented-characters-when-holding-down-a-key
