class PointPlan:

    def __init__(self, x: float = None, y: float = None):
        self._abscisse: float = x
        self._ordonnee: float = y

    def from_point(self):
        return PointPlan(self._abscisse, self._ordonnee)

    @property
    def abscisse(self) -> float:
        return self._abscisse

    @abscisse.setter
    def abscisse(self, x: float) -> None:
        self._abscisse = x

    @property
    def ordonnee(self) -> float:
        return self._ordonnee

    @ordonnee.setter
    def ordonnee(self, y: float) -> None:
        self._ordonnee = y

    def __str__(self):
        return ("\nabscisse = " + str(self._abscisse) +
                ", ordonnee=" + str(self._ordonnee))
