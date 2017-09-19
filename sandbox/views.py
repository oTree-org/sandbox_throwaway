from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class NoDropPage(Page):
    def is_displayed(self):
        group_has_dropout = any([True for p in self.group.get_players() if p.participant.vars.get('dropout', False)])
        return not group_has_dropout


class MyPage(NoDropPage):
    timeout_seconds = 10

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['dropout'] = True


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        group_has_dropout = any([True for p in self.group.get_players() if p.participant.vars.get('dropout', False)])
        return not group_has_dropout

def after_all_players_arrive(self):
        pass


class Results(NoDropPage):
    pass


class DeadEnd(Page):
    def is_displayed(self):
        group_has_dropout = any([True for p in self.group.get_players() if p.participant.vars.get('dropout', False)])
        return group_has_dropout and self.round_number == Constants.num_rounds


page_sequence = [
    MyPage,
    ResultsWaitPage,
    DeadEnd,
    Results,
]
