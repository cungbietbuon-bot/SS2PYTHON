heart_rate = int(input("Nhập nhịp tim bệnh nhân: "))

if heart_rate > 120:
    priority = "RED - Nguy kịch, cấp cứu ngay"

elif heart_rate > 100:
    priority = "YELLOW - Bất thường, cần theo dõi sát"

elif heart_rate < 60:
    priority = "BLUE - Nhịp tim chậm, cần kiểm tra thêm"

else:
    priority = "GREEN - Ổn định, chờ theo thứ tự"

print("\n===== KẾT QUẢ PHÂN LOẠI =====")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f"Mức độ ưu tiên: {priority}")