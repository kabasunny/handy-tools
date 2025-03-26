import os
from PyPDF2 import PdfMerger


def merge_pdfs(pdf_list, directory, output_filename):
    merger = PdfMerger()

    for pdf in pdf_list:
        # ディレクトリとファイル名を結合してフルパスを生成
        full_path = os.path.join(directory, pdf)

        if not os.path.exists(full_path):
            print(f"ファイルが存在しません: {full_path}")
            continue  # ファイルが存在しない場合はスキップする

        print(f"ファイルを追加中: {full_path}")
        merger.append(full_path)

    merger.write(output_filename)
    merger.close()
    print(f"結合が完了しました: {output_filename}")


# 使用例
directory = r"C:\Users\a"  # PDFファイルが格納されているディレクトリ
pdf_files = [
    "1_.pdf",
    "2_.pdf",
    "3_.pdf",
    "4_.pdf",
    "5_.pdf",
    "6_.pdf",
]  # 合成するPDFファイルの名前

output_file = os.path.join(directory, "merged_output.pdf")  # 同じディレクトリに出力
merge_pdfs(pdf_files, directory, output_file)
