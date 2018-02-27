class Suitor(object):
    # prefList is a list of indices,
    # implicitly defining a bijection
    def __init__(self, id, prefList):
        self.prefList = prefList
        self.rejections = 0
        # rejection count is also an index
        self.id = id

    def preference(self):
        return self.prefList[self.rejections]

    def __repr__(self):
        return repr(self.id)

class Suited(object):
    def __init__(self, id, prefList):
        self.prefList = prefList
        self.held = None
        self.currentSuitors = set()
        self.id = id()

    def reject(self):
        if len(self.currentSuitors) == 0:
            return set()

        if self.held is not None:
            self.currentSuitors.add(self.held)

        self.held = min(self.currentSuitors, key = lambda s: self.prefList.index(s.id))
        rejected = self.currentSuitors - set([self.held])
        self.currentSuitors = set()

        return rejected

    def __repr__(self):
        return repr(self.id)

def stableMarriage(suitors, suiteds):
    unassigned = set(suitors)

    while len(unassigned) > 0:
        for suitor in unassigned:
            choice = suitor.preference()
            suiteds[choice].currentSuitors.add(suitor)
        unassigned = set()

        for suited in suiteds:
            unassigned |= suited.reject()

        for suitor in unassigned:
            suitor.rejections += 1

    return {suited.held: suited for suited in suiteds}
