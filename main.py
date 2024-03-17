import csv, json, zipfile 
import requests, PyPDF2

zip_file_url ='https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2023FD.ZIP'
pdf_file_url = 'https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2023/'
r = requests.get(zip_file_url)
zipfile_name = '2023.zip'

with open(zipfile_name, 'wb') as f:
    f.write(r.content)

with zipfile.ZipFile(zipfile_name) as z:
    z.extractall('.')

with open('2023FD.txt') as f:
    for line in csv.reader (f, delimiter='\t'): #delimiter - tab 
        if line[1]=='Pelosi':
            date = line [7]
            doc_id = line [8]

r = requests.get(f"{pdf_file_url}{doc_id}.pdf")
with open(f" {doc_id}.pdf", 'wb') as pdf_file: 
    pdf_file.write(r.content)
