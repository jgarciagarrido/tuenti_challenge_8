#!/usr/bin/env python
# -*- coding: utf-8 -*-

ALL_NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
MINOR_SCALES_KEYS = ["m" + note for note in ALL_NOTES]
MAJOR_SCALES_KEYS = ["M" + note for note in ALL_NOTES]
ALL_SCALES_KEYS = MAJOR_SCALES_KEYS + MINOR_SCALES_KEYS


def flat_translation(note):
    i = ALL_NOTES.index(note[0])-1 % 12
    return ALL_NOTES[i]


def is_flat(note):
    return len(note) == 2 and note[1] == 'b'


def normalize_note(note):
    if is_flat(note):
        return flat_translation(note)
    if note == 'B#':
        return 'C'
    if note == 'E#':
        return 'F'
    return note


def normalize_partiture(partiture):
    return [normalize_note(note) for note in partiture]


def extract_notes(partiture):
    return list(set(normalize_partiture(partiture)))


def generate_scale(note, steps):
    two_octaves = ALL_NOTES + ALL_NOTES
    scale = []
    i = ALL_NOTES.index(note)
    for step in steps:
        scale.append(two_octaves[i])
        i += step
    return scale


def generate_scales_by_type(steps, type):
    scales = {}
    for note in ALL_NOTES:
        scales[type + note] = generate_scale(note, steps)
    return scales


def generate_all_scales():
    minor_scales = generate_scales_by_type([2, 1, 2, 2, 1, 2, 2], 'm')
    major_scales = generate_scales_by_type([2, 2, 1, 2, 2, 2, 1], 'M')
    minor_scales.update(major_scales)
    return minor_scales


def is_partiture_in_scale(notes, scale):
    for note in notes:
        if note not in scale:
            return False
    return True


def possible_scales(all_scales, partiture):
    if len(partiture) == 0:
        return " ".join(ALL_SCALES_KEYS)
    scales = []
    notes = extract_notes(partiture)
    for key in ALL_SCALES_KEYS:
        if is_partiture_in_scale(notes, all_scales[key]):
            scales.append(key)
    if len(scales) == 0:
        return "None"
    return " ".join(scales)


if __name__ == '__main__':
    t = int(raw_input())
    all_scales = generate_all_scales()

    for i in xrange(1, t + 1):
        n = int(raw_input())
        if n > 0:
            partiture = raw_input().strip().split(" ")
        else:
            partiture = []
        scales = possible_scales(all_scales, partiture)
        print "Case #{}: {}".format(i, scales)
