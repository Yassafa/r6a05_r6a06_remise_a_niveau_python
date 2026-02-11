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

    def __init__(self, petitNom, age, poids):
        super().__init__(petitNom, age, poids)
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

    def _calculer_lait(self, panse_avant):
        lait = 0
        for nourriture in self._ration.keys():
            lait += self._ration[nourriture].quantite * self.COEFFICIENT_NUTRITIONNEL[nourriture]
        return self.RENDEMENT_LAIT * lait
