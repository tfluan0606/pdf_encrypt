import PyPDF2
import pandas as pd
from os import listdir

#這是你存放pdf的路徑設定
pdf_path = 'pdf'

#password.xlsx這個是假設你存密碼和檔名的excel檔
df = pd.read_excel('password.xlsx')
filename_list = pd.Series.tolist(df['檔名'])
password_list = pd.Series.tolist(df['密碼'])


for i in range(len(filename_list)):
    pdfFile = open(pdf_path+'/'+str(filename_list[i])+'.pdf', 'rb')
    # Create reader and writer object
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
    pdfWriter.encrypt(str(password_list[i]))
    #存放輸出檔案的資料夾預設是out
    resultPdf = open('out/'+str(filename_list[i])+'.pdf', 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()
