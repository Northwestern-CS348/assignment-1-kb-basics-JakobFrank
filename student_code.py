import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        #Assert a fact or rule into the KB (Assume given is not a rule)
        print("Asserting {!r}".format(fact))
        if fact in self.facts:
            pass
        else:
            if isinstance(fact, Fact):
                self.facts.append(fact)
        
    def kb_ask(self, fact):
        #Ask if a fact is in the KB
        print("Asking {!r}".format(fact))
        blist = ListOfBindings()
        for KBFact in self.facts:
            if match(KBFact.statement, fact.statement):
                blist.add_bindings(match(KBFact.statement, fact.statement), [KBFact])
        if not blist:
            return False
        else:
            return blist