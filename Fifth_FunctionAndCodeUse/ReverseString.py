# Reverse String


def rev_str(s):
    if s == '':
        return s
    else:
        return rev_str(s[1:]) + s[0]


if __name__ == "__main__":
    print(rev_str("I love python !"))
