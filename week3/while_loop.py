# while loops
# for loops
# recursion

x=0;
while x<5:
    print("Count is: "+str(x))
    x=x+1


def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  num = n-1
  while num > 0:
    if (num)>0 and n%(num)==0:
       sum = sum + num
    
    num= num-1

  return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114



