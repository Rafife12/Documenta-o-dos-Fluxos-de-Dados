import pdfplumber
import csv

def pdfToCsv(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf, open(csv_path, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter=';', skipinitialspace=True, lineterminator='\n')
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    writer.writerow(row)
    print(f"O arquivo foi convertido com sucesso! {csv_path}")

pdfToCsv("entrada.pdf", "saida.csv")
