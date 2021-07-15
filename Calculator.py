print("더하기, 빼기, 나누기, 곱셈")

print("처음수")

first=input("수:")
first=int(first)

print("다음수")

second=input("수:")
second=int(second)

print("무엇으로 계산할건가요?(더하기 = 1, 빼기 = 2,나누기 = 3,곱하기 = 4)")

Kinds=input("입력.. :")
Kinds=int(Kinds)

if Kinds == 1:
	print("따라서 결과는", first + second, "입니다.")
elif Kinds == 2:
	print("따라서 결과는", first - second, "입니다.")
elif Kinds == 3:
	print("따라서 결과는", first / second, "입니다.")
elif Kinds == 4:
	print("따라서 결과는", first * second, "입니다.")