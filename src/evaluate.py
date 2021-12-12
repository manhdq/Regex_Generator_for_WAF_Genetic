import re
from .const import INDEX_TABLE

__all__ = ['fitness']

score_table = {
    INDEX_TABLE(0x0) : 10,
    INDEX_TABLE(0x1) : 26,
    INDEX_TABLE(0x2) : 26,
    INDEX_TABLE(0x3) : 52,
    INDEX_TABLE(0x4) : 16,
    INDEX_TABLE(0x5) : 16,
    INDEX_TABLE(0x6) : 72,
    INDEX_TABLE(0x7) : 5,
    INDEX_TABLE(0x8) : 1,
    INDEX_TABLE(0x9) : 100,
    INDEX_TABLE(0xa) : 20,
    INDEX_TABLE(0xb) : 20,
    INDEX_TABLE(0xc) : 100,
    INDEX_TABLE(0xd) : 100,
    INDEX_TABLE(0xe) : 100,
    INDEX_TABLE(0xf) : 100,
    INDEX_TABLE(0x10) : 20,
    INDEX_TABLE(0x11) : 30,
    INDEX_TABLE(0x12) : 30,
    INDEX_TABLE(0x13) : 30,
    INDEX_TABLE(0x14) : 30,
}

def fitness(regex, seq, positive=[], negative=[]):
    # init
    score = 1000

    # can Match
    for t in positive:
        if not re.search(regex, t):
            return -1e9

    # Cant Match
    for t in negative:
        if re.search(regex, t):
            return -1e9

    # regex length (-)
    score -= 2 * len(regex)
    if len(regex) > 100 :
        score *= 0.9
        score = int(score)
    
    # or quantity
    if '|' in regex and regex.count('|') < 5:
        score += 60 
    else : 
        score -= 10 *regex.count('|')

    # Converge rate
    for g in set(seq):
        score -= score_table[INDEX_TABLE(ord(g) & 0x7f)]

    # Single purity
    score -= 10 * len(set(seq))
    score -= 10 * len(seq)

    # .* or .+
    score -= 50 * (regex.count('.*') + regex.count('.+'))
    if '.' in regex and len(regex) < 6:
        score -= 100 * (regex.count('.'))

    if regex in ['.*', '.+', '.*.+', '.+.*']:
        return 1e-9

    return score