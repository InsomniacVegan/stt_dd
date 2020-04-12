class Grid:
    """Base grid stores geometries for creating system"""

    def __init__(self,
                 space   = None,
                 n_space = None,  ):

        import numpy as np

        # Test each dimension is discretized
        if(len(space)) != len(n_space):
            raise ValueError("Spatial dimensions do not match spatial discretization dimensions")

        self.n_dims  = len(space)
        self.space   = space
        self.n_space = n_space
        self.d_space = np.divide(np.array(self.space), np.array(self.n_space))

        # Set up dimension lists for field and scalar grids as templates for ndarray
        self.grid_dim        = list(n_space)
        self.scalar_grid_dim = self.grid_dim.copy()
        self.field_grid_dim  = self.grid_dim.copy()
        self.scalar_grid_dim.append(1)
        self.field_grid_dim.append(3)
