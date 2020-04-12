class State:
    """Constructs system using materials"""

    def __init__(self, mats = None):

        import numpy as np

        # Store the materials
        self.mats = mats

        # Find total system size
        self.sys_size    = sum([material.params['thickness'][0] for material in mats])
        self.grid_size   = sum([material.params['n_dx'][0] for material in mats])

        # Create property_dims
        self.grid        = lambda x : np.zeros(shape=(self.grid_size, x), dtype='float')
        self.scalar_grid = lambda : self.grid(1)
        self.vector_grid = lambda : self.grid(3)

        # Initialize spatial grids
        self.space       = self.scalar_grid()
        self.d_space     = self.scalar_grid()

        # Initialize state grids
        self.je          = self.scalar_grid()
        self.jm          = self.vector_grid()
        self.sa          = self.vector_grid()

        # Initialize parameter grids
        self.params = {}
        for p_name, p_dim in ({p_name: np.shape(p_val)[0] for p_name, p_val in self.mats[0].params.items()}).items():
            self.params[p_name] = self.grid(p_dim)

        # Fill grids
        grid_index = 0
        for mat in self.mats:
            dx = np.divide(mat.params['thickness'][0], mat.params['n_dx'][0])
            for d_step in range(mat.params['n_dx'][0]):
                self.space[grid_index] = self.space[grid_index-1] + dx
                for p_name, p_val in mat.params.items():
                        self.params[p_name][grid_index] = p_val
                grid_index += 1


    def je_fill(self, value):
        self.je.fill(value)

    def od_init(self, mats):
        self.mat_ranges = [0]
        for i in range(len(mats)):
            mat_ranges.append(int(np.floor_divide(mat_ends[i], self.d_space[0])))

            self.mag[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].mag
            self.sa_equil[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].sa_equil
            self.diff[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].diff
            self.polar_con[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].polar_con
            self.polar_diff[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].polar_diff
            self.len_pre[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].len_pre
            self.len_dph[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].len_dph
            self.len_sf[mat_ranges[i]:mat_ranges[i + 1]] = mats[i].len_sf


        # Check for poor division
        if (mat_ranges[-1] != self.grid_dim[0]):
            print('Range mapping mismatch, filling empty cells with last material...')

            self.mag[np.s_[(mat_ranges[-1])::1]] = mats[-1].mag
            self.sa_equil[np.s_[(mat_ranges[-1])::1]] = mats[-1].sa_equil
            self.diff[np.s_[(mat_ranges[-1])::1]] = mats[-1].diff
            self.polar_con[np.s_[(mat_ranges[-1])::1]] = mats[-1].polar_con
            self.polar_diff[np.s_[(mat_ranges[-1])::1]] = mats[-1].polar_diff
            self.len_pre[np.s_[(mat_ranges[-1])::1]] = mats[-1].len_pre
            self.len_dph[np.s_[(mat_ranges[-1])::1]] = mats[-1].len_dph
            self.len_sf[np.s_[(mat_ranges[-1])::1]] = mats[-1].len_sf

    def linear_interface(self):
        # Apply interface
        k = 0
        for i in range(len(inf_w)):
            for j in range(inf_w[i]):
                index = mat_ranges[1 + i] - np.floor_divide(inf_w[i], 2) + j

                self.mag[index] = mats[0 + k].mag
                self.mag[index] = np.subtract(mats[0 + i].mag, (
                        j * np.divide((np.subtract(mats[0 + i].mag, mats[1 + i].mag)), inf_w[i])))
                self.sa_equil[index] = np.subtract(mats[0 + i].sa_equil, (
                        j * np.divide((np.subtract(mats[0 + i].sa_equil, mats[1 + i].sa_equil)), inf_w[i])))
                self.diff[index] = np.subtract(mats[0 + i].diff, (
                        j * np.divide((np.subtract(mats[0 + i].diff, mats[1 + i].diff)), inf_w[i])))
                self.polar_con[index] = np.subtract(mats[0 + i].polar_con, (
                        j * np.divide((np.subtract(mats[0 + i].polar_con, mats[1 + i].polar_con)), inf_w[i])))
                self.polar_diff[index] = np.subtract(mats[0 + i].polar_diff, (
                        j * np.divide((np.subtract(mats[0 + i].polar_diff, mats[1 + i].polar_diff)), inf_w[i])))
                self.len_pre[index] = np.subtract(mats[0 + i].len_pre, (
                        j * np.divide((np.subtract(mats[0 + i].len_pre, mats[1 + i].len_pre)), inf_w[i])))
                self.len_dph[index] = np.subtract(mats[0 + i].len_dph, (
                        j * np.divide((np.subtract(mats[0 + i].len_dph, mats[1 + i].len_dph)), inf_w[i])))
                self.len_sf[index] = np.subtract(mats[0 + i].len_sf, (
                        j * np.divide((np.subtract(mats[0 + i].len_sf, mats[1 + i].len_sf)), inf_w[i])))

            k += 2