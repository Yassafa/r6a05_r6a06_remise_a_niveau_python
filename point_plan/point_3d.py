from point_plan.point_plan import PointPlan


class Point3D(PointPlan):
    def __init__(self, x: float = None, y: float = None, z: float = None):
        super().__init__(x, y)
        self._azimut: float = z

    def from_point(self):
        return Point3D(self._abscisse, self._ordonnee, self._azimut)

    @property
    def azimut(self):
        return self._azimut

    @azimut.setter
    def azimut(self, z: float):
        self._azimut = z

    def __str__(self):
        return ("Point3D :" + super().__str__() +
                "azimut=" + str(self._azimut))
