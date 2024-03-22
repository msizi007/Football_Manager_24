# Attributes
# name: str  
# position: Enum[Position]
# secondary_positions: list[Position]
# age: int
# DOB: date
# is_active: bool
# is_international_player: bool
# international_caps: int
# international_goals: int
# nation: Nation
# club: Club
# value: int
# max_value: int
# wages_per_week: float
# club_role: Enum[ClubRole]
# attributes: PlayerAttributes
# reputation: Enum[Reputation]

class Player:
    def __init__(self, name, position, secondary_positions, age, DOB, is_active, is_international_player, international_caps, international_goals, nation, club, value, max_value, wages_per_week, club_role, attributes, reputation):
        self.name = name
        self.position = position
        self.secondary_positions = secondary_positions
        self.age = age
        self.DOB = DOB
        self.is_active = is_active
        self.is_international_player = is_international_player
        self.international_caps = international_caps
        self.international_goals = international_goals
        self.nation = nation
        self.club = club
        self.value = value
        self.max_value = max_value
        self.wages_per_week = wages_per_week
        self.club_role = club_role
        self.attributes = attributes
        self.reputation = reputation