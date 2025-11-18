# ==============================
# 중급 난이도 문제 1 — 문자열과 f-string 활용
# ==============================
second = "Python is fun"

if "Python" in second:
    result = f"Welcome! {second}"

print("문제 1 출력:", result)
print("-----------------------------")


# ==============================
# 중급 난이도 문제 2 — while 반복문 응용
# ==============================
first = 5

print("문제 2 출력:")
while first >= 1:
    if first == 2:
        print("special")
    first -= 1
print("-----------------------------")


# ==============================
# 중급 난이도 문제 3 — 리스트 합계 및 평균 계산
# ==============================
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

total_scores = []
avg_scores = []

for k, e in zip(kor, eng):
    total = k + e
    avg = total / 2
    total_scores.append(total)
    avg_scores.append(avg)

print("문제 3 출력:")
print("total_scores =", total_scores)
print("avg_scores =", avg_scores)
print("-----------------------------")


# ==============================
# 중급 난이도 문제 4 — 누적 합과 조건문 결합
# ==============================
sum_kor = 0
for score in kor:
    if score >= 60:
        sum_kor += score

print("문제 4 출력:")
print("누적합 =", sum_kor)
