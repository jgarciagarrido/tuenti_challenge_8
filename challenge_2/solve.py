#!/usr/bin/env python
# -*- coding: utf-8 -*-


def numeric_base(code):
    return len(code)


def digit(n):
    if n < 10:
        return chr(ord('0') + n)
    else:
        return chr(ord('a') + n - 10)


def max_possible(base):
    return ''.join([digit(i) for i in xrange(base-1, -1, -1)])


def min_possible(base):
    return '10'+''.join([digit(i) for i in xrange(2, base)])


def hidden_number(code):
    base = numeric_base(s)
    min_number = int(min_possible(base), base)
    max_number = int(max_possible(base), base)
    return max_number - min_number


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        print "Case #{}: {}".format(i, hidden_number(s))
