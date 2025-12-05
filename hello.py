def fact(n):
  if n==0:
    return 1
  else:
    return n * fact(n-1)
number = 5
res=fact(number)
print("factoriel de",number,"est",res )
