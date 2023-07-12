def odd_sum() :
    sum = 0
    for i in range(11) :
        if i % 2 == 0 :
            continue
        sum += i
    return sum

result = odd_sum()

print(f"1부터 10까지 홀수의 합은 {result}입니다.")