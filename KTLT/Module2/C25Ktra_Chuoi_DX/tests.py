from Module2.C25Ktra_Chuoi_DX.C25KtraChuoiDoiXung import ktra_chuoi_dx, kt_chuoi_dx

chuoi = "12345678"
chuoi = "123  321"
chuoi = "12as sa21"

# rs = ktra_chuoi_dx(chuoi)
# if rs==True:
#     print(f"'{chuoi}' là một chuỗi đối xứng!")
# else:
#     print(f"'{chuoi}' không phải là một chuỗi đối xứng")

rs1 = kt_chuoi_dx(chuoi)
if rs1==True:
    print(f"'{chuoi}' là một chuỗi đối xứng!")
else:
    print(f"'{chuoi}' không phải là một chuỗi đối xứng")