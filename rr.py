    self.nbits = n
    items = []
    for x in xrange(n+1):
        ones = x
        zeros = n-x
        item = []
        for i in xrange(ones):
            item.append(1)
        for i in xrange(zeros):
            item.append(0)
        items.append(item)
    perms = set()
    for item in items:
        for perm in itertools.permutations(item):
            perms.add(perm)
    perms = list(perms)
    perms.sort()
    self.to_bits = {}
    self.to_code = {}
    for x in enumerate(perms):
        self.to_bits[x[0]] = ''.join([str(y) for y in x[1]])
        self.to_code[''.join([str(y) for y in x[1]])] = x[0]
