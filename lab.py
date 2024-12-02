# x = int(input("Enter: "))

# while(x%10==0):
#     x //=10
# n=0
# while(x>0):
#     n *=10
#     n += x%10
#     x = x//10
# print(n)



x = "Hello a b c hello a b b"
lst = []
j=0
for i in range(len(x)):
    if x[i] == " ":
        lst.append(x[i:j])
        j=i
print(lst)