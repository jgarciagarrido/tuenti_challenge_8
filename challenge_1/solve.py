#!/usr/bin/env python
def holes_in_waffle(vlines, hlines):
    return (vlines-1) * (hlines-1)

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        vlines, hlines = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, holes_in_waffle(vlines, hlines))
