class BaiTapCoBan:


    def bai1(self):
        print("\n===== BÀI 1: TÍNH TỔNG 2 SỐ NGUYÊN =====")
        try:
            a = int(input("Nhập số thứ nhất: "))
            b = int(input("Nhập số thứ hai: "))
            print("Tổng =", a + b)
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")

   
    def bai2(self):
        print("\n===== BÀI 2: IN CHUỖI =====")
        chuoi = input("Nhập chuỗi ký tự: ")
        print("Chuỗi vừa nhập:", chuoi)

    
    def bai3(self):
        print("\n===== BÀI 3: TÍNH TOÁN 3 SỐ NGUYÊN =====")
        try:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            c = int(input("Nhập c: "))

            # a) Tổng
            print("Tổng 3 số =", a + b + c)

            # b) Hiệu (a - b)
            print("Hiệu a - b =", a - b)

            # c) Phép chia (a chia b)
            if b != 0:
                print("Chia nguyên (a // b) =", a // b)
                print("Chia dư (a % b) =", a % b)
                print("Chia chính xác (a / b) =", a / b)
            else:
                print("Không thể chia cho 0")

        except ValueError:
            print("Lỗi: Phải nhập số nguyên!")

    
    def bai4(self):
        print("\n===== BÀI 4: GHÉP CHUỖI =====")
        s1 = input("Nhập chuỗi 1: ")
        s2 = input("Nhập chuỗi 2: ")
        s3 = input("Nhập chuỗi 3: ")
        print("Kết quả:", f"{s1} {s2} {s3}")

    # ===== BÀI 5 =====
    def bai5(self):
        print("\n===== BÀI 5: HÌNH TRÒN =====")
        try:
            R = float(input("Nhập bán kính: "))
            if R <= 0:
                print("Bán kính phải > 0")
                return

            pi = 3.14
            chu_vi = 2 * pi * R
            dien_tich = pi * R * R

            print("Chu vi =", chu_vi)
            print("Diện tích =", dien_tich)

        except ValueError:
            print("Lỗi: Phải nhập số!")

    # ===== MENU =====
    def menu(self):
        while True:
            print("\n========== MENU ==========")
            print("1. Bài 1 - Tính tổng 2 số")
            print("2. Bài 2 - In chuỗi")
            print("3. Bài 3 - Tính toán 3 số")
            print("4. Bài 4 - Ghép chuỗi")
            print("5. Bài 5 - Hình tròn")
            print("0. Thoát")

            chon = input("Chọn chức năng: ")

            if chon == "1":
                self.bai1()
            elif chon == "2":
                self.bai2()
            elif chon == "3":
                self.bai3()
            elif chon == "4":
                self.bai4()
            elif chon == "5":
                self.bai5()
            elif chon == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ!")

chuong_trinh = BaiTapCoBan()
chuong_trinh.menu()