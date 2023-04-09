import tkinter as tk

root = tk.Tk() # tkというモジュールが持っている、Tkというクラスのオブジェクトを作成する
# Applicationの土台 windowのこと(root)
root.geometry("200x200") # windowの大きさを決めている

frame = tk.Frame(master=root) # Frame...windowの中のウィジェット(部品)をまとめる
frame.pack(expand=True, fill="both")# 親の大きさに合わせる

button = tk.Button(frame, text='Button', command=root.destroy)
button.place(x=80, y=80)

root.mainloop() # イベントループ アプリを起動する