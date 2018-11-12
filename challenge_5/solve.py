#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib


def find_start(fragments):
    for fragment_1 in fragments:
        rest = list(fragments)
        rest.remove(fragment_1)
        for fragment_2 in rest:
            if fragment_2.startswith(fragment_1):
                rest.remove(fragment_2)
                return [([fragment_1, fragment_2],
                        fragment_2.replace(fragment_1, "", 1), rest)]
            if fragment_1.startswith(fragment_2):
                rest.remove(fragment_2)
                return [([fragment_2, fragment_1],
                        fragment_1.replace(fragment_2, "", 1), rest)]
    return


def find_next(option):
    next_options = []
    selected, prefix, fragments = option
    for fragment in fragments:
        rest = list(fragments)
        new_selected = list(selected)
        if fragment.startswith(prefix):
            rest.remove(fragment)
            new_selected.append(fragment)
            next_options.append((new_selected,
                                 fragment.replace(prefix, "", 1), rest))
        elif prefix.startswith(fragment):
            rest.remove(fragment)
            new_selected.append(fragment)
            next_options.append((new_selected,
                                 prefix.replace(fragment, "", 1), rest))
    return next_options


def get_index(adn_fragments, selected):
    index = []
    for element in selected:
        index.append(adn_fragments.index(element)+1)
    return sorted(index)


def clean(adn_sequence):
    adn_fragments = adn_sequence.split()
    options = find_start(adn_fragments)
    while len(options) > 0:
        option = options.pop(0)
        next_options = find_next(option)
        for next_option in next_options:
            options.append(next_option)
            if next_option[1] == "":
                return get_index(adn_fragments, next_option[0])
    return None


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
        print str(test + 1) + " -> " + clean_segments
        tn.write(clean_segments+"\n")
        print tn.read_until(">") + tn.read_until("\n")[:-1]
        test += 1


if __name__ == '__main__':
    adn_client("SUBMIT")
