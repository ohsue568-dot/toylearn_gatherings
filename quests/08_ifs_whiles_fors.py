# 문제 1 - return 누락 오류
def to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius # return 문 추가

result = to_celsius(77)
print(result) # 출력: 25.0

# 문제 2 — 매개변수 이름 오류
def convert(temp):
    return (temp - 32) * 5 / 9   # temps -> temp 및 공식 수정

print(convert(95)) # 출력: 35.0

# 문제 3 — 함수 호출 인자 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9

value = to_celsius(77) # 오류 수정: 인자 (예: 77) 전달
print(value) # 출력: 25.0

# 문제 4 — 타입 오류(TypeError)
def to_celsius(temp):
    return (temp - 32) * 5 / 9 # 공식 수정

print(to_celsius(77)) # 오류 해결: 문자열 "77"을 정수 77로 변경
# 출력: 25.0

#문제 5 — 반복 구조 + 함수 사용 오류
def to_celsius(temp):
    return (temp - 32) * 5 / 9 # 공식 수정

temps = [77, 95, 50]
results = []

for t in temps:
    result = to_celsius(t)   # 변수명 오류 수정: temp -> t
    results.append(result) # 계산된 결과를 results 리스트에 추가

print(results) # 반복문 종료 후 최종 결과 출력
# 출력: [25.0, 35.0, 10.0]