import tkinter as tk
from tkinter import filedialog, messagebox

import os
import zipfile
import tempfile

from PIL import Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

zip_file = ""
word_file = ""


def select_zip():
    global zip_file
    zip_file = filedialog.askopenfilename(
        title="ZIP 파일 선택",
        filetypes=[("ZIP 파일", "*.zip")]
    )
    zip_var.set(zip_file)


def select_word():
    global word_file
    word_file = filedialog.askopenfilename(
        title="Word 파일 선택",
        filetypes=[
    ("Word 파일", "*.doc *.docx"),
    ("모든 파일", "*.*")]
    )
    word_var.set(word_file)


def run():

    if zip_file == "":
        messagebox.showwarning("알림", "ZIP 파일을 선택하세요.")
        return

    if word_file == "":
        messagebox.showwarning("알림", "Word 파일을 선택하세요.")
        return

    temp_folder = tempfile.mkdtemp()

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(temp_folder)

    image_count = 0

    for root_path, dirs, files in os.walk(temp_folder):

        for file in files:

            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_count += 1

    image_files = []

    for root_path, dirs, files in os.walk(temp_folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(root_path, file))

    image_files.sort(
        key=lambda x: int(os.path.splitext(os.path.basename(x))[0])
    )

    if len(image_files) == 0:
        messagebox.showerror("오류", "사진을 찾을 수 없습니다.")
        return
        img = cv2.imread(image_files[0])

    h, w = img.shape[:2]

    crop = img[int(h*0.72):h, 0:w]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    print(text)

    cv2.imshow("하단", gray)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    

root = tk.Tk()
root.title("ROADM 자동 보고서")
root.geometry("700x260")
root.resizable(False, False)

zip_var = tk.StringVar()
word_var = tk.StringVar()

tk.Label(root, text="ZIP 파일").place(x=20, y=20)

tk.Entry(root, textvariable=zip_var, width=70).place(x=20, y=45)

tk.Button(root, text="찾아보기", command=select_zip).place(x=600, y=40)

tk.Label(root, text="Word 양식").place(x=20, y=90)

tk.Entry(root, textvariable=word_var, width=70).place(x=20, y=115)

tk.Button(root, text="찾아보기", command=select_word).place(x=600, y=110)

tk.Button(
    root,
    text="실행",
    width=20,
    height=2,
    command=run
).place(x=260, y=170)

root.mainloop()
