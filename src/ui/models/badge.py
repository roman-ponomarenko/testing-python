from collections import namedtuple
from enum import Enum

# Define a namedtuple for the structure
BadgeInfo = namedtuple("BadgeInfo", ["label"])


class Badge(Enum):
    # Members are defined as BadgeInfo instances
    Demo = BadgeInfo("Demo")
    Classical = BadgeInfo("Classical")
    Pytest = BadgeInfo("Pytest")

    @property
    def label(self) -> str:
        return self.value.label
