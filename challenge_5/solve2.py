#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib
import itertools


def can_be_twice(fragments, half):
    total = 0
    i = 0
    while total < half:
        total += fragments[i][1]
        i += 1
    return total == half


def is_clean(fragments, half):
    sequence = "".join([x[0] for x in fragments])
    return sequence[0: half] == sequence[half:]


def get_index(adn_fragments, selected):
    index = []
    for element in selected:
        index.append(adn_fragments.index(element[0])+1)
    return sorted(index)


def clean(adn_sequence):
    adn_fragments = adn_sequence.split()
    adn_list = [(x, len(x)) for x in adn_fragments]
    n_fragments = len(adn_list)
    for n in xrange(2, n_fragments + 1):
        fragments_combinations = itertools.combinations(adn_list, n)
        for combination in fragments_combinations:
            size = sum([x[1] for x in combination])
            if (size % 2 == 0):
                half = size/2
                possibles = [
                    permutation
                    for permutation in itertools.permutations(combination)
                    if can_be_twice(permutation, half)]
                for fragments in possibles:
                    if is_clean(fragments, half):
                        return get_index(adn_fragments, fragments)
    return get_index(adn_fragments, combination)


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
    # adn_client("TEST")
    # adn_client("SUBMIT")
    # print clean("CACctGcGG GgtacctT aAGCAgag AGcaaA TGcgCcAA AGcaaAca cGGGT CAtc tgTC gcggG TTACACctG tcCtAGgG GTgcggG CgcTTA caCgc GcaCAaAc")
    print clean("ATcGgct Ggct CGATCcGCT GatTAcT Cgcttc gcAC TtaCTc aaGATc tTGTaaG CTtAa GATCcG AATgC AATg tAatTGT")
