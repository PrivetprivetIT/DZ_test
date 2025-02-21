from units import Missile, NuclearBomb

_missiles = []
_nuclear_bombs = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv

def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)

def nuclear_boom(owner):
    b = NuclearBomb(_canvas, owner)
    _nuclear_bombs.append(b)

def update():
    start = len(_missiles) - 1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def update_nuclear():
    start = len(_nuclear_bombs) - 1
    for i in range(start, -1, -1):
        if _nuclear_bombs[i].is_destroyed():
            del _nuclear_bombs[i]
        else:
            _nuclear_bombs[i].update()

def check_missiles_collection(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersects(tank):
            missile.destroy()
            tank.damage(25)
            return

def check_nuclear_bomb_collection(tank):
    for nuclear_bomb in _nuclear_bombs:
        if nuclear_bomb.get_owner() == tank:
            continue
        if nuclear_bomb.intersects(tank):
            nuclear_bomb.destroy()
            tank.damage(100)
            return