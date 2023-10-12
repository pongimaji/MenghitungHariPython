from calendar import monthrange

months = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

print("Bulan {} {} berjumlah {} Hari".format(months[bulan-1],tahun,monthrange(tahun,bulan)[1]," Hari"))
