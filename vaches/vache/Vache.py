from strategy.NoMilkStrategy import NoMilkStrategy
from vaches.exceptions import InvalidVacheException


class Vache:
    AGE_MAX = 25
    AGE_NAISSANCE = 0
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    PANSE_VIDE = 0.0
    RENDEMENT_RUMINATION = 0.25
    NEXT_ID = 1

    def __init__(self, petitNom, poids):
        self._id = Vache.NEXT_ID
        Vache.NEXT_ID += 1
        self._petitNom = petitNom
        self._strategy_rumination = NoMilkStrategy()
        self._poids = poids
        self._panse = Vache.PANSE_VIDE
        self._age = Vache.AGE_NAISSANCE
        self._valider_etat()

    @property
    def nom(self):
        return self._petitNom

    @property
    def id(self):
        return self._id

    @property
    def poids(self):
        return self._poids

    @property
    def panse(self):
        return self._panse

    @property
    def age(self):
        return self._age

    def __str__(self):
        return "Vache " + self.nom

    def brouter(self, quantite, nourriture=None):
        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide.")
        elif nourriture is not None:
            raise InvalidVacheException("Nourriture fournie à une Vache normale.")
        else:
            self._panse += quantite
            self._valider_etat()

    def ruminer(self):
        self._valider_rumination_possible()
        panse_avant = self.panse
        gain = self.RENDEMENT_RUMINATION * panse_avant
        self._poids += gain
        lait = self._strategy_rumination.calculer_lait(self, panse_avant)
        self._strategy_rumination.stocker_lait(self, lait)
        self._panse = 0.0
        self._strategy_rumination.post_rumination(self, panse_avant, lait)

    def vieillir(self):
        self._age += 1
        self._valider_etat()

    def _ajouter_panse(self):
        pass

    def _valider_rumination_possible(self):
        if self.panse <= 0.0:
            raise InvalidVacheException("Panse vide")

    def _valider_etat(self):
        if self.nom.isspace() or self.nom == "":
            raise InvalidVacheException("Nom vide")
        if self.age < 0 or self.age > self.AGE_MAX:
            raise InvalidVacheException("Âge invalide")
        if self.poids < 0:
            raise InvalidVacheException("Poids négatif")
        if self.panse < 0:
            raise InvalidVacheException("Panse négative")
        if self.panse > self.PANSE_MAX:
            raise InvalidVacheException("Panse trop pleine")
        if self.poids > self.POIDS_MAX:
            raise InvalidVacheException("Poids trop élevé")
