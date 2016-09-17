from deltas import RegexTokenizer

from .productions import Production, SymbolProduction, TerminalProduction


class Node(Production):
    pass

    def format(self, depth):
        raise NotImplementedError()


class TerminalNode(Node, TerminalProduction):
    pass

    def format(self, depth=0):
        return "\t" * depth + str(self)

    def __iter__(self):
        yield TerminalProduction(self.source, self.produces)


class SymbolNode(Node, SymbolProduction):
    def __init__(self, source, targets):
        for target in targets:
            if not isinstance(target, Node):
                raise ValueError(
                    "target {0} should be a Node, but got {1} instead"
                    .format(repr(target), type(target)))

        Node.__init__(self, source, tuple(targets))

    def __repr__(self):
        return "{0}({1}, {2})".format(
            self.__class__.__name__, repr(self.source), repr(self.produces))

    def __iter__(self):
        yield SymbolProduction(self.source,
                               tuple(t.source for t in self.produces))

        for target in self.produces:
            yield from iter(target)

    def format(self, depth=0):
        return ("\t" * depth + "(" + self.source + "\n" +
                "\n".join(t.format(depth + 1) for t in self.produces) + "\n" +
                "\t" * depth + ")")


tokenizer = RegexTokenizer([
    ("open_b", r"\("),
    ("close_b", r"\)"),
    ("symbol", r"[^ \(\)'\"]+"),
    ("literal", r"'[^']+'|" + r'"[^"]+"')
])


def parse(line):
    tokens = tokenizer.tokenize(line)
    return _parse(tokens)


def _parse(tokens, offset=0):
    if tokens[offset].type != "open_b":
        raise ValueError("Parse at {0} does not start with {1}, but rather {2}"
                         .format(offset, "(", tokens[offset]))
    elif tokens[offset + 1].type != "symbol":
        raise ValueError("Parse at {0} does not have a symbol, but rather {2}"
                         .format(offset + 1, tokens[offset + 1].type))

    symbol = str(tokens[offset + 1])

    if tokens[offset + 2].type == "open_b":
        nodes = tuple(_parse(tokens, sub_offset)
                      for sub_offset in _get_sub_b_offsets(tokens, offset))

        return SymbolNode(symbol, nodes)

    elif tokens[offset + 2].type == "literal":
        return TerminalNode(symbol, str(tokens[offset + 2].strip("'\"")))


def _get_sub_b_offsets(tokens, offset):
    if tokens[offset].type != "open_b":
        raise ValueError("Parse at {0} does not start with {1}, but rather {2}"
                         .format(offset, "(", tokens[offset]))
    depth = 0
    for i, token in enumerate(tokens[offset:]):
        if token.type == "open_b":
            depth += 1
            if depth == 2:
                yield offset + i
        elif token.type == "close_b":
            depth -= 1

        if depth == 0:
            break
