def cleanstring(string, substring):
    if substring in string:
        pos = string.find(substring)
        return string[0:pos] + string[pos+len(substring):]
    else:
        return string


if __name__ == '__main__' :
    a = input("Enter a String:")
    b = input("Enter a substring/character: ")
    print(cleanstring(a, b))
