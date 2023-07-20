#pip install pypdf2
#cd C:\Users\aguir\PycharmProjects\pythonProject3\python projects\automate python\pdf_merger


#.PDF MERGER
import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger() #.PdfMerger allows you to merge multiple PDF files into one

for file in os.listdir(os.curdir):  #check if the file is a pdf file
    if file.endswith(".pdf"):
        with open(file, 'rb') as f: #if True, open the file and read binary 'rb'
            merger.append(f)    #the file is appended to merger object

with open("CombinedA2Inburgering.pdf", 'wb') as output: #the string is the result of multiple pdf files combined.
    merger.write(output)



#.DOCX MERGER
# import docx
# import os
#
# def merge_word_documents():
#     merged_document = docx.Document()
#
#     for file in os.listdir(os.curdir):
#         if file.endswith(".docx"):
#             document = docx.Document(file)
#             for element in document.element.body:
#                 merged_document.element.body.append(element)
#
#     merged_document.save("CombinedDocument.docx")
#
# merge_word_documents()

