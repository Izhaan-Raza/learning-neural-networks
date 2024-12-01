x = int(input("Enter: "))

while(x%10==0):
    x //=10
n=0
while(x>0):
    n *=10
    n += x%10
    x = x//10
print(n)