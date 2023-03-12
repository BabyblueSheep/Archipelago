import typing
from Options import Choice, Toggle, Option, DeathLink


class LevelShuffle(Toggle):
    """Whether levels are shuffled."""
    display_name = "Level Shuffle"


class TowerSecretTreasure(Toggle):
    """Whether finding the secret topping in a level counts as a check."""
    display_name = "Tower Secret Treasure"


class RankRequirement(Choice):
    """What rank is required to send items upon level completion."""
    display_name = "Required Rank"
    option_d = "D"
    option_c = "C"
    option_b = "B"
    option_a = "A"
    option_s = "S"
    option_p = "P"


class JudgementRequirement(Choice):
    """Determines what Final Judgement is needed"""
    display_name = "Required Judgement"
    option_you_suck = 0
    option_confused = 1
    option_thats_the_one_officer = 2
    option_no_judgement = 3
    option_not_bad_not_bad_at_all = 4
    option_wow = 5


class JohnNeeded(Toggle):
    """Determines whether you need to revive John to finish the run."""
    display_name = "Required John"


pizza_tower_options: typing.Dict[str, type(Option)] = {
    "death_link": DeathLink,
    "shuffle_level": LevelShuffle,
    "rank_needed": RankRequirement,
    "tower_secret_treasure": TowerSecretTreasure,
    "john": JohnNeeded,
    "goal": JudgementRequirement
}
