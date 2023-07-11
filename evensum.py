sum = 0
for i in range(1,101):
     if i%2 == 0:
         continue
     sum += i
     
print(f"홀수의 합은 {sum} 입니다.")

sum = 0
for i in range(1,101):
     if i%2 == 1:
          continue
     sum += i
print(f"짝수의 합은 {sum}입니다.")
  

