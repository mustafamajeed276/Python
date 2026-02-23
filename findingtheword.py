def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

if __name__ == "__main__":
    s1 = "welcome"
    s2 = "welcome to codingal"
    result = isSubstring(s1, s2)
    if result == -1:
        print("not present")
    else:
        print(str(result))    