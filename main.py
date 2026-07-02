import tkinter as tk
from tkinter import filedialog

# ----------------------------
# 함수
# ----------------------------

def select_zip():
    filename = filedialog.askopenfilename(
        title="ZIP 파일 선택",
        filetypes=[("ZIP 파일", "*.zip")]
    )
    zip_path.set(filename)


def select_word():
    filename = filedialog.askopenfilename(
        title="Word 파일 선택",
        filetypes=[("Word 파일", "*.docx")]
    )
    word_path.set(filename)


# ----------------------------
# 메인창
# ----------------------------

root = tk.Tk()
root.title("ROADM 자동 보고서")
root.geometry("700x300")
root.resizable(False, False)

zip_path = tk.StringVar()
word_path = tk.StringVar()

# ZIP
tk.Label(root, text="ZIP 파일").pack(anchor="w", padx=20, pady=(20, 5))

frame1 = tk.Frame(root)
frame1.pack(fill="x", padx=20)

tk.Entry(frame1, textvariable=zip_path).pack(side="left", fill="x", expand=True)

tk.Button(frame1, text="찾아보기", command=select_zip).pack(side="left", padx=5)

# WORD
tk.Label(root, text="Word 양식").pack(anchor="w", padx=20, pady=(15, 5))

frame2 = tk.Frame(root)
frame2.pack(fill="x", padx=20)

tk.Entry(frame2, textvariable=word_path).pack(side="left", fill="x", expand=True)

tk.Button(frame2, text="찾아보기", command=select_word).pack(side="left", padx=5)

# 실행 버튼
tk.Button(
    root,
    text="실행",
    width=20,
    height=2
).pack(pady=25)

status = tk.Label(root, text="상태 : 대기중")
status.pack()

root.mainloop()
