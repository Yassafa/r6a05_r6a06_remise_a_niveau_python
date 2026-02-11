from strategy.StandardMilkStrategy import StandardMilkStrategy
from vaches.exceptions import InvalidVacheException
from vaches.vache_a_lait import VacheALait
from nourriture.TypeNourriture import TypeNourriture


class PieNoire(VacheALait):
    COEFFICIENT_NUTRITIONNEL = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    def __init__(self, petitNom, poids):
        super().__init__(petitNom, poids)
        self._strategy_rumination = StandardMilkStrategy()
        self._nombreTacheNoire = 0
        self._nombreTacheBlanche = 0
        self._ration = {}

    @property
    def nombreTacheNoire(self):
        return self._nombreTacheNoire

    @property
    def nombreTacheBlanche(self):
        return self._nombreTacheBlanche

    def __str__(self):
        return "Pie noire " + self.nom

    def brouter(self, quantite, nourriture=None):
        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide.")
        elif nourriture is not None:
            self._ration[nourriture.type] += quantite
        self._panse += quantite
        self._valider_etat()
