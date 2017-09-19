from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sandbox'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def has_dropout(self):
        return any(p.participant.vars.get('dropout') for p in self.get_players())


class Player(BasePlayer):
    pass
