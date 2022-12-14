# percabangan
jumlah_botol_susu = 2
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} btl")
print(f"jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("budi membeli satu botol susu")
    else:
        print("budi membeli 6 botol susu")
else :
    print("budi tidak jadi membeli satu botol susu")

print("budi pulang kerumah")
print("menyerahkan hasilnya kepada ibu")