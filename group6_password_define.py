import tkinter as tk
from tkinter import messagebox

password_dung="@567890"
lanthutoida = 2
lanthu = 0


def dangnhap():
    global lanthu
    password = password_nhan.get()
    if password == password_dung:
        messagebox.showinfo("Thông báo", "Đăng nhập thành công")
        window.quit()
    elif lanthu == lanthutoida:
        messagebox.showwarning("Thông báo", "Số lần nhập sai quá giới hạn")
        window.quit()
    else:
        lanthu+=1
        messagebox.showwarning("Đã nhập sai mật khẩu.", f"Còn {lanthutoida-lanthu} lần thử ")
        password_nhan.delete()
    
window = tk.Tk()
window.title("Đăng nhập bảo mật")
window.geometry("250x200")

nhan = tk.Label(window, text="Nhập mật khẩu")
nhan.pack()
password_nhan = tk.Entry(window)
password_nhan.pack()
password_dangnhap = tk.Button(text='đăng nhập',command= dangnhap)
password_dangnhap.pack()

window.mainloop()