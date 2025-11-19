# 문제 6 — 함수 내부 변수 오타

def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9   # celsiu -> celsius 수정
    return celsius

print(to_celsius(77)) # 출력: 25.0

# 문제 7 — return 위치 오류
def to_celsius(temp):
    if temp > 0:
        celsius = (temp - 32) * 5 / 9
        return celsius # 올바른 위치
    # return             # 제거
    #     celsius
    
print(to_celsius(50)) # 출력: 10.0

#문제 8 — 함수 재사용 시 논리 오류
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9 # 공식 수정
    return celsius

temp = 77
result1 = to_celsius(temp)

temp = 95
result2 = to_celsius(temp) # 인자 temp 추가

temp = 50
result3 = to_celsius(temp)

print(result1, result2, result3) # 출력: 25.0 35.0 10.0

#문제 9 — 리스트 값 변환 시 타입 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9 # 공식 수정

temps = [77, 95, 50]
values = []

# 리스트의 각 요소에 대해 함수 호출
for temp_val in temps:
    values.append(to_celsius(temp_val))

print(values) # 출력: [25.0, 35.0, 10.0]

#문제 10 — 함수 반환값을 활용한 조건문 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9

if to_celsius(77) > 20:       # 함수 호출 및 인자 (예: 77) 전달
    print("warm")
else:
    print("cold") # 출력: warm