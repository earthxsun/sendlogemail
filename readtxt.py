import codecs

with codecs.open('aaa.txt', encoding='GB2312') as fp:
    # Create a text/plain message
    msg = fp.read()
    print(msg)

