def tinh_gia_ve(tuoi, la_hoi_vien, ngay_cuoi_tuan):
    if tuoi < 6:
        gia_ve = 0
    elif 6 <= tuoi < 12:
        gia_ve = 50000
    else:
        gia_ve = 100000

    if la_hoi_vien:
        gia_ve *= 0.8
    
    if ngay_cuoi_tuan:
        gia_ve *= 1.1
    
    return round(gia_ve)