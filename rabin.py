
def searchPattern(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    d = 10

    for i in range(m-1):
        h = (h*d) % q

    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q   

    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                print("Patten is found at positi0on : "  + str(i+1))

        if i < n-m: 
            t = (d*(t-ord(text[i]) *h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q             

text = "ABCCDDEFGH"
pattern = "CCD"
q = 13
print(searchPattern(pattern, text, q))