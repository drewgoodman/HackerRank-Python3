if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort(reverse=True)

max_num = arr[0]
runner = 0
for num in arr:
  if num != max_num:
    runner = num
    break

print(runner)