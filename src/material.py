class Material:
    """Main material class containing material parameters"""

    def __init__(self,
                 mag        = None,
                 sa_equil   = None,
                 diff       = None,
                 polar_con  = None,
                 polar_diff = None,
                 len_pre    = None,
                 len_dph    = None,
                 len_sf     = None, ):

        # Initialize properties

        # Normalize magnetization if present
        if np.square(np.sum(mag)) > 0:
            self.mag = np.divide(mag, np.linalg.norm(mag))
        else:
            self.mag = mag

        self.sa_equil = sa_equil
        self.diff = diff
        self.polar_con = polar_con
        self.polar_diff = polar_diff
        self.len_pre = len_pre
        self.len_dph = len_dph
        self.len_sf = len_sf

        return
