n = int(input("Введите число n (1 ≤ n ≤ 4): "))
total_sum = 0

if n == 1:
    total_sum = sum(range(1, 10))
elif n == 2:
    for i in range(1, 10):
        for j in range(10):
            total_sum += int(str(i) + str(j))
elif n == 3:
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                total_sum += int(str(i) + str(j) + str(k))
else: # n == 4
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    total_sum += int(str(i) + str(j) + str(k) + str(l))

print(f"Сумма всех {n}-значных чисел равна {total_sum}.")
 
    #If GxVeteran

