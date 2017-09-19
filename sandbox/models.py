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
    players_per_group = 3
    num_rounds = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    ...


class Player(BasePlayer):
    pass
