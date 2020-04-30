# NaverCafe-noti
Notification bot for people who are not members of specific Naver Cafe

## 기능
- 일정 시간마다 게시판을 확인하여 **새 글이 발견되면 텔레그램으로 알림을 전송**합니다.
- 카페의 회원이 아니거나 **게시판 접근 권한이 없어도 사용**할 수 있습니다. (단, 게시글 작성자가 외부 검색을 허용한 경우에만 가능합니다.)
- 게시글 내에 URL이 있는 경우, **자동으로 해당 URL을 엽니다.** (네이버 카페를 특가/재고 알림용으로 사용할 때 유용합니다.)
- GUI가 없습니다.

### 게시글 내 URL 자동 열기 기능 설정

게시글 내 URL 자동 열기 기능은 네이버 카페를 특가/재고 알림용으로 사용할 때 유용하나, 한편 게시판에 광고성 글이 게시될 경우 이 프로그램을 실행하는 컴퓨터에 심각한 보안 문제를 야기할 가능성이 있습니다. 이러한 위험을 방지하기 위해 이 기능을 비활성화하거나, 또는 게시글으로 접속되도록 설정할 수 있습니다.

`source.py` 파일의 **line 55-58**의 코드를 수정합니다.

```python
while nr < lim:
    webbrowser.open(urls[nr].get("href"))
    #webbrowser.open(baseURL + cafeName + "/" + postID)
    nr = nr + 1
```

- `webbrowser.open(urls[nr].get("href"))` (line 56): 게시글 내에 입력된 URL들을 엽니다.
- `#webbrowser.open(baseURL + cafeName + "/" + postID)` (line 57): 게시글을 엽니다.

코드 줄 맨 앞에 `#`을 입력하면 해당 줄은 **비활성화**됩니다. 예를 들어 위와 같은 상황에서, line 56의 코드는 **활성화**, line 57의 코드는 **비활성화** 상태입니다.

**주의: 들여쓰기가 맞지 않으면 오류가 발생합니다.**


## 설치 및 실행
### Firefox 설치
이 프로그램은 Firefox 환경에서 실행되도록 설정되어 있습니다.
Firefox가 설치되어 있지 않은 경우, https://www.mozilla.org/ko/firefox/new/ 에서 설치하십시오.

### Python 설치
https://www.python.org/downloads/ 에서 최신 버전의 Python을 다운로드하여 설치합니다.

### Python 패키지 설치
PowerShell, cmd 등 터미널 소프트웨어에서
```bash
pip install bs4
pip install selenium
pip install python-telegram-bot
pip install requests
```
을 실행합니다.

### 다운로드
1. https://github.com/headacheParrot/NaverCafe-noti 에서 **Clone or download**를 누른 후, **Download ZIP**을 눌러 파일을 다운로드합니다.
2. 파일을 압축 해제합니다.

### 사전 설정
#### Telegram bot 생성
이 부분은 Google에 검색하면 많이 나옵니다.
1. Telegram 검색에서 BotFather을 클릭합니다.
2. Start 클릭 후 /newbot 을 입력하여 봇을 생성합니다.
3. 봇 이름, 봇 사용자 이름을 입력하면 Use this token to access the HTTP API: 뒤에 있는 부분에 위치한 **토큰**을 복사합니다.
4. 웹 브라우저에서 api.telegram.org/bot**xyzxyz**/getUpdates 의 **xyzxyz**에 해당하는 부분에 방금 복사한 토큰을 붙여넣기 후 접속합니다.
5. 생성된 봇에서 아무 메시지나 보낸 후 위 페이지를 새로 고침합니다.
6. 위 페이지의 `"from"::{id:0000000000` 에서 숫자에 해당하는 부분에 위치한 수신자의 **ID**를 기억해 둡니다. 

#### config 파일 수정
3. `config.ini` 파일의 내용을 수정합니다.
   
   - **token**: 텔레그램 봇의 **토큰**을 입력합니다. 
   - **userID**: 텔레그램 알림 수신자의 고유 **ID**를 입력합니다.
     
     예시: 0000000000
   - **boardURL**: **모바일 버전** 게시판의 URL을 입력합니다.
     
     예시: https://m.cafe.naver.com/ca-fe/web/cafes/00000000/menus/000
   - **cafeName**: **데스크톱 버전** 카페 URL cafe.naver.com/**abcde**/ 에서 **abcde**에 해당하는 부분을 입력합니다.
     
     예시: 카페 주소가 cafe.naver.com/**test**/... 인 경우 **test** 입력 
   - **refresh**: 새로고침 시간 간격을 입력합니다. (초 단위)
   
     예시: 10초에 한 번 새로고침할 경우 10 입력
   - **maxAttempt**: 최대 새로고침 횟수를 입력합니다.
     
     예시: 최대 100회 새로고침 할 경우 100 입력

### 실행
`exec.bat` 을 실행합니다.

### 강제 종료
실행 중인 cmd, 또는 PowerShell에서 **CTRL + C** (복사 단축키와 동일) 를 눌러 강제 종료 가능합니다.
