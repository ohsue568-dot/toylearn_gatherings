# ----------------------------------------------------
# 🔹 문제 1: 섭씨 온도 3개의 평균을 반환하는 함수
# 함수명: avg_celsius(t1, t2, t3)
# ----------------------------------------------------
def avg_celsius(t1, t2, t3):
    """섭씨 온도 3개를 받아 평균을 계산하여 반환합니다."""
    average = (t1 + t2 + t3) / 3
    return average

# 함수 실행 (최소 3회 호출)
print("--- 문제 1: 섭씨 온도 평균 ---")
print(f"1. 평균 (10, 20, 30): {avg_celsius(10, 20, 30)}°C")
print(f"2. 평균 (0, 5, 10): {avg_celsius(0, 5, 10)}°C")
print(f"3. 평균 (25.5, 27.5, 30): {avg_celsius(25.5, 27.5, 30)}°C")
print("-" * 30)


# ----------------------------------------------------
# 🔹 문제 2: 이름과 좋아하는 언어 2개를 형식에 맞춰 출력하는 함수
# 함수명: print_preference(name, lang1, lang2)
# ----------------------------------------------------
def print_preference(name, lang1, lang2):
    """이름과 선호 언어 2개를 형식에 맞춰 출력합니다."""
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

# 함수 실행 (최소 3회 호출)
print("--- 문제 2: 선호 언어 출력 ---")
print_preference("홍길동", "Python", "Java")
print_preference("김철수", "C++", "C#")
print_preference("이영희", "JavaScript", "TypeScript")
print("-" * 30)


# ----------------------------------------------------
# 🔹 문제 3: 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수
# 함수명: sum_pass_scores(scores)
# ----------------------------------------------------
def sum_pass_scores(scores):
    """점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환합니다."""
    total_sum = 0
    for score in scores:
        if score >= 60:
            total_sum += score
    return total_sum

# 함수 실행 (최소 3회 호출)
print("--- 문제 3: 60점 이상 점수 합계 ---")
print(f"1. 합계 ([80, 50, 90, 70]): {sum_pass_scores([80, 50, 90, 70])}점") 
print(f"2. 합계 ([40, 55, 30]): {sum_pass_scores([40, 55, 30])}점") 
print(f"3. 합계 ([100, 60, 95]): {sum_pass_scores([100, 60, 95])}점")
print("-" * 30)


# ----------------------------------------------------
# 🔹 문제 4: 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수
# 함수명: combine(str1, str2)
# ----------------------------------------------------
def combine(str1, str2):
    """문자열 두 개를 이어 붙여 하나의 문장으로 반환합니다."""
    combined_string = str1 + str2
    return combined_string

# 함수 실행 (최소 3회 호출)
print("--- 문제 4: 문자열 결합 ---")
print(f"1. 결합: {combine('Hello', ' World!')}")
print(f"2. 결합: {combine('Python', ' Programming')}")
print(f"3. 결합: {combine('파이썬은 ', '정말 쉽다.')}")
print("-" * 30)


# ----------------------------------------------------
# 🔹 문제 5: 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수
# 함수명: fahrenheit_to_celsius_list(temps_f)
# ----------------------------------------------------
def fahrenheit_to_celsius_list(temps_f):
    """온도 리스트(화씨)를 받아 모두 섭씨로 변환해 새로운 리스트로 반환합니다."""
    temps_c = []
    for temp_f in temps_f:
        # 섭씨 변환 공식: C = (F - 32) * 5 / 9
        temp_c = (temp_f - 32) * 5 / 9
        temps_c.append(temp_c)
    return temps_c

# 함수 실행 (최소 3회 호출)
print("--- 문제 5: 화씨 리스트 섭씨 변환 ---")
print(f"1. 변환 ([32, 212]): {fahrenheit_to_celsius_list([32, 212])}") 
print(f"2. 변환 ([50, 68, 86]): {fahrenheit_to_celsius_list([50, 68, 86])}")
print(f"3. 변환 ([98.6, 14]): {fahrenheit_to_celsius_list([98.6, 14])}")
print("-" * 30)