def select_letter(n, s):
    return s[(n - 1) % len(s)]

import re
def isotopes(seq):
    r = re.findall(r'(\d+)([A-Za-z]+)', seq)
    return [(int(m), sym) for m, sym in r]

def read_elements(location, symbol_idx, name_idx, separator='\t', header=True):
    d = {}
    with open(location, encoding='utf-8') as f:
        lines = f.readlines()
    if header:
        lines = lines[1:]
    for line in lines:
        if line.strip() == '':
            continue
        fields = line.strip('\n').split(separator)
        symbol = fields[symbol_idx - 1]
        name = fields[name_idx - 1]
        d[symbol] = name
    return d

def chemist(isoseq, symbol2name):
    iso = isotopes(isoseq)
    return ''.join(select_letter(mass, symbol2name[sym]) for mass, sym in iso)
