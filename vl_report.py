from proms_rulesets import RuleSet
from proms_rulesets import Rule
from proms_rulesets.rulesets.reports import ExternalReport


class VLReport(RuleSet):
    def __init__(self, g):
        rules = []
        # TODO: implement real list of Rules
        r1 = VLRule1(g)
        rules.append(r1)
        RuleSet.__init__(
            self,
            'Virtual Laboratories Report',
            rules,
            [ExternalReport(g)])  # dependent on ExternalReport and thus PromsReport & PROV-O constraints


class VLRule1(Rule):
    def __init__(self, g):
        self.passed = True
        self.fail_reasons = []

        # TODO: implement Rule logic

        Rule.__init__(
            self,
            'Single Activity',
            'The Report has the same starting & ending Activity',
            'PROMS Ontology',
            self.passed,
            self.fail_reasons,
            1,  # the number of individual tests
            len(self.fail_reasons)  # the number of tests failed
        )
