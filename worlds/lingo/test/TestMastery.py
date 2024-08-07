from . import LingoTestBase


class TestMasteryWhenVictoryIsTheEnd(LingoTestBase):
    options = {
        "mastery_achievements": "22",
        "victory_condition": "the_end",
        "shuffle_colors": "true",
        "shuffle_postgame": "true",
    }

    def test_requirement(self):
        self.assertFalse(self.multiworld.state.can_reach("Orange Tower Seventh Floor", "Region", self.player))

        self.collect_by_name(["Red", "Blue", "Black", "Purple", "Orange"])
        self.assertTrue(self.multiworld.state.can_reach("Orange Tower Seventh Floor", "Region", self.player))
        self.assertTrue(self.can_reach_location("The End (Solved)"))
        self.assertFalse(self.can_reach_location("Orange Tower Seventh Floor - THE MASTER"))

        self.collect_by_name(["Green", "Brown", "Yellow"])
        self.assertTrue(self.can_reach_location("Orange Tower Seventh Floor - THE MASTER"))


class TestMasteryWhenVictoryIsTheMaster(LingoTestBase):
    options = {
        "mastery_achievements": "24",
        "victory_condition": "the_master",
        "shuffle_colors": "true"
    }

    def test_requirement(self):
        self.assertFalse(self.multiworld.state.can_reach("Orange Tower Seventh Floor", "Region", self.player))

        self.collect_by_name(["Red", "Blue", "Black", "Purple", "Orange"])
        self.assertTrue(self.multiworld.state.can_reach("Orange Tower Seventh Floor", "Region", self.player))
        self.assertTrue(self.can_reach_location("Orange Tower Seventh Floor - THE END"))
        self.assertFalse(self.can_reach_location("Orange Tower Seventh Floor - Mastery Achievements"))

        self.collect_by_name(["Green", "Gray", "Brown", "Yellow"])
        self.assertTrue(self.can_reach_location("Orange Tower Seventh Floor - Mastery Achievements"))


class TestMasteryBlocksDependents(LingoTestBase):
    options = {
        "mastery_achievements": "24",
        "shuffle_colors": "true",
        "location_checks": "insanity",
        "victory_condition": "level_2",
    }

    def test_requirement(self):
        self.collect_all_but("Gray")
        self.assertFalse(self.can_reach_location("Orange Tower Basement - THE LIBRARY"))
        self.assertFalse(self.can_reach_location("The Fearless - MASTERY"))

        self.collect_by_name("Gray")
        self.assertTrue(self.can_reach_location("Orange Tower Basement - THE LIBRARY"))
        self.assertTrue(self.can_reach_location("The Fearless - MASTERY"))
