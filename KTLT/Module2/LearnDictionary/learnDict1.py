emp1 = {"Ma":"NV1",
       "Ten":"Nguyen Thi Han",
       "Tuoi":25}
dataset = [emp1,
           {"Ma":"NV2",
            "Ten":"Tran Hihi",
            "Tuoi":27}]

dataset.append({"Ma":"NV3",
            "Ten":"Tran Hahahahahah",
            "Tuoi":24})

print("Danh sách nhân viên:")
for emp in dataset:
    print(emp["Ma"],emp["Ten"],emp["Tuoi"])