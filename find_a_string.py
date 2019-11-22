def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
      if string.find(sub_string,i,i+len(sub_string)) != -1:
        count += 1
    return count

if __name__ == '__main__':