from vaches.exceptions import InvalidVacheException

class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    RENDEMENT_RUMINATION = 0.25
    _NEXT_ID = 1

    def __init__(self, petitNom, age, poids):
        self._id = self._NEXT_ID
        self._NEXT_ID += 1
        self._petitNom = petitNom
        self._poids = poids
        self._panse = 0
        self._age = age

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
        self._panse += quantite

    def ruminer(self):
        self._calculer_lait(self.panse)
        self._stocker_lait("")
        self._post_rumination()

    def vieillir(self):
        self._age += 1

    def _calculer_lait(self, panse_avant):
        pass

    def _stocker_lait(self, lait):
        pass

    def _post_rumination(self):
        pass

    def _ajouter_panse(self):
        pass

    def _valider_rumination_possible(self):
        pass

    def _valider_etat(self):
        if self.nom.isspace():
            raise InvalidVacheException
