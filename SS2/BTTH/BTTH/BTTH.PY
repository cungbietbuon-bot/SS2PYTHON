from datetime import datetime

patient_name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh: "))
sick_days = int(input("Nhập số ngày bị bệnh: "))
body_temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
medical_fee = float(input("Nhập chi phí khám: "))

current_year = datetime.now().year

if patient_name.strip() == "":
    print("LỖI: Tên bệnh nhân không được để trống!")

elif birth_year < 1900 or birth_year > current_year:
    print("LỖI: Năm sinh không hợp lệ!")

elif sick_days < 0:
    print("LỖI: Số ngày bị bệnh không hợp lệ!")

elif body_temperature < 30 or body_temperature > 45:
    print("LỖI: Nhiệt độ cơ thể không hợp lệ!")

elif medical_fee <= 0:
    print("LỖI: Chi phí khám phải lớn hơn 0!")

else:
    patient_age = current_year - birth_year

    extra_fee = medical_fee * 0.10
    total_fee = medical_fee + extra_fee

    if body_temperature > 38 and sick_days > 3:
        health_status = "Nguy hiểm"

    elif body_temperature > 38:
        health_status = "Sốt cao"

    elif body_temperature > 37.5:
        health_status = "Sốt nhẹ"

    else:
        health_status = "Bình thường"

    if health_status == "Nguy hiểm":

        if patient_age > 60:
            priority = "Cấp cứu"

        else:
            priority = "Ưu tiên cao"

    else:
        priority = "Bình thường"


    cost_level = "Cao" if total_fee > 500000 else "Thấp"

  
    print("\n========== KẾT QUẢ KHÁM ==========")

    print(f"Tên bệnh nhân: {patient_name}")
    print(f"Tuổi: {patient_age}")
    print(f"Số ngày bị bệnh: {sick_days}")
    print(f"Nhiệt độ cơ thể: {body_temperature} °C")

    print(f"\nChi phí khám: {medical_fee:,.0f} VNĐ")
    print(f"Phụ phí (10%): {extra_fee:,.0f} VNĐ")
    print(f"Tổng chi phí: {total_fee:,.0f} VNĐ")

    print(f"\nTình trạng sức khỏe: {health_status}")
    print(f"Mức độ ưu tiên: {priority}")
    print(f"Mức chi phí: {cost_level}")

    print("==================================")