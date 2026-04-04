# ============================================================
#              1.9 LUYỆN TẬP - BÀI TẬP VỀ LIST
# ============================================================

def bai_1():
    print("=" * 50)
    print("BÀI 1: Tính tổng các phần tử trong list")
    print("=" * 50)
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tong = 0
    for phan_tu in _list:
        tong += phan_tu
    print(f"List: {_list}")
    print(f"Tổng = {tong}")

def bai_2():
    print("\n" + "=" * 50)
    print("BÀI 2: Tính tích các phần tử trong list")
    print("=" * 50)
    _list = [1, 2, 3, 4, 5]
    tich = 1
    for phan_tu in _list:
        tich *= phan_tu
    print(f"List: {_list}")
    print(f"Tích = {tich}")

def bai_3():
    print("\n" + "=" * 50)
    print("BÀI 3: Tách list thành list số chẵn và số lẻ")
    print("=" * 50)
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even = []
    odd = []
    for phan_tu in _list:
        if phan_tu % 2 == 0:
            even.append(phan_tu)
        else:
            odd.append(phan_tu)
    print(f"List gốc : {_list}")
    print(f"Số chẵn  : {even}")
    print(f"Số lẻ    : {odd}")

def bai_4():
    print("\n" + "=" * 50)
    print("BÀI 4: Lấy phần tử vị trí thứ 2 và thứ 3")
    print("=" * 50)
    _list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    _new = _list[2:4]
    print(f"List gốc : {_list}")
    print(f"List mới : {_new}")

def bai_5():
    print("\n" + "=" * 50)
    print("BÀI 5: Thêm phần tử vào danh sách")
    print("=" * 50)
    _list = ['zero', 'three']
    _list.insert(1, 'one')
    _list.insert(2, 'two')
    _new = _list
    print(f"List mới : {_new}")

def bai_7a():
    print("\n" + "=" * 50)
    print("BÀI 7a: Loại bỏ tất cả phần tử có giá trị trùng lặp")
    print("=" * 50)
    _list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
    _new = []
    for phan_tu in _list:
        if _list.count(phan_tu) == 1:
            _new.append(phan_tu)
    print(f"List gốc : {_list}")
    print(f"List mới : {_new}")

def bai_7b():
    print("\n" + "=" * 50)
    print("BÀI 7b: Giữ lại 1 phần tử khi bị trùng lặp")
    print("=" * 50)
    _list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
    _new = []
    for phan_tu in _list:
        if phan_tu not in _new:
            _new.append(phan_tu)
    print(f"List gốc : {_list}")
    print(f"List mới : {_new}")

def bai_8():
    print("\n" + "=" * 50)
    print("BÀI 8: Lấy số lớn nhất trong list")
    print("=" * 50)
    _list = [11, 2, 23, 45, 6, 9]
    _max = _list[0]
    for so in _list:
        if so > _max:
            _max = so
    print(f"List    : {_list}")
    print(f"Số lớn nhất = {_max}")

def bai_9():
    print("\n" + "=" * 50)
    print("BÀI 9: Lấy số nhỏ nhất trong list")
    print("=" * 50)
    _list = [11, 2, 23, 45, 6, 9]
    _min = _list[0]
    for so in _list:
        if so < _min:
            _min = so
    print(f"List    : {_list}")
    print(f"Số nhỏ nhất = {_min}")

def bai_10():
    print("\n" + "=" * 50)
    print("BÀI 10: Copy list thành list mới")
    print("=" * 50)
    _list = [11, 2, 23, 45, 6, 9]
    _new = []
    for phan_tu in _list:
        _new.append(phan_tu)
    print(f"List gốc : {_list}")
    print(f"List mới : {_new}")
    print(f"Là 2 list khác nhau: {_list is not _new}")

def bai_11():
    print("\n" + "=" * 50)
    print("BÀI 11: Tìm các từ có độ dài lớn hơn n")
    print("=" * 50)
    _list = ['apple', 'hi', 'python', 'is', 'great', 'ok']
    try:
        n = int(input("Nhập số n: "))
        _new = []
        for tu in _list:
            if len(tu) > n:
                _new.append(tu)
        print(f"List gốc        : {_list}")
        print(f"Từ có độ dài > {n}: {_new}")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def bai_12():
    print("\n" + "=" * 50)
    print("BÀI 12: Đếm chuỗi có độ dài >= n và ký tự đầu == ký tự cuối")
    print("=" * 50)
    _list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
    try:
        n = int(input("Nhập giá trị độ dài tối thiểu n: "))
        dem = 0
        for chuoi in _list:
            if len(chuoi) >= n and chuoi[0] == chuoi[-1]:
                dem += 1
        print(f"List gốc : {_list}")
        print(f"Độ dài >= {n}, ký tự đầu == ký tự cuối => Đếm được: {dem}")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def main():
    while True:
        print("\n" + "=" * 50)
        print("               MENU CHỌN BÀI TẬP LIST")
        print("=" * 50)
        print("1.  Bài 1: Tính tổng các phần tử trong list")
        print("2.  Bài 2: Tính tích các phần tử trong list")
        print("3.  Bài 3: Tạo 2 list mới: số chẵn và số lẻ")
        print("4.  Bài 4: Lấy phần tử ở vị trí thứ 2 và thứ 3")
        print("5.  Bài 5: Thêm các phần tử vào danh sách ban đầu")
        print("7a. Bài 7a: Loại bỏ TẤT CẢ phần tử có giá trị giống nhau")
        print("7b. Bài 7b: Với phần tử trùng lặp, chỉ giữ lại 1 phần tử")
        print("8.  Bài 8: Lấy số lớn nhất trong list")
        print("9.  Bài 9: Lấy số nhỏ nhất trong list")
        print("10. Bài 10: Copy một list thành một list mới")
        print("11. Bài 11: Nhập số n, tìm các từ có độ dài > n trong list")
        print("12. Bài 12: Đếm số chuỗi thỏa mãn điều kiện")
        print("0.  Thoát")
        print("=" * 50)
        
        choice = input("Vui lòng nhập lựa chọn của bạn: ").strip()

        if choice == '1':
            bai_1()
        elif choice == '2':
            bai_2()
        elif choice == '3':
            bai_3()
        elif choice == '4':
            bai_4()
        elif choice == '5':
            bai_5()
        elif choice == '6':
            print("\n!!! Bài 6 bị bỏ qua theo yêu cầu !!!")
        elif choice.lower() == '7a':
            bai_7a()
        elif choice.lower() == '7b':
            bai_7b()
        elif choice == '8':
            bai_8()
        elif choice == '9':
            bai_9()
        elif choice == '10':
            bai_10()
        elif choice == '11':
            bai_11()
        elif choice == '12':
            bai_12()
        elif choice == '0':
            print("\nĐã thoát chương trình. Tạm biệt!")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()
