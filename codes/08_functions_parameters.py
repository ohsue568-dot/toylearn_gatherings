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

#sum = get_sum(kor, eng, math)
#print(f"총점: {sum}")

#sum = get_sum(kor, eng)
#print(f"총점: {sum}")

#for문 함수 작성
kor_scores = [90, 80, 70, 60, 50]
eng_scores = [85, 75, 65, 55, 45]
math_scores = [88, 78, 68, 58, 48]

length = len(kor_scores)
len_list=range(length)
range(len(kor_scores)) # 0, 1, 2, 3, 4
pass
for i in range(len(kor_scores)):
    kor = kor_scores[i]
    eng = eng_scores[i]
    math = math_scores[i]
    sum = get_sum(kor, eng, math)
    print(f"{i+1}번째 학생 총점: {sum}")

def get_for_sum(korean_scores, english_scores, mathematics_scores):
     # 실행할 코드
     for i in range(len(kor_scores)):
         kor = kor_scores[i]
         eng = eng_scores[i]
         math = math_scores[i]
         sum = get_sum(kor, eng, math)
         print(f"{i+1}번째 학생 총점: {sum}")

    return 0

get_for_sum(kor_scores, eng_scores, math_scores)