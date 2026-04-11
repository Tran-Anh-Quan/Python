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
from exceptions.employee_exceptions import EmployeeError, DuplicateEmployeeError

class EmployeeManagementApp:
    def __init__(self):
        self.company = Company()
        self.root = tk.Tk()
        self.root.title("Employee Management - Công ty ABC")
        self.root.geometry("1320x820")
        self.root.minsize(1180, 720)

        self._setup_style()

        self._load_sample_data()
        self._build_header()
        self._build_notebook()
        self._build_table()
        self._build_footer()
        self.refresh_table()

    def _setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        self.root.configure(bg="#f5f7fb")

        style.configure("App.TFrame", background="#f5f7fb")
        style.configure("Card.TLabelframe", background="#ffffff", padding=12)
        style.configure("Card.TLabelframe.Label", background="#ffffff", foreground="#1f2937", font=("Segoe UI", 10, "bold"))
        style.configure("Header.TLabel", background="#f5f7fb", foreground="#0f172a", font=("Segoe UI", 18, "bold"))
        style.configure("SubHeader.TLabel", background="#f5f7fb", foreground="#475569", font=("Segoe UI", 10))
        style.configure("Accent.TButton", padding=(12, 7), font=("Segoe UI", 9, "bold"))
        style.configure("TNotebook", background="#f5f7fb", borderwidth=0)
        style.configure("TNotebook.Tab", padding=(14, 8), font=("Segoe UI", 9, "bold"))
        style.configure("Treeview", rowheight=28, font=("Segoe UI", 9))
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))

    def _build_header(self):
        header = ttk.Frame(self.root, style="App.TFrame")
        header.pack(fill="x", padx=16, pady=(14, 8))

        ttk.Label(header, text="Employee Management", style="Header.TLabel").pack(anchor="w")
        ttk.Label(header, text="", style="SubHeader.TLabel").pack(anchor="w", pady=(2, 0))

    def _load_sample_data(self):
        sample_employees = [
            Manager("NV001", "Nguyen Van An", 35, 30000000, 8),
            Developer("NV002", "Tran Minh Khoa", 28, 22000000, "Python"),
            Intern("NV003", "Le Thu Ha", 24, 12000000, "Khoa hoc may tinh"),
            Developer("NV004", "Pham Quoc Bao", 31, 25000000, "Java"),
            Manager("NV005", "Vo Thanh Huong", 40, 32000000, 12),
        ]

        performance_scores = {
            "NV001": 9.2,
            "NV002": 8.5,
            "NV003": 7.8,
            "NV004": 8.9,
            "NV005": 9.5,
        }

        sample_projects = {
            "NV001": ["ERP Migration", "Hiring Plan"],
            "NV002": ["Payroll API", "Auth Service"],
            "NV003": ["QA Support"],
            "NV004": ["CRM Refactor", "Report Module"],
            "NV005": ["Digital Transformation", "Budget 2026"],
        }

        for employee in sample_employees:
            employee.performance_score = performance_scores[employee.emp_id]
            for project_name in sample_projects.get(employee.emp_id, []):
                employee.add_project(project_name)
            self.company.add_employee(employee)

    def _build_notebook(self):
        notebook_frame = ttk.Frame(self.root, style="App.TFrame")
        notebook_frame.pack(fill="x", padx=16, pady=(0, 10))

        notebook = ttk.Notebook(notebook_frame)
        notebook.pack(fill="x")

        self.employee_tab = ttk.Frame(notebook, style="App.TFrame")
        self.project_tab = ttk.Frame(notebook, style="App.TFrame")
        self.hr_tab = ttk.Frame(notebook, style="App.TFrame")

        notebook.add(self.employee_tab, text="Nhân viên")
        notebook.add(self.project_tab, text="Dự án")
        notebook.add(self.hr_tab, text="Nhân sự")

        self._build_employee_section(self.employee_tab)
        self._build_project_section(self.project_tab)
        self._build_hr_section(self.hr_tab)

    def _build_employee_section(self, parent):
        card = ttk.LabelFrame(parent, text="Thông tin nhân viên", style="Card.TLabelframe")
        card.pack(fill="x", padx=10, pady=10)

        self.emp_id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.salary_var = tk.StringVar()
        self.score_var = tk.StringVar()
        self.type_var = tk.StringVar(value="Manager")
        self.extra_var = tk.StringVar()
        self.search_id_var = tk.StringVar()

        self._add_labeled_entry(card, "ID", self.emp_id_var, 0, 0, 1, 14)
        self._add_labeled_entry(card, "Tên", self.name_var, 0, 2, 3, 24)
        self._add_labeled_entry(card, "Tuổi", self.age_var, 0, 4, 5, 10)
        self._add_labeled_entry(card, "Lương cơ bản", self.salary_var, 0, 6, 7, 16)

        ttk.Label(card, text="Loại").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        type_cb = ttk.Combobox(card, textvariable=self.type_var, values=["Manager", "Developer", "Intern"], state="readonly", width=12)
        type_cb.grid(row=1, column=1, padx=6, pady=6, sticky="w")
        type_cb.bind("<<ComboboxSelected>>", self._on_type_change)

        self.extra_label = ttk.Label(card, text="Quy mô team")
        self.extra_label.grid(row=1, column=2, padx=6, pady=6, sticky="w")
        ttk.Entry(card, textvariable=self.extra_var, width=24).grid(row=1, column=3, padx=6, pady=6, sticky="w")

        ttk.Label(card, text="Điểm hiệu suất").grid(row=1, column=4, padx=6, pady=6, sticky="w")
        ttk.Entry(card, textvariable=self.score_var, width=10).grid(row=1, column=5, padx=6, pady=6, sticky="w")

        ttk.Button(card, text="Thêm nhân viên", style="Accent.TButton", command=self.add_employee).grid(row=1, column=6, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Làm mới", command=self.clear_form).grid(row=1, column=7, padx=6, pady=6, sticky="w")

        ttk.Separator(card, orient="horizontal").grid(row=2, column=0, columnspan=8, sticky="ew", padx=6, pady=10)

        ttk.Label(card, text="Tìm / chọn ID").grid(row=3, column=0, padx=6, pady=6, sticky="w")
        ttk.Entry(card, textvariable=self.search_id_var, width=16).grid(row=3, column=1, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Tìm", command=self.search_by_id).grid(row=3, column=2, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Hiển thị tất cả", command=self.refresh_table).grid(row=3, column=3, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Cập nhật điểm", command=self.update_performance).grid(row=3, column=4, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Tổng lương", command=self.show_total_payroll).grid(row=3, column=5, padx=6, pady=6, sticky="w")

    def _build_project_section(self, parent):
        card = ttk.LabelFrame(parent, text="Quản lý dự án", style="Card.TLabelframe")
        card.pack(fill="x", padx=10, pady=10)

        self.project_var = tk.StringVar()

        self._add_labeled_entry(card, "Tên dự án", self.project_var, 0, 0, 1, 28)
        ttk.Button(card, text="Gán dự án", style="Accent.TButton", command=self.assign_project).grid(row=0, column=2, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="DS theo dự án", command=self.show_employees_by_project).grid(row=0, column=3, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="Sắp xếp theo số dự án", command=self.sort_by_project_count).grid(row=0, column=4, padx=6, pady=6, sticky="w")
        ttk.Button(card, text="DS tham gia dự án", command=self.show_project_participants).grid(row=0, column=5, padx=6, pady=6, sticky="w")

    def _build_hr_section(self, parent):
        card = ttk.LabelFrame(parent, text="Nhân sự & lương", style="Card.TLabelframe")
        card.pack(fill="x", padx=10, pady=10)

        self.days_without_work_var = tk.StringVar(value="0")
        self.days_notice_violation_var = tk.StringVar(value="0")
        self.compensation_var = tk.StringVar()
        self.deduction_var = tk.StringVar()

        self._add_labeled_entry(card, "Số ngày bị đình chỉ công việc", self.days_without_work_var, 0, 0, 1, 16)
        self._add_labeled_entry(card, "Số ngày vi phạm báo trước", self.days_notice_violation_var, 0, 2, 3, 16)
        self._add_labeled_entry(card, "Tổng bồi thường dự kiến (VNĐ)", self.compensation_var, 0, 4, 5, 18, readonly=True)
        ttk.Button(card, text="Cho nghỉ việc", style="Accent.TButton", command=self.terminate_employee).grid(row=0, column=6, padx=6, pady=6, sticky="w")

        self._add_labeled_entry(card, "Giảm lương", self.deduction_var, 1, 0, 1, 16)
        ttk.Button(card, text="Áp dụng giảm", style="Accent.TButton", command=self.reduce_salary).grid(row=1, column=2, padx=6, pady=6, sticky="w")

    def _add_labeled_entry(self, parent, label, variable, row, label_col, entry_col, width, readonly=False):
        ttk.Label(parent, text=label).grid(row=row, column=label_col, padx=6, pady=6, sticky="w")
        entry = ttk.Entry(parent, textvariable=variable, width=width)
        if readonly:
            entry.configure(state="readonly")
        entry.grid(row=row, column=entry_col, padx=6, pady=6, sticky="w")
        return entry

    def _build_table(self):
        table_frame = ttk.Frame(self.root, style="App.TFrame")
        table_frame.pack(fill="both", expand=True, padx=16, pady=(0, 8))

        table_card = ttk.LabelFrame(table_frame, text="Danh sách nhân viên", style="Card.TLabelframe")
        table_card.pack(fill="both", expand=True)

        columns = ("id", "name", "type", "age", "base_salary", "score", "salary", "projects", "extra")
        self.tree = ttk.Treeview(table_card, columns=columns, show="headings")

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

        y_scroll = ttk.Scrollbar(table_card, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=y_scroll.set)
        self.tree.bind("<<TreeviewSelect>>", self.on_employee_selected)

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
        extra = self.extra_var.get().strip()

        if not emp_id or not name or not extra:
            raise ValueError("ID, tên và thông tin thêm không được để trống")

        try:
            age = int(self.age_var.get().strip())
        except ValueError:
            raise ValueError("Tuổi phải là số nguyên hợp lệ")

        try:
            base_salary = float(self.salary_var.get().strip())
        except ValueError:
            raise ValueError("Lương cơ bản phải là số hợp lệ")

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
        except DuplicateEmployeeError as exc:
            messagebox.showerror("Trùng mã nhân viên", f"{exc}\nHãy đổi ID hoặc bấm 'Làm mới' để nhập nhân viên mới.")
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi nhập liệu", str(exc))

    def clear_form(self, keep_type=False):
        self.emp_id_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.salary_var.set("")
        self.extra_var.set("")
        self.score_var.set("")
        self.project_var.set("")
        self.compensation_var.set("")
        self.days_without_work_var.set("0")
        self.days_notice_violation_var.set("0")
        self.deduction_var.set("")
        if hasattr(self, "tree"):
            self.tree.selection_remove(self.tree.selection())
        if not keep_type:
            self.type_var.set("Manager")
            self._on_type_change()
        self.emp_id_var.set("")

    def _employee_extra_text(self, employee):
        if isinstance(employee, Manager):
            return f"Team: {employee.team_size}"
        if isinstance(employee, Developer):
            return f"Ngôn ngữ: {employee.programming_language}"
        return f"Chuyên ngành: {employee.major}"

    def on_employee_selected(self, _event=None):
        selected_items = self.tree.selection()
        if not selected_items:
            return

        item_id = selected_items[0]
        values = self.tree.item(item_id, "values")
        if not values:
            return

        emp_id = values[0]
        try:
            employee = self.company.find_employee_by_id(emp_id)
        except EmployeeError:
            return

        self.emp_id_var.set(employee.emp_id)
        self.name_var.set(employee.name)
        self.age_var.set(str(employee.age))
        if isinstance(employee.base_salary, float) and employee.base_salary.is_integer():
            self.salary_var.set(str(int(employee.base_salary)))
        else:
            self.salary_var.set(str(employee.base_salary))
        self.score_var.set(f"{employee.performance_score:.1f}")
        self.search_id_var.set(employee.emp_id)

        if isinstance(employee, Manager):
            self.type_var.set("Manager")
            self._on_type_change()
            self.extra_var.set(str(employee.team_size))
        elif isinstance(employee, Developer):
            self.type_var.set("Developer")
            self._on_type_change()
            self.extra_var.set(employee.programming_language)
        else:
            self.type_var.set("Intern")
            self._on_type_change()
            self.extra_var.set(employee.major)

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

    def _render_employees(self, employees, status_message):
        for row_id in self.tree.get_children():
            self.tree.delete(row_id)
        for employee in employees:
            self._insert_employee(employee)
        self.status_var.set(status_message)

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

    def assign_project(self):
        emp_id = self.search_id_var.get().strip()
        project_name = self.project_var.get().strip()
        if not emp_id or not project_name:
            messagebox.showwarning("Thiếu dữ liệu", "Cần nhập ID (ô tìm kiếm) và tên dự án")
            return
        try:
            employee = self.company.find_employee_by_id(emp_id)
            employee.add_project(project_name)
            self.refresh_table()
            self.status_var.set(f"Đã gán dự án cho {emp_id}")
            messagebox.showinfo("Thành công", f"Đã gán dự án '{project_name}'")
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi", str(exc))

    def show_employees_by_project(self):
        project_name = self.project_var.get().strip()
        if not project_name:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên dự án")
            return
        try:
            employees = self.company.get_employees_by_project(project_name)
            self._render_employees(employees, f"Dự án '{project_name}': {len(employees)} nhân viên")
        except EmployeeError as exc:
            messagebox.showerror("Không tìm thấy", str(exc))

    def sort_by_project_count(self):
        employees = self.company.get_employees_sorted_by_projects()
        self._render_employees(employees, "Đã sắp xếp theo số dự án (giảm dần)")

    def show_project_participants(self):
        try:
            employees = self.company.get_project_participants()
            self._render_employees(employees, f"Nhân viên tham gia dự án: {len(employees)}")
        except EmployeeError as exc:
            messagebox.showerror("Không có dữ liệu", str(exc))

    def terminate_employee(self):
        emp_id = self.search_id_var.get().strip()
        days_without_work_txt = self.days_without_work_var.get().strip()
        days_notice_violation_txt = self.days_notice_violation_var.get().strip()
        if not emp_id:
            messagebox.showwarning("Thiếu dữ liệu", "Cần nhập ID nhân viên ở ô tìm kiếm")
            return
        try:
            days_without_work = int(days_without_work_txt) if days_without_work_txt else 0
            days_notice_violation = int(days_notice_violation_txt) if days_notice_violation_txt else 0
            employee = self.company.find_employee_by_id(emp_id)
            compensation = self.company.calculate_termination_compensation(
                employee,
                days_without_work,
                days_notice_violation,
            )
            employee = self.company.terminate_employee(emp_id, days_without_work, days_notice_violation)
            self.refresh_table()
            self.compensation_var.set(Formatters.format_currency(compensation))
            message = (
                f"Đã cho nghỉ việc {employee.name} ({employee.emp_id}). "
                f"Đền bù: {Formatters.format_currency(compensation)}"
            )
            self.status_var.set(message)
            messagebox.showinfo("Thành công", message)
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi", str(exc))

    def reduce_salary(self):
        emp_id = self.search_id_var.get().strip()
        deduction_txt = self.deduction_var.get().strip()
        if not emp_id or not deduction_txt:
            messagebox.showwarning("Thiếu dữ liệu", "Cần nhập ID (ô tìm kiếm) và số tiền giảm lương")
            return
        try:
            deduction = float(deduction_txt)
            employee = self.company.reduce_salary(emp_id, deduction)
            self.refresh_table()
            message = f"Đã giảm lương {employee.emp_id} còn {Formatters.format_currency(employee.base_salary)}"
            self.status_var.set(message)
            messagebox.showinfo("Thành công", message)
        except (EmployeeError, ValueError) as exc:
            messagebox.showerror("Lỗi", str(exc))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EmployeeManagementApp()
    app.run()
