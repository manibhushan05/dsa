def reverseOnlyLetters(s: str) -> str:
    s = list(s)
    m, n = 0, len(s) - 1
    while m < n:
        print(m, n, s[m].isalpha() and s[n].isalpha())
        if s[m].isalpha() and s[n].isalpha():
            s[m], s[n] = s[n], s[m]
            m += 1
            n -= 1
        elif not s[m].isalpha():
            m += 1
        elif not s[n].isalpha():
            n -= 1
    return "".join(s)


print(reverseOnlyLetters("a-bC-dEf-ghIj"))
