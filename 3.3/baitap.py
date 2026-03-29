import time
import math

class BaiTap:

    def bai1(self):
        n = int(input("Nhập một số nguyên dương: "))

        if n % 2 == 0:
            print("Đây là một số chẵn")
        else:
            print("Đây là một số lẻ")

    def bai2(self):
        a = int(input("Nhập cạnh a: "))
        b = int(input("Nhập cạnh b: "))
        c = int(input("Nhập cạnh c: "))

        if a + b > c and a + c > b and b + c > a:
            print("Đây là độ dài ba cạnh của một tam giác")
        else:
            print("Đây không phải độ dài ba cạnh tam giác")

    def bai3(self):
        nam_sinh = int(input("Nhập năm sinh: "))

        x = time.localtime()
        nam_hien_tai = x[0]

        tuoi = nam_hien_tai - nam_sinh

        print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")

    # ===== BÀI 4 =====
    def bai4(self):
        n = int(input("Nhập một số nguyên dương: "))

        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        chia2 = (n % 2 == 0)
        chia3 = (n % 3 == 0)

        if chia2 and chia3:
            print(f"{n} chia hết cho cả 2 và 3")
        elif chia2:
            print(f"{n} chia hết cho 2")
        elif chia3:
            print(f"{n} chia hết cho 3")
        else:
            print(f"{n} không chia hết cho 2 và 3")

    # ===== BÀI 5 =====
    def bai5(self):
        print("Giải phương trình bậc 2: ax^2 + bx + c = 0")

        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: "))

        if a == 0:
            print("Đây không phải phương trình bậc 2")
            return

        delta = b*b - 4*a*c
        print("Delta =", delta)

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Phương trình có 2 nghiệm phân biệt:")
            print("x1 =", x1)
            print("x2 =", x2)

        elif delta == 0:
            x = -b / (2*a)
            print("Phương trình có nghiệm kép:")
            print("x =", x)

        else:
            print("Phương trình vô nghiệm (trong tập số thực)")

    def menu(self):
        while True:
            print("\n========= MENU =========")
            print("1. Kiểm tra số chẵn / lẻ")
            print("2. Kiểm tra 3 cạnh tam giác")
            print("3. Tính tuổi")
            print("4. Kiểm tra chia hết cho 2 và 3")
            print("5. Giải phương trình bậc 2")
            print("0. Thoát")
            print("========================")

            choice = input("Chọn bài: ")

            if choice == "1":
                self.bai1()
            elif choice == "2":
                self.bai2()
            elif choice == "3":
                self.bai3()
            elif choice == "4":
                self.bai4()
            elif choice == "5":
                self.bai5()
            elif choice == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ!")


# ===== CHẠY CHƯƠNG TRÌNH =====
if __name__ == "__main__":
    app = BaiTap()
    app.menu()