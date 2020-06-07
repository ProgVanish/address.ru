from natasha import MorphVocab
from natasha import AddrExtractor
import csv, os
morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)
with open('bad.csv', 'r+', encode="utf8) as f:
    reader = csv.reader(f)
    for row in reader:
        lines = row[1]
        a = list(addr_extractor(lines))
        data = [row[0], row[1], a]
        with open('test.csv', 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
