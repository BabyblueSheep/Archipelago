import typing
from Options import Choice, Toggle, Option, DeathLink, Range


class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2


class TimerTrap(BaseTrapWeight):
    """Likelihood of a receiving a trap which starts Pizza Time earlier than usual."""
    display_name = "Timer Trap Weight"


class StunTrap(BaseTrapWeight):
    """Likelihood of a receiving a trap which stuns you temporarily."""
    display_name = "Stun Trap Weight"


class TransformationTrap(BaseTrapWeight):
    """Likelihood of a receiving a trap which gives you a random transformation."""
    display_name = "Transformation Trap Weight"


class TrapFillPercentage(Range):
    """Replace a percentage of junk items in the item pool with random traps."""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class LevelShuffle(Toggle):
    """Whether levels are shuffled."""
    display_name = "Level Shuffle"


class RankRequirement(Choice):
    """What rank is required to send items upon level completion."""
    display_name = "Required Rank"
    option_d = "D"
    option_c = "C"
    option_b = "B"
    option_a = "A"
    option_s = "S"
    option_p = "P"
    default = option_d


class JudgementRequirement(Choice):
    """Determines what Final Judgement is needed"""
    display_name = "Required Judgement"
    option_you_suck = 0
    option_confused = 1
    option_thats_the_one_officer = 2
    option_no_judgement = 3
    option_not_bad_not_bad_at_all = 4
    option_wow = 5
    default = option_you_suck


class JohnNeeded(Toggle):
    """Determines whether you need to revive John to finish the run."""
    display_name = "Required John"


class SecretLocation(Toggle):
    """Whether secret entrances grant checks."""
    display_name = "Secret Checks"


class TowerSecretTreasure(Toggle):
    """Whether finding the secret topping in a level counts as a check."""
    display_name = "Tower Secret Treasure"


pizza_tower_options: typing.Dict[str, type(Option)] = {
    "death_link": DeathLink,

    "secret_check": SecretLocation,
    "treasure_check": TowerSecretTreasure,

    "timer_trap": TimerTrap,
    "stun_trap": StunTrap,
    "transformation_trap": TransformationTrap,
    "trap_fill_percentage": TrapFillPercentage,

    "shuffle_level": LevelShuffle,

    "rank_needed": RankRequirement,
    "goal": JudgementRequirement,
    "john": JohnNeeded,
}
