from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants



class MyPage(Page):
    timeout_seconds = 10

    def is_displayed(self):
        return not self.group.has_dropout()

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['dropout'] = True


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        return not self.group.has_dropout()


class DeadEnd(Page):
    def is_displayed(self):
        return self.group.has_dropout() and self.round_number == Constants.num_rounds


class Results(Page):
    def is_displayed(self):
        return not self.group.has_dropout()

page_sequence = [
    MyPage,
    ResultsWaitPage,
    DeadEnd,
    Results,
]
