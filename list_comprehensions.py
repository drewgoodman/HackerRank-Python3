if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

coords = []
i = 0

while i <= x:
  j = 0
  while j <= y:
    k = 0
    while k <= z:
      if i + j + k != n:
        coords.append([i,j,k])
      k += 1
    j += 1
  i += 1


print(coords)