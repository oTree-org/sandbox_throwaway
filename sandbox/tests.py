from otree.api import Currency as c, currency_range, Submission
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        group_has_dropout = any([True for p in self.group.get_players() if p.participant.vars.get('dropout', False)])
        if group_has_dropout:
            if self.player.round_number == Constants.num_rounds:
                yield Submission(views.DeadEnd)
            else:
                return
        else:
            if random.random() < 0.2:
                yield Submission(views.MyPage, timeout_happened=True)
            else:
                yield Submission(views.MyPage)
            group_has_dropout = any(
                [True for p in self.group.get_players() if p.participant.vars.get('dropout', False)])
            if not group_has_dropout:
                yield (views.Results)
