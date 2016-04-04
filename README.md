# CS321-HW-4-Tester
POSTECH CS321 Programming Language HW 4 Tester / 2016

## 사용법
1. git clone 또는 [ZIP 아카이브 다운로드](https://github.com/Qwaz/CS321-HW-4-Tester/archive/master.zip)를 이용해 파일을 다운로드 받습니다.
2. 다운 받은 파일들을 HW4 폴더 안으로 옮겨 주세요.
3. $ make
4. $ python3 test.py

## 테스트 만들기
test 폴더 내의 `XXX.in` 파일에 테스트 할 람다 표현식을 적습니다. `xxx.n`에는 Call-by-Name으로 리듀스 했을 때의 순서를, `xxx.v`에는 Call-by-Value로 리듀스 했을 때의 순서를 저장합니다.

## 주의사항
- alpha equivalent를 체크하지 않습니다. 단순 문자열 비교로 검사합니다.
- 테스터는 n -> v 순으로 시행되며 getFreshVariable 카운터를 초기화하지 않습니다. 이를 고려해 `.n`과 `.v` 파일을 작성해주세요.
- 표현식이 무한히 리듀스 되어 stack overflow가 발생하는 경우는 본 테스터로 검사할 수 없습니다.
- __테스트를 직접 만드는 것을 장려하기 위해 의도적으로 적은 수의 케이스만을 포함하고 있습니다. 테스터를 통과하더라도 과제 만점이 보장되지는 않습니다.__
