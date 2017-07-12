#!/usr/bin/env python

import sys, string
# the global list of [word, frequency] pairs
word_freqs = []

# iterate through the file one line at a time 
for line in open('/Users/pratikshetty/Work/workshops/hde_inst/searchTerms'):
    start_char = None
    i = 0
    for c in line:
        if start_char == None:
            if c.isalnum():
                # We found the start of a word
                start_char = i
        else:
            if not c.isalnum():
                # We found the end of a word. Process it
                found = False
                word = line[start_char:i].lower()
                pair_index = 0
                # Let's see if it already exists
                for pair in word_freqs:
                    if word == pair[0]:
                        pair[1] += 1
                        found = True
                        found_at = pair_index
                        break
                    pair_index += 1
                if not found:
                    word_freqs.append([word, 1])
                elif len(word_freqs) > 1:
                    # We may need to reorder
                    for n in reversed(range(pair_index)):
                        if word_freqs[pair_index][1] > word_freqs[n][1]:
                            # swap
                            word_freqs[n], word_freqs[pair_index] = word_freqs[pair_index], word_freqs[n]
                            pair_index = n
                # Let's reset
                start_char = None
        i += 1

with open ("sortedTerms.tsv", "a") as f:
    f.write("term\tfrequency" + "\n")
    for tf in word_freqs:
        #print tf[0], ' - ', tf[1]
        f.write("{}\t{}\n".format(tf[0], tf[1]))
