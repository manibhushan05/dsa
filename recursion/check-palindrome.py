def check_palindrome(s, i, j):
    if i > j:
        return True
    return s[i] == s[j] and check_palindrome(s, i + 1, j - 1)


if __name__ == '__main__':
    s = 'AA'
    print(check_palindrome(s, 0, len(s) - 1))
