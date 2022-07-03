#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        mytuple = (0, None)
        return mytuple
    else:
        mytuple = (len(sentence), sentence[0])
        return mytuple
