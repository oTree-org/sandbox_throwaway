from otree.api import Currency as c, currency_range, Submission
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    cases = [{'timeout': True}, {'timeout': False}]

    def play_round(self):
        has_dropout = self.group.has_dropout()
        if has_dropout and self.player.round_number == Constants.num_rounds:
            yield views.DeadEnd
        if not has_dropout:
            yield Submission(views.MyPage, timeout_happened=self.case['timeout'])
            if not self.group.has_dropout():
                yield views.Results
