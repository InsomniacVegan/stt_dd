class Material:
    """Main material class containing material parameters"""

    def __init__(self, params):
        import numpy as np

        # Initialize properties
        self.params = {}
        for p_name, p_val in params.items():
            if p_name == 'mag' and (np.square(np.sum(p_val)) > 0):
                self.params[p_name] = np.divide(p_val, np.linalg.norm(p_val))
            else:
                self.params[p_name] = p_val
