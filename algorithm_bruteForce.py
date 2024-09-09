# 연습문제
pw = input("4자리 비밀번호를 입력하세요: ")

answer = ''
found = False

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                answer = str(a) + str(b) + str(c) + str(d)
                if answer == pw:
                    found = True
                    break  # 가장 안쪽 루프를 종료
            if found:
                break  # c 루프를 종료
        if found:
            break  # b 루프를 종료
    if found:
        break  # a 루프를 종료

print('정답:', answer)
