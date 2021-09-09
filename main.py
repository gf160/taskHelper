import log
from tkinter import *
import excelUtil

#로그설정
logger = log.setLogging("main")

def excelMerge():
    bFlag = excelUtil.beforeFolderMerge()
    if bFlag :
        # 파일이 정상적으로 생성됨
        resultText.insert(END, '/excel_result/excel_before.xlsx 파일이 생성되었습니다.\n')
    else :
        resultText.insert(END, 'excel_before 폴더가 비어있습니다.\n')

    aFlag = excelUtil.afterFolderMerge()
    if aFlag :
        resultText.insert(END, '/excel_result/excel_after.xlsx 파일이 생성되었습니다.\n')
    else :
        resultText.insert(END, 'excel_after 폴더가 비어있습니다.\n')


root = Tk()
root.title("업무 자동화 시스템")
root.geometry("400x300")
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


