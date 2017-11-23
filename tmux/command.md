# tmux

## Common Command

start 
```
tmux
```

start with session name
```
tmux new -s <name>
```

attach
```
tmux a # 
```

attach by name
```
tmux a -t <name>
```

show sessions list
```
tmux ls
```

kill session
```
tmux kill-session -t <name>
```

kill all the tmux sessions
```
tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill
```


## Prefix 

tmux에서 prefix를 `ctrl+b`를 사용함

`~/.tmux.conf`로 설정을 바꿀 수 있음

```
# Ctrl+a로 prefix 변경
set-option -g prefix C-a
bind-key C-a last-window
bind-key a send-prefix
```

[참고](http://mutelight.org/practical-tmux)


## Session

```
:new<CR>					new session
<prefix> s					list sessions
<prefix> $					name session
exit						exit session
```

## Window

```
<prefix> c					new window
<prefix> n					move to next window
<prefix> p					move to prev window
<prefix> 0-9				move to nth window
<prefix> a					move to last window
<prefix> w					list windows
<prefix> ,					name window
<prefix> &					kill window
```

## Pane

```
<prefix> %					vertical split
<prefix> "					horizontal split

<prefix> <spacebar>			toggle pane layout (vertical <-> horizontal)

<prefix> q					move to pane by number(displayed screen)
<prefix> o					move to next pane
<prefix> <arrow>			move to pane by arrow key

<prefix> x					kill pane

# resize pane in 
<prefix> : resize-pane -D	resizing pane to down
<prefix> : resize-pane -U	resizing pane to upward
<prefix> : resize-pane -R	resizing pane to right
<prefix> : resize-pane -L	resizing pane to left
<prefix> : resize-pane [-D|-U|-R|-L] 20		resizing pane to [down|upward|right|left] by 20 cells

