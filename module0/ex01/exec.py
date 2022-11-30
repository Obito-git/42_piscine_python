import sys

s = ""
res = ""
for e in range(1, len(sys.argv)):
    s += (sys.argv[e] + " ")
s = s[:len(s) - 1]
s = s[::-1]
for c in s:
    res += c.upper() if c.islower() else c.lower()
if len(res) > 0:
    print(res)

