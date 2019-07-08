# Terraform Un-Lock

Terraform을 사용해 여러명의 사용자가 동시에 인프라를 수정하는 것을 방지하기 위해 Terraform에서는 해당 인프라에 대해 Lock을 걸 수 있다.

하지만 `terraform` 명령어를 실행하다가 중간에 어떠한 이유로 Lock이 걸린 상태에서 실패하게 되면 Lock이 해제가 안되어 있을 수 있다.

```sh
$ terraform apply
Error: Error locking state: Error acquiring the state lock: ConditionalCheckFailedException: The conditional request failed
	status code: 400, request id: CC008DNO1QQ3C7V433N8CFUJTFVV4KQNSO5AEMVJF66Q9ASUAAJG
Lock Info:
  ID:        b653c0c4-e200-fbf9-2402-fb024894a5eb
  Path:      resource-path/terraform.state
  Operation: OperationTypeApply
  Who:       yunseop@ip-x-x-x-x.ap-northeast-1.compute.internal
  Version:   0.12.3
  Created:   2019-07-08 01:30:12.693711 +0000 UTC
  Info:


Terraform acquires a state lock to protect the state from being written
by multiple users at the same time. Please resolve the issue above and try
again. For most commands, you can disable locking with the "-lock=false"
flag, but this is not recommended.
```

`-lock=false`옵션을 사용해 Lock을 무시하고 명령어를 사용할 수 있지만 추천하지 않는다.

그럴 떄는 `terraform force-unlock <LOCK-ID>` 명령어를 사용하자!

## Refer 

- https://www.terraform.io/docs/commands/force-unlock.html