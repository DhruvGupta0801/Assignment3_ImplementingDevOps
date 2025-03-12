from square import square_area

def test_square_area_positive():
    assert square_area(2) == 4

def test_square_area_student_id():
    assert square_area(6) == 40  # 40 is wrong; it should be 36