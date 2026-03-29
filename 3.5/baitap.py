class MayTinhToanTu:
    def __init__(self, so_a, so_b, so_c):
        self.a = so_a
        self.b = so_b
        self.c = so_c

    def tinh_so_hoc(self):
        print("\n--- 1. PHÉP TOÁN SỐ HỌC ---")
        print("Cộng a + b + c =", self.a + self.b + self.c)
        print("Trừ a - b =", self.a - self.b)
        print("Nhân b * c =", self.b * self.c)

        if self.c != 0:
            print("Chia a / c =", self.a / self.c)
        else:
            print("Không thể chia cho 0")

        print("Lũy thừa b mũ c =", self.b ** self.c)

        if self.b != 0:
            print("Chia lấy dư a % b =", self.a % self.b)
        else:
            print("Không thể chia lấy dư cho 0")

        print("-" * 30)

    def so_sanh(self):
        print("\n--- 2. TOÁN TỬ SO SÁNH ---")
        print("a > b ->", self.a > self.b)
        print("b < c ->", self.b < self.c)
        print("a == c ->", self.a == self.c)
        print("a != b ->", self.a != self.b)
        print("-" * 30)

    def phep_gan(self):
        print("\n--- 3. TOÁN TỬ GÁN ---")
        x = 10
        print("Giá trị x ban đầu =", x)

        x += self.b
        print("Sau x += b:", x)

        x *= 2
        print("Sau x *= 2:", x)
        print("-" * 30)

    def logic(self):
        print("\n--- 4. TOÁN TỬ LOGIC ---")
        dk1 = (self.a > self.b)
        dk2 = (self.b > self.c)

        print("a > b:", dk1)
        print("b > c:", dk2)
        print("AND:", dk1 and dk2)
        print("OR:", dk1 or dk2)
        print("NOT dk1:", not dk1)
        print("-" * 30)

    def thao_tac_bit(self):
        print("\n--- 5. THAO TÁC BIT ---")
        print("b & c =", self.b & self.c)
        print("b | c =", self.b | self.c)
        print("a << 3 =", self.a << 3)
        print("a >> 2 =", self.a >> 2)
        print("-" * 30)


# ================= MENU =================

def hien_menu():
    print("\n===== MENU MÁY TÍNH TOÁN TỬ =====")
    print("1. Phép toán số học")
    print("2. Toán tử so sánh")
    print("3. Toán tử gán")
    print("4. Toán tử logic")
    print("5. Thao tác bit")
    print("0. Thoát")


# ===== CHƯƠNG TRÌNH CHÍNH =====

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

may_tinh = MayTinhToanTu(a, b, c)

while True:
    hien_menu()
    chon = input("Chọn chức năng: ")

    if chon == "1":
        may_tinh.tinh_so_hoc()
    elif chon == "2":
        may_tinh.so_sanh()
    elif chon == "3":
        may_tinh.phep_gan()
    elif chon == "4":
        may_tinh.logic()
    elif chon == "5":
        may_tinh.thao_tac_bit()
    elif chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")