str1 = input("Enter the long string: ")

str2 = input("Enter the short string: ")

count = 0

for i in range(0, len(str1)):
    for j in range(0, len(str2)):
        if str1[i+j] != str2[j]:
            print("str", str1[i], str2[j])
            break
        else:
            print("str", str1[i], str2[j])
            if j == len(str2) - 1:
                count += 1
print("count: ", count)
