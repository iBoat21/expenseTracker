# 💰 Expense Tracker (CLI)

โปรแกรมบันทึกรายรับ-รายจ่ายผ่าน Command Line Interface (CLI) พัฒนาด้วยภาษา Python โดยใช้หลักการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming: OOP) พร้อมระบบบันทึกข้อมูลลงไฟล์ Text อัตโนมัติ

---

## 📌 ฟีเจอร์หลัก (Features)
* บันทึกรายการ **รายรับ (Income)** และ **รายจ่าย (Expense)**
* กำหนดหมวดหมู่ ยอดเงิน และเลือกวันที่ทำรายการได้ (ตั้งค่าเริ่มต้นเป็นวันที่ปัจจุบันอัตโนมัติ)
* ระบบตรวจสอบความถูกต้องของข้อมูล (Validate ยอดเงินต้องมากกว่า 0)
* สรุปรายงานการเงิน: ยอดรายรับรวม, รายจ่ายรวม และยอดเงินคงเหลือสุทธิ (Net Balance)
* ระบบจัดเก็บและโหลดข้อมูลจากไฟล์ `expenseList.txt` (Data Persistence)

---

## 🏗️ โครงสร้างคลาส (Class Design)

### 1. `Class Transaction`
โมเดลข้อมูลสำหรับธุรกรรม 1 รายการ
* **Attributes:** `type_str`, `category`, `amount`, `date_time`
* **Method:** `to_text()` สำหรับจัดฟอร์แมตข้อมูลเตรียมบันทึกลงไฟล์

### 2. `Class ExpenseTracker`
ตัวควบคุมระบบจัดการข้อมูลการเงิน
* **Attributes:** `file_name`, `transactions`
* **Methods:**
  * `add_transaction()`: ตรวจสอบและเพิ่มรายการใหม่
  * `show_report()`: แสดงประวัติและสรุปยอดคงเหลือสุทธิ
  * `save_to_file()`: บันทึกข้อมูลลงไฟล์
  * `load_from_file()`: โหลดข้อมูลเดิมขึ้นมาเมื่อเปิดโปรแกรม

---

## 🚀 วิธีการติดตั้งและรันโปรแกรม (Getting Started)

### ความต้องการของระบบ (Prerequisites)
* Python 3.10 ขึ้นไป (เนื่องจากมีการใช้ฟีเจอร์ `match-case`)

### ขั้นตอนการรัน
1. Clone repository หรือดาวน์โหลดไฟล์:
   ```bash
   git clone [https://github.com/your-username/expense-tracker.git](https://github.com/your-username/expense-tracker.git)
   cd expense-tracker