import log
from tkinter import *
import excelUtil

#로그설정
logger = log.setLogging("main")

def excelMerge():
    excelUtil.beforeFolderMerge()
    excelUtil.afterFolderMerge()
    resultText.insert(END, '엑셀파일이 만들어졌습니다.\n /excel_result/ 폴더를 확인해주세요\n')


root = Tk()
root.title("업무 자동화 시스템")
root.geometry("300x300")
root.resizable(False, False)

excelMergeBtn = Button(root, text="엑셀 합치기", command=excelMerge)
excelMergeBtn.pack(padx=2, pady=2, fill='x')

queryMakeBtn = Button(root, text="쿼리만들기")
queryMakeBtn.pack(padx=2, pady=2, fill='x')

queryMakeBtn = Button(root, text="엑셀비교하기")
queryMakeBtn.pack(padx=2, pady=2, fill='x')

resultText = Text(root, bg='light gray')
resultText.pack(padx=2, pady=2, fill='both')

root.mainloop()


