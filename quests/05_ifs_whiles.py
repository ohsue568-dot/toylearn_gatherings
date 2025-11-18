first = 5   # 오타

while first > 0:
    print(f"while 값 : {first}")
    first = first - 1


first = 5

while first > 0:
    print(f"while 값 : {first}")  # 올바른 들여쓰기
    first = first - 1


first = 5

while first > 0:
    print(f"while 값 : {first}")
    if first < 3:     # 잘못된 조건
        print("break 실행")
        break
    first = first - 1