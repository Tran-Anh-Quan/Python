import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk

# Thêm thư mục hiện tại vào sys.path để import các module local
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import Manager, Developer, Intern
from services.company import Company
from utils.validators import Validators
from utils.formatters import Formatters
from exceptions.employee_exceptions import EmployeeError

class EmployeeManagementApp:
    def __init__(self):
        self.company = Company()
        self.root = tk.Tk()
        self.root.title("Employee Management - Công ty ABC")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)

        self._build_form()
        self._build_table()
        self._build_footer()

    def _build_form(self):
        form_frame = ttk.LabelFrame(self.root, text="Thêm nhân viên")
        form_frame.pack(fill="x", padx=12, pady=10)

        ttk.Label(form_frame, text="ID").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="Tên").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="Tuổi").grid(row=0, column=4, padx=6, pady=6, sticky="w")
        ttk.Label(form_frame, text="Lương cơ bản").grid(row=0, column=6, padx=6, pady=6, sticky="w")

        self.emp_id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.salary_var = tk.StringVar()

        ttk.Entry(form_frame, textvariable=self.emp_id_var, width=14).grid(row=0, column=1, padx=6, pady=6)
        ttk.Entry(form_frame, textvariable=self.name_var, width=24).grid(row=0, column=3, padx=6, pady=6)
        ttk.Entry(form_frame, textvariable=self.age_var, width=8).grid(row=0, column=5, padx=6, pady=6)
        ttk.Entry(form_frame, textvariable=self.salary_var, width=14).grid(row=0, column=7, padx=6, pady=6)

        ttk.Label(form_frame, text="Loại").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        self.type_var = tk.StringVar(value="Manager")
        type_cb = ttk.Combobox(
            form_frame,
            textvariable=self.type_var,
            values=["Manager", "Developer", "Intern"],
            state="readonly",
            width=12,
        )
        type_cb.grid(row=1, column=1, padx=6, pady=6, sticky="w")
        type_cb.bind("<<ComboboxSelected>>", self._on_type_change)

        self.extra_label = ttk.Label(form_frame, text="Quy mô team")
        self.extra_label.grid(row=1, column=2, padx=6, pady=6, sticky="w")
        self.extra_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.extra_var, width=24).grid(row=1, column=3, padx=6, pady=6, sticky="w")

        self.score_var = tk.StringVar()
        ttk.Label(form_frame, text="Điểm hiệu suất (0-10)").grid(row=1, column=4, padx=6, pady=6, sticky="w")
        ttk.Entry(form_frame, textvariable=self.score_var, width=14).grid(row=1, column=5, padx=6, pady=6, sticky="w")

        ttk.Button(form_frame, text="Thêm nhân viên", command=self.add_employee).grid(row=1, column=6, padx=6, pady=6)
        ttk.Button(form_frame, text="Làm mới form", command=self.clear_form).grid(row=1, column=7, padx=6, pady=6)

        ttk.Separator(form_frame, orient="horizontal").grid(row=2, column=0, columnspan=8, sticky="ew", padx=6, pady=8)

        ttk.Label(form_frame, text="Tìm theo ID").grid(row=3, column=0, padx=6, pady=6, sticky="w")
        self.search_id_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.search_id_var, width=16).grid(row=3, column=1, padx=6, pady=6, sticky="w")
        ttk.Button(form_frame, text="Tìm", command=self.search_by_id).grid(row=3, column=2, padx=6, pady=6, sticky="w")
        ttk.Button(form_frame, text="Hiển thị tất cả", command=self.refresh_table).grid(row=3, column=3, padx=6, pady=6, sticky="w")
        ttk.Button(form_frame, text="Cập nhật điểm", command=self.update_performance).grid(row=3, column=4, padx=6, pady=6, sticky="w")
        ttk.Button(form_frame, text="Tổng lương", command=self.show_total_payroll).grid(row=3, column=5, padx=6, pady=6, sticky="w")

    def _build_table(self):
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=12, pady=4)

        columns = ("id", "name", "type", "age", "base_salary", "score", "salary", "projects", "extra")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Tên")
        self.tree.heading("type", text="Loại")
        self.tree.heading("age", text="Tuổi")
        self.tree.heading("base_salary", text="Lương cơ bản")
        self.tree.heading("score", text="Điểm HS")
        self.tree.heading("salary", text="Lương thực nhận")
        self.tree.heading("projects", text="Số dự án")
        self.tree.heading("extra", text="Thông tin thêm")

        self.tree.column("id", width=90, anchor="center")
        self.tree.column("name", width=180)
        self.tree.column("type", width=100, anchor="center")
        self.tree.column("age", width=70, anchor="center")
        self.tree.column("base_salary", width=130, anchor="e")
        self.tree.column("score", width=90, anchor="center")
        self.tree.column("salary", width=150, anchor="e")
        self.tree.column("projects", width=90, anchor="center")
        self.tree.column("extra", width=190)

        y_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=y_scroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        y_scroll.pack(side="right", fill="y")

    def _build_footer(self):
        self.status_var = tk.StringVar(value="Sẵn sàng")
        status_label = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_label.pack(fill="x", padx=12, pady=(2, 10))

    def _on_type_change(self, _event=None):
        emp_type = self.type_var.get()
        if emp_type == "Manager":
            self.extra_label.config(text="Quy mô team")
        elif emp_type == "Developer":
            self.extra_label.config(text="Ngôn ngữ")
        else:
            self.extra_label.config(text="Chuyên ngành")

    def _build_employee_from_form(self):
        emp_id = self.emp_id_var.get().strip()
        name = self.name_var.get().strip()
        age = int(self.age_var.get().strip())
        base_salary = float(self.salary_var.get().strip())
        extra = self.extra_var.get().strip()

        if not emp_id or not name or not extra:
            raise ValueError("ID, tên và thông tin thêm không được để trống")

        Validators.validate_age(age)
        Validators.validate_salary(base_salary)

        emp_type = self.type_var.get()
        if emp_type == "Manager":
            team_size = int(extra)
            if team_size < 0:
                raise ValueError("Quy mô team không được âm")
            employee = Manager(emp_id, name, age, base_salary, team_size)
        elif emp_type == "Developer":
            employee = Developer(emp_id, name, age, base_salary, extra)
        else:
            employee = Intern(emp_id, name, age, base_salary, extra)

        score_txt = self.score_var.get().strip()
        if score_txt:
            employee.performance_score = float(score_txt)

        return employee

    def add_employee(self):
        try:
            employee = self._build_employee_from_form()
            self.company.add_employee(employee)
            self.refresh_table()
            self.status_var.set(f"Đã thêm nhân viên {employee.emp_id}")
            self.clear_form(keep_type=True)
            messagebox.showinfo("Thành công", "Đã thêm nhân viên thành công")
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi nhập liệu", str(exc))

    def clear_form(self, keep_type=False):
        self.emp_id_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.salary_var.set("")
        self.extra_var.set("")
        self.score_var.set("")
        if not keep_type:
            self.type_var.set("Manager")
            self._on_type_change()

    def _employee_extra_text(self, employee):
        if isinstance(employee, Manager):
            return f"Team: {employee.team_size}"
        if isinstance(employee, Developer):
            return f"Ngôn ngữ: {employee.programming_language}"
        return f"Chuyên ngành: {employee.major}"

    def _insert_employee(self, employee):
        self.tree.insert(
            "",
            "end",
            values=(
                employee.emp_id,
                employee.name,
                employee.__class__.__name__,
                employee.age,
                Formatters.format_currency(employee.base_salary),
                f"{employee.performance_score:.1f}",
                Formatters.format_currency(employee.calculate_salary()),
                len(employee.projects),
                self._employee_extra_text(employee),
            ),
        )

    def refresh_table(self):
        for row_id in self.tree.get_children():
            self.tree.delete(row_id)
        for employee in self.company.get_all_employees():
            self._insert_employee(employee)
        self.status_var.set(f"Tổng nhân viên: {len(self.company.get_all_employees())}")

    def search_by_id(self):
        emp_id = self.search_id_var.get().strip()
        if not emp_id:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập ID để tìm")
            return
        try:
            employee = self.company.find_employee_by_id(emp_id)
            for row_id in self.tree.get_children():
                self.tree.delete(row_id)
            self._insert_employee(employee)
            self.status_var.set(f"Đã tìm thấy nhân viên {emp_id}")
        except EmployeeError as exc:
            messagebox.showerror("Không tìm thấy", str(exc))

    def update_performance(self):
        emp_id = self.search_id_var.get().strip()
        score_txt = self.score_var.get().strip()
        if not emp_id or not score_txt:
            messagebox.showwarning("Thiếu dữ liệu", "Cần nhập ID (ô tìm kiếm) và điểm hiệu suất")
            return
        try:
            employee = self.company.find_employee_by_id(emp_id)
            employee.performance_score = float(score_txt)
            self.refresh_table()
            self.status_var.set(f"Đã cập nhật điểm cho {emp_id}")
            messagebox.showinfo("Thành công", "Đã cập nhật điểm hiệu suất")
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi", str(exc))

    def show_total_payroll(self):
        total = self.company.calculate_total_payroll()
        messagebox.showinfo("Tổng lương công ty", f"Tổng lương hiện tại: {Formatters.format_currency(total)}")
        self.status_var.set(f"Tổng lương: {Formatters.format_currency(total)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EmployeeManagementApp()
    app.run()
