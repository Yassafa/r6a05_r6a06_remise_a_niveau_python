from typing import Protocol


class RuminationStrategy(Protocol):

    def calculer_lait(self, vache, panse_avant):
        ...

    def stocker_lait(self, vache, lait):
        ...

    def post_rumination(self, vache, panse_avant, lait):
        ...
