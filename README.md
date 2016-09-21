A library for training and applying probabilistic context-free grammars to
text.

* Kasami, T. (1965). An efficient recognition and syntax analysis algorithm
  for context-free languages. (No. Scientific-2). Hawaii University, Dept. of
  Electrical Engineering.

# Example use

```python
>>> from bllipparser import RerankingParser
>>>
>>> from kasami import TreeScorer
>>> from kasami.normalizers import bllip
>>>
>>> # Loading WSJ-PTB3 treebank into bllip's RerankingParser
... bllip_rrp = RerankingParser.fetch_and_load('WSJ-PTB3')

>>> bllip_parse = lambda s: bllip.normalize_tree(bllip_rrp.parse(s)[0].ptb_parse)
>>>
>>> tree = bllip_parse("I am a little teapot")
>>> print(tree)
(S1 (S (NP (PRP 'I')) (VP (VBP 'am') (NP (DT 'a') (JJ 'little') (NN 'teapot')))))
>>> print(tree.format(depth=1))
	(S1
		(S
			(NP
				(PRP 'I')
			)
			(VP
				(VBP 'am')
				(NP
					(DT 'a')
					(JJ 'little')
					(NN 'teapot')
				)
			)
		)
	)
>>>
>>> for production in tree:
...     print(str(production))
...
(S1 S)
(S NP VP)
(NP PRP)
(PRP 'I')
(VP VBP NP)
(VBP 'am')
(NP DT JJ NN)
(DT 'a')
(JJ 'little')
(NN 'teapot')
>>> sentences = ["I am a little teapot",
...              "Here is my handle",
...              "Here is my spout",
...              "When I get all steamed up I just shout tip me over and pour me out",
...              "I am a very special pot",
...              "It is true",
...              "Here is an example of what I can do",
...              "I can turn my handle into a spout",
...              "Tip me over and pour me out"]
>>>
>>>
>>> teapot_grammar = TreeScorer.from_tree_bank(bllip_parse(s) for s in sentences)
>>>
>>> teapot_grammar.score(bllip_parse("Here is a little teapot"))
8.333333333333338e-05
>>> teapot_grammar.score(bllip_parse("It is my handle"))
6.751543209876548e-05
>>> teapot_grammar.score(bllip_parse("I am a spout"))
3.038194444444445e-05
>>> teapot_grammar.score(bllip_parse("Your teapot is gay"))
1.8754286694101494e-05
>>> teapot_grammar.score(bllip_parse("Your mom's teapot is asldasnldansldal"))
1.1721429183813438e-07
```

# Author
* Aaron Halfaker -- https://github.com/halfak

... and substantially informed by https://github.com/aetilley
