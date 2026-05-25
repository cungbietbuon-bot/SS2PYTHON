patient_name = input("Nhập họ tên bệnh nhân: ").strip()

patient_age = int(input("Nhập tuổi bệnh nhân: "))

if patient_name == "":
    print("\nLỖI: Tên bệnh nhân không hợp lệ!")

elif patient_age < 0 or patient_age > 150:
    print("\nLỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")

else:

    if patient_age < 6:
        classification = (
            "ƯU TIÊN: Bệnh nhi - "
            "Chuyển thẳng phòng khám Nhi."
        )

    elif patient_age >= 80:
        classification = (
            "ƯU TIÊN: Người cao tuổi - "
            "Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        )

    else:
        classification = (
            "KHÁM THƯỜNG: "
            "Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
        )

    print("\n===================================")
    print("      PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print("===================================")

    print(f"Họ tên bệnh nhân : {patient_name}")
    print(f"Tuổi bệnh nhân   : {patient_age}")

    print("\nKết quả phân luồng:")
    print(classification)

    print("===================================")