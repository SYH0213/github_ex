
import tkinter as tk

def on_click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# --- UI 설정 ---
window = tk.Tk()
window.title("계산기")

# 결과 표시줄
entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 버튼 리스트
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# 버튼 생성 및 배치
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: on_click(x)
    tk.Button(window, text=button, width=5, height=2, font=("Arial", 15), command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
