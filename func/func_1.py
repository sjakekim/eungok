def even_sum() :
    num = 0
    for i in range(11) :
        if i%2 == 1 :
            continue
        num += i

    print(f"1부터 10까지 합은 {num}")

even_sum()

