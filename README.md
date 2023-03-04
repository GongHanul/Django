# Django

2023/03/02

---

# Setting Django Environment

[점프 투 장고](https://wikidocs.net/book/4223)

사용할 파이썬 버전 - 3.10.4

[Python Release Python 3.10.4](https://www.python.org/downloads/release/python-3104/)

1. Python 가상환경 directory 생성
    
    ```powershell
    C:\S_PJT> mkdir venvs
    C:\S_PJT> cd venvs
    ```
    
2. 파이썬 가상환경 생성
    
    ```powershell
    C:\S_PJT\venvs> python -m venv venv_1
    ```
    
3. 가상환경에 진입하기
    
    ```powershell
    C:\S_PJT\venvs\venv_1\Scripts> activate
    (venv_1) C:\S_PJT\venvs\venv_1\Scripts>
    ```
    
4. 가상환경에서 벗어나기
    
    ```powershell
    (venv_1) C:\S_PJT\venvs\venv_1\Scripts> deactivate
    ```
    
5. 장고 설치
    
    ```powershell
    (venv_1) C:\S_PJT\venvs\venv_1\Scripts> pip install django==4.0.3
    (venv_1) C:\S_PJT\venvs\venv_1\Scripts> python -m pip install —upgrade pip
    ```
    
6. 프로젝트 생성 및 가상환경에 진입
    
    ```powershell
    C:\S_PJT> mkdir projects
    C:\S_PJT> cd projects
    C:\S_PJT\projects> C:\S_PJT\venvs\venv_1\Scripts\activate
    (venv_1) C:\S_PJT\projects> mkdir pjt_1
    (venv_1) C:\S_PJT\projects> cd pjt_1
    (venv_1) C:\S_PJT\projects\pjt_1> django-admin startproject config .
    ```
    
7. 개발 서버 구동하고 웹사이트에 접속
    
    ```powershell
    (venv_1) C:\S_PJT\projects\pjt_1> python [manage.py](http://manage.py) runserver
    ```
    
    [http://127.0.0.1:8000](http://127.0.0.1:8000) or [http://localhost:8000](http://localhost:8000)
    

### 한 번에 가상환경에 진입하는 방법

1. pjt_1_access.cmd 파일 생성
    
    ```
    @echo off
    cd C:\S_PJT\projects\pjt_1
    C:\S_PJT\venvs\venv_1\Scripts\activate
    ```
    
2. 환경 변수 Path에 추가
    
    <win+R> sysdm.cpl
    
    고급, 환경 변수 선택
    
    Path 편집
    
    `C:\S_PJT\venvs` 디렉터리 추가 및 확인
    
3. pjt_1_access 명령 실행
    
    ```powershell
    C:\> pjt_1_access
    ```
    

2022/03/04

---

# Pybo Service 구축

[Pybo Service](https://www.notion.so/Pybo-Service-04ddac7dfcf8429991ecea05be948546)