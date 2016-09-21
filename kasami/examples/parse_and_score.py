from bllipparser import RerankingParser

from kasami import TreeScorer
from kasami.normalizers import bllip

# Loading WSJ-PTB3 treebank into bllip's RerankingParser
bllip_rrp = RerankingParser.fetch_and_load('WSJ-PTB3')
bllip_parse = lambda s: bllip.normalize_tree(bllip_rrp.parse(s)[0].ptb_parse)

tree = bllip_parse("I am a little teapot")
print(tree)
print(tree.format(depth=1))

for production in tree:
    print(str(production))

sentences = ["I am a little teapot",
             "Here is my handle",
             "Here is my spout",
             "When I get all steamed up I just shout tip me over and pour me out",
             "I am a very special pot",
             "It is true",
             "Here is an example of what I can do",
             "I can turn my handle into a spout",
             "Tip me over and pour me out"]


teapot_grammar = TreeScorer.from_tree_bank(bllip_parse(s) for s in sentences)

teapot_grammar.score(bllip_parse("Here is a little teapot"))
teapot_grammar.score(bllip_parse("It is my handle"))
teapot_grammar.score(bllip_parse("I am a spout"))
teapot_grammar.score(bllip_parse("Your teapot is gay"))
teapot_grammar.score(bllip_parse("Your mom's teapot is asldasnldansldal"))
