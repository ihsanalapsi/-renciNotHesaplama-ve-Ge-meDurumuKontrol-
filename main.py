grades = {
    'Küçük Sınavlar 2': 30.00,
    'Küçük Sınavlar 3': 65.00,
    'Küçük Sınavlar 4': 50.00,
    'Küçük Sınavlar 1': 0.00, 
    'Sunum': 100,             
    'Ara Sınavlar':32,       
    'Final': 50
}

weights = {
    'Küçük Sınavlar 2': 3.75,
    'Küçük Sınavlar 3': 3.75,
    'Küçük Sınavlar 4': 3.75,
    'Küçük Sınavlar 1': 3.75,
    'Sunum': 15,
    'Ara Sınavlar': 30,
    'Final': 40
}

final_grade = sum(grades[test] * (weights[test] / 100) for test in grades)
passing_grade = 50
final_grade_percentage = final_grade / sum(weights.values()) * 100 
passed = final_grade_percentage >= passing_grade

print("Genel Ders Notu :", final_grade)
print("Yuzdelik :", final_grade_percentage)
print("Ogrenci Dersten Gecti mi ? : ", "Evet" if passed else "Hayir")
