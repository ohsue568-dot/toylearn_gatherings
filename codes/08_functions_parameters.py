# 함수 사용
# def function_name(param_first, ..., param_last):
#    # 실행할 코드
#    return return_value

# 점수 총합 함수 작성
kor = 60
eng = 70
math = 80

#sum = kor + eng
def get_sum(korean, english, mathematics):
    # 실행할 코드
    summation =  korean + english + mathematics
    print("함수 내부에서 출력:", summation)
    return summation

sum = get_sum(kor, eng, math)
print(f"총점: {sum}")

sum = get_sum(kor, eng)
print(f"총점: {sum}")