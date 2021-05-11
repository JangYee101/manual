

PASS_SIZE = 50

def getPass(source_pass):
    pass_list = []
    for char in source_pass:
        the_ord = ord(char)
        if the_ord < 10:
            the_ord += 10
        pass_list.append(str(the_ord)[:2])
    pass_str = ''.join(pass_list)
    if len(pass_str) > PASS_SIZE:
        return pass_str
    print pass_str
    return getPass(pass_str)


if __name__ == "__main__":
    print getPass("jiangye")
    print getPass("ye")
