
import random
import pygame as pg


class _State(object):
    """Base class for all game states"""
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.game_data = {}
        self.music = None
        self.music_title = None
        self.previous_music = None

   

def create_game_data_dict():
        player_items = {'GOLD': dict([('quantity',100),
                                  ('value',0)]),
                    'Healing Potion': dict([('quantity',2),
                                            ('value',15)]),
                    'Ether Potion': dict([('quantity',1),
                                          ('value', 15)]),
                    'Rapier': dict([('quantity', 1),
                                    ('value', 50),
                                    ('power', 9)]),
                    'equipped weapon': 'Rapier',
                    'equipped armor': []}

    player_health = {'current': 70,
                     'maximum': 70}

    player_magic = {'current': 70,
                    'maximum': 70}

    player_stats = {'health': player_health,
                    'Level': 1,
                    'experience to next level': 30,
                    'magic': player_magic,
                    'attack points': 10,
                    'Defense Points': 10}


    data_dict = {'last location': None,
                 'last state': None,
                 'last direction': 'down',
                 'king item': 'GOLD',
                 'old man item': {'ELIXIR': dict([('value',1000),
                                                  ('quantity',1)])},
                 'player inventory': player_items,
                 'player stats': player_stats,
                 'treasure1': True,
                 'treasure2': True,
                 'treasure3': True,
                 'treasure4': True,
                 'treasure5': True,
                 'start of game': True,
                 'talked to king': False,
                 'old man quest complete': False,
                 'talked to old man`s daugther': False,
                 'has daughter elixir': False,
                 'elixir received': False,
                 'old man gift': '',
                 'battle type': '',
                 'princes quest': False,
                 'princes crown': False,
                 'daughters item': 'Potion'
    }

    return data_dict
