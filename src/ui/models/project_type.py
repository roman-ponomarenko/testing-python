from collections import namedtuple
from enum import Enum

# Define a namedtuple for the structure
ProjectInfo = namedtuple("ProjectInfo", ["locator", "label"])


class ProjectType(Enum):
    # Assign namedtuple instances to members
    CLASSICAL = ProjectInfo("#classical", "Classical Project")
    BDD = ProjectInfo("#bdd", "BDD Project")

    @property
    def locator(self):
        return self.value.locator

    @property
    def label(self):
        return self.value.label
