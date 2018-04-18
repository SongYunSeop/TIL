# Public key로 SSH 접속하기

## Key 생성

일단 퍼블릭키가 없다면 생성합시다

```sh
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user1/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/user1/.ssh/id_rsa.
Your public key has been saved in /home/user1/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:0M6+abcdefg+Cg user1@host
The key's randomart image is:
+---[RSA 2048]----+
|=+ooo+..         |
| +ooW.*. T       |
|  =   .+.. _     |
| o o o oo o  +   |
|  * .   S     =  |
|E=oTo ..  S   A  |
|.oo*.A  .  W     |
|  ++B.+  .  D    |
|   OAoD+.   T    |
+----[SHA256]-----+
$ ll ~/.ssh
-rw------- 1 user1 user1 1679 Apr 18 02:17 id_rsa
-rw-r--r-- 1 user1 user1  436 Apr 18 02:17 id_rsa.pub
```

## PubKey 등록

ssh로 접속할 호스트의 접속할 유저의 홈 디렉토리안의  `~/.ssh/authorized_keys`라는 파일에 퍼블릭 키를 등록해주면 된다.

## SSH 접속

아마 이제 접속이 될것이다.

```sh
$ ssh user1@{접속할 호스트}
```

## 만약 접속이 안된다면

#### PubkeyAuthentication

접속할 호스트에 `/etc/ssh/sshd_config`를 살펴보자
`PubkeyAuthentication` 옵션이 no로 되어있거나 주석처리가 되어 있으면 yes로 바꿔서 활성화 해두자

```
PubkeyAuthentication yes
```

그리고 ssh 서비스를 리스타트 하면 된다.

```sh
$ service sshd restart
```

