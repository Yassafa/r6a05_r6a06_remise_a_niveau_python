from vaches.exceptions import InvalidVacheException
from vaches.vache import Vache


class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 40.0

    def __init__(self, petitNom, poids):
        super().__init__(petitNom, poids)
        self._lait_disponible = 0.0
        self._lait_total_produit = 0.0
        self._lait_total_traite = 0.0

    @property
    def lait_disponible(self):
        return self._lait_disponible

    @property
    def lait_total_produit(self):
        return self._lait_total_produit

    @property
    def lait_total_traite(self):
        return self._lait_total_traite

    def __str__(self):
        return "Vache à lait " + self.nom

    def traire(self, litres):
        if litres <= 0:
            raise InvalidVacheException("Litres de traite trop faible")
        elif litres > self.lait_disponible:
            raise InvalidVacheException("Litres de traite supérieurs à disponible")
        else:
            self._lait_disponible -= litres
            self._lait_total_traite += litres
            return litres

    def _calculer_lait(self, panse_avant):
        lait = VacheALait.RENDEMENT_LAIT * panse_avant
        return lait

    def _stocker_lait(self, lait):
        self._lait_disponible += lait
        self._lait_total_produit += lait
        if self.lait_disponible > VacheALait.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Producion max dépassée")
