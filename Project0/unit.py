import math

class Unit:

    CHAOTIC = "chaotic"
    US = "us"
    THEM = "them"

    def __init__(self, attack_power, max_hit_points, x, y, team, range = math.sqrt((2))):
        self._attack_power = attack_power
        self._max_hit_points = max_hit_points
        self._hit_points = max_hit_points
        self._range = range
        self._x_position = x
        self._y_position = y
        self._team = team

# https://umgpt.umich.edu/ - write get functions for class
    def get_attack_power(self):
        return self._attack_power

    def get_max_hit_points(self):
        return self._max_hit_points

    def get_hit_points(self):
        return self._hit_points

    def get_range(self):
        return self._range

    def get_x_position(self):
        return self._x_position

    def get_y_position(self):
        return self._y_position

    def get_team(self):
        return self._team

    def set_hit_points(self, hit_points):
        self._hit_points = hit_points
        if self._hit_points < 0:
            self._hit_points = 0
        if self._hit_points > self._max_hit_points:
            self._hit_points = self._max_hit_points

    def _is_within_range(self, target : Unit):
        return (self._range >=
            math.sqrt(
                ( self._x_position - target.get_x_position() )**2
                + ( self._y_position - target.get_y_position() )**2) )

    def _should_attack(self, target: Unit):
        return self._team == self.CHAOTIC or self._team != target.get_team()

    def attack(self, target):
        if self._is_within_range(target) and self._should_attack(target):
            target.set_hit_points(target.get_hit_points() - self._attack_power)

    def move(self, x, y):
        raise NotImplementedError()
