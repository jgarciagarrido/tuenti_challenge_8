#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib
import itertools


def is_clean(sequence):
    n = len(sequence)
    if (n % 2 == 1):
        return False
    half = n / 2
    return sequence[0: half] == sequence[half:]


def get_index(adn_fragments, selected):
    index = []
    for element in selected:
        index.append(adn_fragments.index(element)+1)
    return sorted(index)


def clean(adn_sequence):
    adn_fragments = adn_sequence.split()
    n_fragments = len(adn_fragments)
    possibles_fragments = itertools.permutations(adn_fragments, n_fragments)
    for fragments in possibles_fragments:
        test_sequence = ""
        n = 0
        for fragment in fragments:
            n += 1
            test_sequence += fragment
            if is_clean(test_sequence):
                print fragments[0:n]
                print test_sequence
                return get_index(adn_fragments, fragments[0:n])
    return []


def adn_client(mode):
    tn = telnetlib.Telnet("52.49.91.111", 3241)
    print tn.read_until('"SUBMIT"')
    tn.write(mode + "\n")
    tn.read_until("!\n")
    test = 0
    while test < 20:
        adn_sequence = tn.read_until("\n")
        print adn_sequence
        clean_segments = ",".join([str(x) for x in clean(adn_sequence)])
        print str(test + 1) + " -> " + clean_segments + "\n"
        tn.write(clean_segments+"\n")
        print tn.read_until(">") + tn.read_until("\n")
        test += 1


if __name__ == '__main__':
    adn_client("TEST")
    # adn_client("SUBMIT")
    # print clean("CACctGcGG GgtacctT aAGCAgag AGcaaA TGcgCcAA AGcaaAca cGGGT CAtc tgTC gcggG TTACACctG tcCtAGgG GTgcggG CgcTTA caCgc GcaCAaAc")
