import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("ドロップダウンメニューの例")
root.attributes("-topmost", True)  # 他のウィンドウの上に表示
root.title("Task Schedule Overlay")
root.geometry("300x400")  # ウィンドウの初期サイズを設定
root.resizable(True, True)

#モンスターの選択
def Monster_select(event):
    global selcted_monster
    selected_monster=SM.get()
    Mlabel.config(text=f"{selected_monster}")
Mlabel=tk.Label(root,text="モンスターを選択してください")
Mlabel.pack(pady=10)
SM=ttk.Combobox(root,values=["ミラボレアス"])
SM.pack(pady=10)
SM.bind("<<ComboboxSelected>>", Monster_select)

#肉質の選択
def on_select(event):
    global selected_nikusitu
    selected_nikusitu = nikusitu.get()
    Nlabel.config(text=f"選択された値: {selected_nikusitu}")
# ラベルの作成
Nlabel= tk.Label(root, text="攻撃部位を選択してください")
Nlabel.pack(pady=10)
# ドロップダウンメニューの作成
nikusitu = ttk.Combobox(root, values=["head", "body", "arm","legs","tail"])
nikusitu.pack(pady=10)
# 選択イベントのバインド
nikusitu.bind("<<ComboboxSelected>>", on_select)

#武器種の選択
def get_select(event):
    global selcted_weatype
    selected_weatype=weatype.get()
    Hunter.config(text=f"{selected_weatype}")
    print(selected_weatype)
Hunter=tk.Label(root,text="武器種を選択してください")
Hunter.pack(pady=10)
weatype=ttk.Combobox(root,values=["片手剣","大剣","太刀","双剣","ガンランス","ランス","スラッシュアックス","チャージアックス","操虫棍"])
weatype.pack(pady=10)
weatype.bind("<<ComboboxSelected>>", get_select)


# メインループの開始
root.mainloop()
