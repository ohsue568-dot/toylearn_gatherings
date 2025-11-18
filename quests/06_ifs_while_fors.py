# 문제1
second = "Programming"
first = "Welcome to Python Strings " + second

print(first)


# 문제 2
first = "Hello Python"
count = 5

while count > 0:
    print(first)
    count = count - 1

# 문제 3
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]
sum_all = 0

for k, e in zip(kor, eng):
    sum_all = sum_all + k + e

print(sum_all)

# 문제 4
kor = [70, 80, 90, 40, 50]
eng = [90, 80, 70, 70, 60]

sum_total = 0

for i in range(len(kor)):
    sum_total = sum_total + kor[i] + eng[i]

print(sum_total)

