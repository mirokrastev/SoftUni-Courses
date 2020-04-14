the_N = int(input())
 
for i1 in range(1,10):
  for i2 in range(1,10):
    for i3 in range(1,10):
      for i4 in range(1,10):
        s_number = f'{i1}{i2}{i3}{i4}'
        number = int(s_number)
        if the_N % i1 == 0 and the_N % i2 == 0 and the_N % i3 == 0 and the_N % i4 == 0:
          print(number, end=' ')