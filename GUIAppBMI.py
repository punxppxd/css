# การพัฒนาแอปพลิเคชันด้วย Tkinter GUI
# โปรแกรมคำนวณค่าดัชนีมวลกาย (BMI)
# ปรับปรุง: ตรวจสอบข้อมูล, รองรับทศนิยม, แสดงผลเป็นระเบียบ,
# ปุ่มล้างข้อมูล, กด Enter เพื่อคำนวณ และป้องกันโปรแกรมหยุดเมื่อกรอกข้อมูลผิด

import tkinter as tk
from tkinter import ttk, messagebox


# -----------------------------
# ฟังก์ชันคำนวณ BMI
# -----------------------------
def calculate_bmi():
    name = name_var.get().strip()

    try:
        height_cm = float(height_var.get())
        weight_kg = float(weight_var.get())

        if not name:
            messagebox.showwarning("ข้อมูลไม่ครบ", "กรุณากรอกชื่อและนามสกุล")
            name_entry.focus()
            return

        if height_cm <= 0:
            messagebox.showwarning("ข้อมูลไม่ถูกต้อง", "ส่วนสูงต้องมากกว่า 0 เซนติเมตร")
            height_entry.focus()
            return

        if weight_kg <= 0:
            messagebox.showwarning("ข้อมูลไม่ถูกต้อง", "น้ำหนักต้องมากกว่า 0 กิโลกรัม")
            weight_entry.focus()
            return

        # แปลงส่วนสูงจากเซนติเมตรเป็นเมตร
        height_m = height_cm / 100

        # สูตร BMI = น้ำหนัก(kg) / ส่วนสูง(m)^2
        bmi = weight_kg / (height_m ** 2)

        # เกณฑ์การแปลผลตามโจทย์เดิม
        if bmi < 18.50:
            result = "น้ำหนักต่ำกว่าเกณฑ์"
        elif bmi < 23.00:
            result = "รูปร่างสมส่วน"
        elif bmi < 25.00:
            result = "ภาวะน้ำหนักเกิน"
        elif bmi < 30.00:
            result = "โรคอ้วน"
        else:
            result = "โรคอ้วนระดับสูง ควรปรึกษาแพทย์ผู้เชี่ยวชาญ"

        bmi_result_var.set(f"BMI = {bmi:.2f}")
        status_result_var.set(f"ผลการประเมิน: {result}")

    except ValueError:
        messagebox.showerror(
            "ข้อมูลไม่ถูกต้อง",
            "กรุณากรอกส่วนสูงและน้ำหนักเป็นตัวเลข เช่น 170 หรือ 65.5"
        )


# -----------------------------
# ฟังก์ชันล้างข้อมูล
# -----------------------------
def clear_form():
    name_var.set("")
    height_var.set("")
    weight_var.set("")
    bmi_result_var.set("BMI = -")
    status_result_var.set("ผลการประเมิน: -")
    name_entry.focus()


# -----------------------------
# สร้างหน้าต่างหลัก
# -----------------------------
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("560x500")
window.resizable(False, False)

# -----------------------------
# ตัวแปร
# -----------------------------
name_var = tk.StringVar()
height_var = tk.StringVar()
weight_var = tk.StringVar()
bmi_result_var = tk.StringVar(value="BMI = -")
status_result_var = tk.StringVar(value="ผลการประเมิน: -")

# -----------------------------
# Style
# -----------------------------
style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass

style.configure("Title.TLabel", font=("Tahoma", 20, "bold"))
style.configure("Label.TLabel", font=("Tahoma", 11))
style.configure("Result.TLabel", font=("Tahoma", 18, "bold"))
style.configure("Status.TLabel", font=("Tahoma", 12, "bold"))

# -----------------------------
# ส่วนหัว
# -----------------------------
main_frame = ttk.Frame(window, padding=25)
main_frame.pack(fill="both", expand=True)

ttk.Label(
    main_frame,
    text="โปรแกรมคำนวณดัชนีมวลกาย (BMI)",
    style="Title.TLabel"
).pack(pady=(0, 20))

# -----------------------------
# แบบฟอร์ม
# -----------------------------
form_frame = ttk.Frame(main_frame)
form_frame.pack(fill="x")

ttk.Label(form_frame,
          text="ชื่อ - นามสกุล",
          style="Label.TLabel").grid(row=0, column=0, sticky="w", pady=8)

name_entry = ttk.Entry(
    form_frame,
    textvariable=name_var,
    width=35,
    font=("Tahoma", 11))

name_entry.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=(15, 0),
    pady=8)

ttk.Label(
    form_frame,
    text="ส่วนสูง (ซม.)",
    style="Label.TLabel").grid(row=1, column=0, sticky="w", pady=8)

height_entry = ttk.Entry(
    form_frame,
    textvariable=height_var,
    width=35,
    font=("Tahoma", 11))
height_entry.grid(row=1, column=1, sticky="ew", padx=(15, 0), pady=8)

ttk.Label(
    form_frame,
    text="น้ำหนัก (กก.)",
    style="Label.TLabel").grid(row=2, column=0, sticky="w", pady=8)

weight_entry = ttk.Entry(
    form_frame,
    textvariable=weight_var,
    width=35,
    font=("Tahoma", 11))
weight_entry.grid(row=2, column=1, sticky="ew", padx=(15, 0), pady=8)

form_frame.columnconfigure(1, weight=1)

# -----------------------------
# ปุ่มคำสั่ง
# -----------------------------
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

ttk.Button(
    button_frame,
    text="คำนวณ BMI",
    command=calculate_bmi).grid(row=0, column=0, padx=8)

ttk.Button(
    button_frame,
    text="ล้างข้อมูล",
    command=clear_form).grid(row=0, column=1, padx=8)

# -----------------------------
# ส่วนแสดงผล
# -----------------------------
result_frame = ttk.LabelFrame(
    main_frame,
    text="ผลการคำนวณ",
    padding=20)
result_frame.pack(fill="x", pady=5)

ttk.Label(
    result_frame,
    textvariable=bmi_result_var,
    style="Result.TLabel").pack(pady=5)

ttk.Label(
    result_frame,
    textvariable=status_result_var,
    style="Status.TLabel",
    wraplength=450,
    justify="center").pack(pady=5)

ttk.Label(
    main_frame,
    text="หมายเหตุ: ใช้ส่วนสูงเป็นเซนติเมตร และน้ำหนักเป็นกิโลกรัม",
    style="Label.TLabel").pack(pady=(15, 0))

# กด Enter เพื่อคำนวณ
window.bind("<Return>", lambda event: calculate_bmi())

# เริ่มต้นที่ช่องชื่อ
name_entry.focus()

window.mainloop()
