from strategy import RuminationStrategy


class NoMilkStrategy:

    def calculer_lait(self, vache, panse_avant):
        return 0.0

    def stocker_lait(self, vache, lait):
        return

    def post_rumination(self, vache, panse_avant, lait):
        return


strategy: RuminationStrategy = NoMilkStrategy()
