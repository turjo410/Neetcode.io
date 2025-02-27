s = input("Input First String ")
t = input("Input Second String ")
sorted_s = ''.join(sorted(s))
sorted_t = ''.join(sorted(t))
count = 0

print(sorted_s)
print(sorted_t)

for i in range(len(s)):
        if sorted_s[i] == sorted_t[i]:
            count = count+1

if(count == len(s)):
      print('true')
else: print('false')




