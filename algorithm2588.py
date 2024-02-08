# 세자리 수 * 세자리 수를 계산할때 각 자리수 별 값 구하기
# 예시) 472*385
# (1) 472*5
# (2) 472*8
# (3) 472*3 와 (4) 472*385의 답 을 구하면 됨.

num1 = int(input())
num2 = int(input())

n1 = num2%10
n2 = num2%100

n2 = n2-n1
n3 = num2-n2-n1

ans1 = num1*n1
ans2 = num1*n2//10
ans3 = num1*n3//100
ans4 = ans1+ans2*10+ans3*100
print(ans1,ans2,ans3,ans4,sep='\n') # 답은 맞으나 더 줄일 수 있을 거 같으니 더 생각해 보자


