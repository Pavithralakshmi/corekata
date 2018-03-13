import collections
s = 'tkhiuiguguygiugiiiogigikgdfsfa'
d = collections.defaultdict(int)
for c in s:
    d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))

