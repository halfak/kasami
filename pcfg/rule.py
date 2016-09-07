from .symbol import Symbol


class Rule:
    """A transformation (rewrite) rule for any CFG"""

    def __init__(self, source, targets, proba=None):
        """
        Source should be a Variable
        targets should be a tuple of 0 or more Symbols
        """

        if not isinstance(source, Symbol):

        self.source = source
        self.targets = targets
        self.proba = float(proba) if proba is not None else None

        self.check_Rule()

    def arity(self):
        """Return number of target symbols."""
        return len(self.targets)

    def substitute(self, sub_dict):
        """
        Make substitutions (in the source or targets) according to dictionary sub_dict which has
        Symbols as keys and Symbols as values.
        """
        source = self.source()
        if source in sub_dict.keys():
            new_source = sub_dict[source]
        else:
            new_source = source
        new_targets = ()
        for target in self.targets():
            if target in sub_dict.keys():
                new_target = sub_dict[target]
            else:
                new_target = target
            new_targets = new_targets + (new_target,)
        new_rule = Rule(new_source, new_targets)
        return new_rule

    def substitute_many(self, var, new_targs):
        """
        Perhaps currently poorly named, this method allows Not for more than
        one *kind* of substitution
        (as does the method substitute(), but rather for more than one symbol to be substituted
        in the place of one symbol (which substitute() does not currently allow).
        The resulting Rule may therefore be of a different arity than that of the
        instance on which this
        method is called.
        """
        assert type(new_targs) is tuple
        same_source = self.source()
        new_targets = ()
        for target in self.targets():
            if target == var:
                new_targets = new_targets + new_targs
            else:
                new_targets = new_targets + (target,)
        new_rule = Rule(same_source, new_targets)
        return new_rule

    def __str__(self):
        return self._source.__str__() + " " + self._targets.__str__()

    def __eq__(self, other):
        return self._source == other._source and self._targets == other._targets

    def __hash__(self):
        return hash((self._source, self._targets))

    def __repr__(self):
        return self._source.__str__() + " " + self._targets.__str__()

    def to_json(self):
        return {'source': self.source, 'targets': self.targets,
                'proba': self.proba}
