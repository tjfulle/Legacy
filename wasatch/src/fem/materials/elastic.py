import numpy as np

from src.fem.materials._material import Material
import src.base.consts as consts
from src.base.tensor import iso, dev
from src.base.errors import WasatchError

class Elastic(Material):
    name = "elastic"
    mid = 1
    def __init__(self):
        """Instantiate the Elastic material

        """
        super(Elastic, self).__init__()
        self.register_parameters({"E": 0, "NU": 1})

    def setup(self, pdict):
        """Set up the Elastic material

        Parameters
        ----------
        pdict : dict
            Parameter dictionary

        """
        self.parse_input_parameters(pdict)
        self._check_params()

        nu = self._params[self.NU]

        # Bulk modulus, Youngs modulus and Poissons ratio
        self.K = self._params[self.E] / 3. / (1. - 2. * nu)
        self.G = self._params[self.E] / 2. / (1. + nu)

        # compute the constant stiffness
        Eh = self._params[self.E] / (1. + nu) / (1. - 2 * nu)
        self.C = Eh * np.array([[1. - nu, nu, nu, 0, 0, 0],
                                [nu, 1. - nu, nu, 0, 0, 0],
                                [nu, nu, 1. - nu, 0, 0, 0],
                                [0, 0, 0, (1. - 2 * nu) / 2., 0, 0],
                                [0, 0, 0, 0, (1. - 2 * nu) / 2., 0],
                                [0, 0, 0, 0, 0, (1. - 2 * nu) / 2.]],
                               dtype=np.float)

    def _check_params(self):
        """Check parameters and set defaults

        """
        if self._params[self.E] < 0.:
            raise WasatchError("Young's modulus E must be > 0")
        if not -1 < self._params[self.NU] < .5:
            raise WasatchError("Poisson's ratio NU out of bounds")
        return

    def set_up(self, *args, **kwargs):
        pass

    def update_state(self, dt, d, stress, xtra):
        """Compute updated stress given strain increment

        Parameters
        ----------
        dt : float
            Time step

        d : array_like
            Deformation rate

        stress : array_like
            Stress at beginning of step

        xtra : array_like
            Extra variables

        Returns
        -------
        S : array_like
            Updated stress

        xtra : array_like
            Updated extra variables

        """
        dstrain = d * dt
        dstress = 3. * self.K * iso(dstrain) + 2 * self.G * dev(dstrain)
        return stress + dstress, xtra

    def stiffness(self, dt, d, stress, xtra):
        """Return the constant stiffness
        dt : float
            time step

        d : array_like
            Deformation rate

        stress : array_like
            Stress at beginning of step

        """
        return self.C
