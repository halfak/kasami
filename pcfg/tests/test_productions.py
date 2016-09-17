from nose.tools import eq_

from ..productions import SymbolProduction, TerminalProduction


def test_productions():
    tp = TerminalProduction("NN", "foo")
    eq_(tp.produces, "foo")
    eq_(str(tp), "(NN 'foo')")
    eq_(repr(tp), "TerminalProduction('NN', 'foo')")

    sp = SymbolProduction("NN", ["VP", "ADJ"])
    eq_(sp.produces, ("VP", "ADJ"))
    eq_(str(sp), "(NN VP ADJ)")
    eq_(repr(sp), "SymbolProduction('NN', ('VP', 'ADJ'))")
