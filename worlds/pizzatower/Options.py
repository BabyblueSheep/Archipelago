from dataclasses import dataclass
import typing
from Options import Choice, Toggle, DeathLink, Range, PerGameCommonOptions


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
    """Likelihood of a receiving a trap which shortens the timer during Pizza Time."""
    display_name = "Timer Trap Weight"


class TimerTrapReduce(Range):
    """The amount of seconds reduced when receiving a Timer Trap."""
    display_name = "Timer Trap Time Reduced"
    range_start = 5
    range_end = 60
    default = 10


class StunTrap(BaseTrapWeight):
    """Likelihood of a receiving a trap which stuns you temporarily."""
    display_name = "Stun Trap Weight"


class TransformationTrap(BaseTrapWeight):
    """Likelihood of a receiving a trap which gives you a random transformation."""
    display_name = "Transformation Trap Weight"


class TransformationTrapTime(Range):
    """The amount of seconds a transformation trap lasts."""
    display_name = "Transformation Trap Time"
    range_start = 2
    range_end = 30
    default = 10


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


class TowerSecretTreasure(Toggle):
    """Whether finding the secret topping in a level counts as a check."""
    display_name = "Tower Secret Treasure"


class BossKeys(Choice):
    """Chooses how boss keys are handled.
    Bosses Defeated: bosses need to be defeated in order to access the next floor.
    Keys Randomised: keys need to be gotten from players to access the next floor.
    Both: bosses need to be defeated and keys have to be gotten from players to access the next floor.
    """
    display_name = "Boss Keys"
    option_bosses_defeated = 0
    option_keys_randomised = 1
    option_both = 2


class PumpkinHunt(Toggle):
    """Whether Pumpkin Hunt should be available"""
    display_name = "Pumpkin Hunt"


class TowerSecretEye(Toggle):
    """Whether finding any of the 3 secret eyes in a level counts as a check."""
    display_name = "Secrets"


@dataclass
class PizzaTowerOptions(PerGameCommonOptions):
    death_link: DeathLink

    boss_keys: BossKeys
    treasure_check: TowerSecretTreasure
    secret_eye_check: TowerSecretEye
    pumpkin_hunt: PumpkinHunt

    timer_trap: TimerTrap
    timer_reduce: TimerTrapReduce
    stun_trap: StunTrap
    transformation_trap: TransformationTrap
    transformation_time: TransformationTrapTime
    trap_fill_percentage: TrapFillPercentage

    shuffle_level: LevelShuffle

    rank_needed: RankRequirement
    goal: JudgementRequirement
    john: JohnNeeded
