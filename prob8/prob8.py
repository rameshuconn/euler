file1 = open("data.txt",'r')
lines = file1.readlines()
a = ""
for line in lines:
    line = line.rstrip()
    a += line

def read_n(s, cur):
    return(s[cur:cur+13])

def prod_str(s):
    n = 1
    for c in s:
        n *= int(c)
        # print(n)

    return(n)

i = 0
highest_prod = 0
highest_string = "0"
while i < len(a)-13:
    next_string = read_n(a,i)
    next_prod = prod_str(next_string)
    if highest_prod < next_prod:
        highest_prod = next_prod
        highest_string = next_string
    
    i += 1

print(highest_string)
print(highest_prod)
