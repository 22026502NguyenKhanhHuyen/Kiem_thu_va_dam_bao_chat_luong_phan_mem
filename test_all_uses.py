from tinh_gia_ve import tinh_gia_ve

def kiem_thu():
    test_cases = [
        (5, True, True, 0),
        (7, True, False, 40000),
        (15, True, True, 88000),
        (5, False, False, 0),
        (5, False, False, 0),
        (7, False, True, 55000),
        (7, False, False, 50000),
        (15, False, True, 110000),
        (15, False, False, 100000)
    ]
    
    for i, (tuoi, hoi_vien, cuoi_tuan, expected) in enumerate(test_cases, 1):
        result = tinh_gia_ve(tuoi, hoi_vien, cuoi_tuan)
        print(f"Test case {i}: Expected = {expected}, Actual = {result}, {'Pass' if result == expected else 'Fail'}")
        
kiem_thu()
