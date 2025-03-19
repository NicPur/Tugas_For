status = ["Tetap", "Honor"]
group = ["A", "B", "C"]
salary = [1000000, 750000]
permanent_bonus = [200000, 400000, 550000]
honor_bonus = [150000, 275000, 480000]

for s in status:
    print("Status:", s)
    for i in range(len(group)):
        if s == "Tetap":
            sal = salary[0]
            bonus = permanent_bonus[i]
        else:
            sal = salary[1]
            bonus = honor_bonus[i]
        total = sal + bonus
        print("Golongan:", group[i])
        print("Gaji pokok:", format(sal, ","))
        print("Bonus:", format(bonus, ","))
        print("Total:", format(total, ","))
        print()