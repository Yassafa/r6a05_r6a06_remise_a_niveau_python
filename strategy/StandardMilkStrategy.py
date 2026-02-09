from strategy import RuminationStrategy
from vaches.exceptions import InvalidVacheException


class StandardMilkStrategy:

    def calculer_lait(self, vache, panse_avant):
        lait = vache.RENDEMENT_LAIT * panse_avant
        return lait

    def stocker_lait(self, vache, lait):
        vache.lait_disponible += lait
        vache.lait_total_produit += lait
        if vache.lait_disponible > vache.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Producion max dépassée")

    def post_rumination(self, vache, panse_avant, lait):
        return


strategy: RuminationStrategy = StandardMilkStrategy()
