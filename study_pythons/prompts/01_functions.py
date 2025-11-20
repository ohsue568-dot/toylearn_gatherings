# prompts/01_functions.py

# 테스트 리스트 (10개)
# 제약 조건: 테스트 데이터는 리스트(list)로만 제공되어야 함.
# 제약 조건: 테스트 데이터 쌍은 10개여야 함.
# 제약 조건: 변수명은 소문자와 언더스코어(_) 조합을 사용해야 함.
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

def perform_arithmetic_operations(num_a, num_b):
    """
    두 숫자에 대해 덧셈, 뺄셈, 곱셈, 나눗셈을 수행하고 결과를 반환합니다.
    나눗셈에서 0으로 나누는 경우 'division_error'를 반환합니다.
    
    :param num_a: 첫 번째 숫자
    :param num_b: 두 번째 숫자
    :return: (덧셈 결과, 뺄셈 결과, 곱셈 결과, 나눗셈 결과)를 포함하는 튜플
    """
    
    # 덧셈 계산
    addition_result = num_a + num_b
    
    # 뺄셈 계산
    subtraction_result = num_a - num_b
    
    # 곱셈 계산
    multiplication_result = num_a * num_b
    
    # 나눗셈 계산 및 0으로 나누는 경우 처리
    # 제약 조건: 나눗셈에서 0으로 나누는 경우, 해당 나눗셈 결과 대신 문자열 "division_error"를 반환해야 함.
    if num_b == 0:
        division_result = "division_error"
    else:
        division_result = num_a / num_b
        
    # 제약 조건: 함수는 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 포함하는 튜플 또는 리스트 형태로 반환해야 함.
    return (addition_result, subtraction_result, multiplication_result, division_result)

# 테스트 실행
# 제약 조건: range(10)을 사용하여 test_a와 test_b의 요소를 반복 접근
# 제약 조건: 반복문 내에서 정의된 함수 호출
print("--- 사칙연산 테스트 결과 ---")
print("(덧셈, 뺄셈, 곱셈, 나눗셈)")
print("--------------------------")
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    
    # 함수 호출
    result = perform_arithmetic_operations(a, b)
    
    # 출력 형식: print(f"{a}, {b} => {result}")
    print(f"{a}, {b} => {result}")
print("--------------------------")


--- 사칙연산 테스트 결과 ---
(덧셈, 뺄셈, 곱셈, 나눗셈)
--------------------------
10, 5 => (15, 5, 50, 2.0)
25, 5 => (30, 20, 125, 5.0)
40, 8 => (48, 32, 320, 5.0)
12, 3 => (15, 9, 36, 4.0)
7, 0 => (7, 7, 0, 'division_error')
9, 3 => (12, 6, 27, 3.0)
16, 2 => (18, 14, 32, 8.0)
100, 4 => (104, 96, 400, 25.0)
3, 9 => (12, -6, 27, 0.3333333333333333)
81, 9 => (90, 72, 729, 9.0)
--------------------------