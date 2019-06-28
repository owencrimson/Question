import copy
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def question(x):
	answer1 = []
	answer = []
	for i in numbers:
		numbers2 = copy.copy(numbers)		
		numbers2.remove(i)
		for j in numbers2:
			num1 = i * 100
			num1 += j * 10
			numbers3 = copy.copy(numbers2)
			numbers3.remove(j)
			for k in numbers3:
				num1 = i * 100 + j * 10
				num1 += k
				numbers4 = copy.copy(numbers3)
				numbers4.remove(k)

				for a in numbers4:
					num2 = a * 100
					numbers5 = copy.copy(numbers4)
					numbers5.remove(a)
					for b in numbers5:
						num2 = a * 100
						num2 += b * 10
						numbers6 = copy.copy(numbers5)
						numbers6.remove(b)
						for c in numbers6:
							num2 = a * 100 + b * 10
							num2 += c
							numbers7 = copy.copy(numbers6)
							numbers7.remove(c)

							for d in numbers7:
								num3 = d * 100
								numbers8 = copy.copy(numbers7)
								numbers8.remove(d)
								for e in numbers8:
									num3 = d * 100
									num3 += e * 10
									numbers9 = copy.copy(numbers8)
									numbers9.remove(e)
									for f in numbers9:
										num3 = d * 100 + e * 10
										num3 += f

									if num2 == 2 * num1 and num3 == 3 * num1:
										answer1.append(num1)
										answer1.append(num2)
										answer1.append(num3)
										answer.append(answer1)
										answer1 = []
	return answer

print(question(numbers))