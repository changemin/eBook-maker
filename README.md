## 프로젝트를 시작하게 된 계기
국어 수행평가 중 시집 ebook만들기가 있었는데 너무 노가다 여서 해결하고자 만들게 되었다.
~~정말 귀찮다~~
잘 사용될지는 모르지만 재미있을거 같아서 시작했다.

## 파일 구조
* res 
    * background-imgs
        > [배경화면번호.png]의 형식으로 저장한다.
    * font-files
        > 시집에 사용할 폰트를 조정한다.
    * poem-txt 
        > 시의 원문을 저장한다. 형식은 [poem(N).txt]이다.
    * read-files-example
        > 예제들
* main.py
* poem2jpg.py
* txt2poem.py
* README.md

## 프로그램을 실행하기 전

> python Pillow를 import하기 위해서 cmd에서 Pillow를 설치해 준다. 

    C:>pip install Pillow

## 유용한 기능들

> 시의 개수와 background img의 개수를 맞추기 위해서 migration을 해주어야 한다.(배경 이미지나 새로운 시를 입력했을 때도 migrate필요) [-m]

    C:\YOURWORKSPACE> python main.py -m

> 새로운 시를 입력할 수도 있다. [-add]

    C:\YOURWORKSPACE> python main.py -add 
    -----------------Create New poem------------------
    시 제목을 입력해주세요:이거슨 시 제목
    시인의 이름을 입력해주세요:변경민
    본문 입력('@'를 입력하여 본문 입력을 끝냅니다.) : 안녕 반가워
    본문 입력('@'를 입력하여 본문 입력을 끝냅니다.) : 이건 시야
    본문 입력('@'를 입력하여 본문 입력을 끝냅니다.) : @
    새로운 시 제목 :이거슨 시 제목
    새로운 시인:변경민
    새로운 시 본문:['안녕 반가워', '이건 시야']
    -------------New poem added to list---------------

> 가장 최근에 추가한 시를 제거할 수도 있다. [-rm]

    C:\YOURWORKSPACE> python .\main.py -rm

> 현재까지의 시를 나열할 수도 있다. [-l]

    C:\YOURWORKSPACE> python .\main.py -l
    poem(1).txt: 기다림

    poem(2).txt: 깨우침

    poem(3).txt: 이것은 시

    poem(4).txt: 이거슨 시 제목

## 사용예시
> res/peom-txt/poem(1).txt

    기다림
    유치환
    무척이나 무척이나 기다렸네라.
    기다리다 기다리다 갔네라.

    날에 날마다 속여 울던 뱃고동이
    그제사 아니 우는 빈 창머리
    책상 위엔 쓰던 펜대도 종이도 그대로
    눈익은 검정 모자도 벽에 걸어 둔대로

    두번 다시 못 올 길이었으매
    홀홀히 어느 때고 떠나야 할 길이었으매
    미래없는 억만 시간을
    시간마다 기다리고 기다렸네라.

> res/background-imgs/1.PNG (여러개 중 하나를 무작위 선택)
![res/background-imgs/1.PNG](res/background-imgs/1.PNG)

> cmd(또는 terminal)에서 main.py실행

    C:\Users\workspace\Python\eBook-maker>python main.py
    1번 시 제목:기다림

    시인:유치환

    [LOG]Image Saved!
    --------------------------------

> result/poemResult(1).png

![result/poemResult(1).PNG](result/poemResult(1).png)

## 이런식으로 완성이 된다!