from collections import defaultdict

from . import errors
from .symbol import Variable


def read_lines(training_file_path):
    """Read lines from a file a return an iterator of lists"""
    fi = open(training_file_path, 'r')
    for line in fi:
        fields = line.strip().split(' ')
        yield fields


class CFG:
    """
    A context free grammar.
    """
    TOLERANCE = .00000000000001
    START_SYMBOL_CODE = "S"

    def __init__(self, rules, start_symbol):
        self.rules = rules
        self.start_symbol = start_symbol \
            if start_symbol is not None \
            else self.START_SYMBOL

        self.sources = set()
        self.variables = set()
        self._source2rules = defaultdict(set)
        self._arity2rules = defaultdict(set)
        for rule in self.rules:
            self._source2rules[rule.source].add(rule)
            self._arity2rules[rule.arity()].add(rule)
            self.variables.add(rule.source)
            for var in rule.targets:
                self.variables.add(var)

        self.sources = set(self.source2rules.keys())
        self.terminals = self.variables - self.sources

        if self.start_symbol not in self.sources:
            raise errors.ConstraintError(
                "Start symbol {0} does not appear in sources."
                .format(self.start_symbol))

    def sources(self):
        return self.sources2rules.keys()

    def terminals(self):
        return {target
                for rule in self.rules
                for target in rule.targets()
                if target not in self._source2rules}

    def check_valid_CNF(self):
        # Only rules of arity 1 and 2:
        for rule in self.rules:
            if rule.arity() > 2:
                raise errors.ConjunctiveNormalFormError(
                    "Rule {0} has > 2 arity {1}".format(rule, rule.arity()))

        for rule in self._arity2rule[1]:
            target = rule.target[0]
            if target in self._source2rule:
                invalids = self._source2rule[target]
                raise errors.ConjunctiveNormalFormError(
                    "The unary rule {0} has target {1} ".format(rule, target) +
                    "that is non-terminal in {2}"
                    .format(", ".join(str(r) for r in invalids)))
