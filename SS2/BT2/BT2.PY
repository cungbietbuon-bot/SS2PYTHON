donor_age = int(input("Nhập tuổi người hiến máu: "))
donor_weight = float(input("Nhập cân nặng (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("\nKẾT QUẢ: ĐỦ ĐIỀU KIỆN hiến máu")

else:
    print("\nKẾT QUẢ: KHÔNG ĐỦ ĐIỀU KIỆN hiến máu")

    if donor_age < 18:
        print("- Lý do: Chưa đủ 18 tuổi")

    if donor_weight < 50:
        print("- Lý do: Cân nặng dưới 50kg")