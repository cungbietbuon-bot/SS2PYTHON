age = int(input("Nhập tuổi bệnh nhân: "))
systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print("\nLỖI: Dữ liệu nhập vào không hợp lệ!")

else:
    if age >= 75:
        print("\nTỪ CHỐI PHẪU THUẬT")
        print("Lý do: Tuổi bệnh nhân quá cao.")

    else:
        if systolic_bp < 90 or systolic_bp > 140:
            print("\nTỪ CHỐI PHẪU THUẬT")
            print("Lý do: Huyết áp ngoài ngưỡng an toàn.")

        else:
            if blood_sugar >= 150:
                print("\nTỪ CHỐI PHẪU THUẬT")
                print("Lý do: Đường huyết quá cao.")

            else:
                print("\nĐỦ ĐIỀU KIỆN PHẪU THUẬT")
                print("Bệnh nhân đạt toàn bộ tiêu chuẩn an toàn.")