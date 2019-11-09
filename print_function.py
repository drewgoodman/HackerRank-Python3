# PRINT FUNCTION
# All digits in order, no string functions

if __name__ == '__main__':
    n = int(input())
    nums = []
    i = 0
    while i < n:
        i += 1
        nums.append(i)
    output = 0
    for num in nums:
        j = num
        count = 0
        while j > 0:
            j = j//10
            count += 1
        output *= 10**count
        output += num
    print(output)