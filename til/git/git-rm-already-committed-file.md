Title: 이미 커밋된 파일 삭제하고 싶을 때!

# 이미 커밋된 파일 삭제하고 싶을 때!


실수로 `.gitignore`에 넣는것을 빠뜨리고 어떤 파일을 커밋했을 때

`git rm --cached`를 사용하면 삭제할 수 있다.

```bash
$ git rm --cached <file_name>
rm '<file_name>'
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    <file_name>

$ git commit -m 'Delete file!'

...

$ echo '<file_name>' >> .gitignore
```

