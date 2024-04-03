def compress(S):
    #:type S: str
    #:rtype: str

    S1 = ""
    i = 0
    while i < len(S):
        c = S[i]
        j = i + 1
        while j < len(S) and S[j] == c:
            j += 1
        S1 += c
        if j - i > 1:
            S1 += ""
        i = j
    return S1


# Test cases
print(compress("stuuudents"))
