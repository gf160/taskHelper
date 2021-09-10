## 개요
 ### RPA 프로젝트
 분산된 엑셀파일들을 하나의 파일로 Merge하고, Merge된 두 파일을 비교하여 결과 파일을 생성  
 Merge된 파일을 DB에 Insert 할 수있는 sql문으로 변환  
 
   + 추가로 DB에 직접 접속하여 데이터 Insert 까지 향후 개발 가능
 
 
## 기능
 1. excel_before, excel_after 디렉토리에 있는 .xlsx(엑셀) 파일을 읽어 하나의 파일로 merge 하는 작업을 진행
 2. Merge된 파일을 Insert할 수 있게 sql문 생성
 3. Merge된 파일을 비교하여 하나의 엑셀 파일생성
 

## 사용 모듈

    pip install xlrd
    pip install openpyxl
    pip install pandas
    
## 파일 구성
1. main.py
    * 실행파일
    * Tkinter GUI 생성
 
2. log.py
    * logging 설정 모듈
 
3. excelUtil.py
    * 엑셀 작업(merge) 모듈
