import taichi as ti
import numpy as np
import sys
sys.path.append(".")

ti.init()

@ti.data_oriented
class NeighborhoodSearch():
    def __init__(self, pos) -> None:
        # common paramters
        dim = 3
        num_particles = 100
        particle_radius = 3.0
        h = 1.1

        # read positions from the test data input
        self.positions = ti.Vector.field(dim, float, num_particles)
        self.positions.from_numpy(pos)

        # nsearch parameters
        self.grid_size = (16,16,16)
        cell_size = 2.51
        self.cell_recpr = 1.0 / cell_size
        self.neighbor_radius = h * 1.05
        self.max_num_particles_per_cell = 100
        self.max_num_neighbors = 100

        # nsearch fields
        self.grid_num_particles = ti.field(int)
        self.particle_num_neighbors = ti.field(int)
        self.particle_neighbors = ti.field(int)
        grid_snode = ti.root.dense(ti.ijk, self.grid_size) 
        grid_snode.place(self.grid_num_particles)
        self.grid2particles = ti.field(int, (self.grid_size + (self.max_num_particles_per_cell,)))
        nb_node = ti.root.dense(ti.i, num_particles)
        nb_node.place(self.particle_num_neighbors)
        nb_node.dense(ti.j, self.max_num_neighbors).place(self.particle_neighbors)


    @ti.func
    def get_cell(self,pos):
        return int(pos * self.cell_recpr)

    @ti.func
    def is_in_grid(self,c):
        return 0 <= c[0] and c[0] < self.grid_size[0] and 0 <= c[1] and c[
            1] < self.grid_size[1]

    @ti.kernel
    def neighborhood_search(self):
        # clear neighbor lookup table
        for I in ti.grouped(self.grid_num_particles):
            self.grid_num_particles[I] = 0
        for I in ti.grouped(self.particle_neighbors):
            self.particle_neighbors[I] = -1

        # update grid
        for p_i in self.positions:
            cell = self.get_cell(self.positions[p_i])
            offs = ti.atomic_add(self.grid_num_particles[cell], 1)
            self.grid2particles[cell, offs] = p_i
        # find particle neighbors
        for p_i in self.positions:
            pos_i = self.positions[p_i]
            cell = self.get_cell(pos_i)
            nb_i = 0
            for offs in ti.static(ti.grouped(ti.ndrange((-1, 2), (-1, 2),(-1, 2)))):
                cell_to_check = cell + offs
                if self.is_in_grid(cell_to_check):
                    for j in range(self.grid_num_particles[cell_to_check]):
                        p_j = self.grid2particles[cell_to_check, j]
                        if nb_i < self.max_num_neighbors and p_j != p_i and (
                                pos_i - self.positions[p_j]).norm() < self.neighbor_radius:
                            self.particle_neighbors[p_i, nb_i] = p_j
                            nb_i += 1
            self.particle_num_neighbors[p_i] = nb_i
    

def test():
    pos = np.loadtxt('E:/Dev/SPH_Taichi/tests/test_data_input_nsearch.csv',dtype=float)
    search = NeighborhoodSearch(pos)
    search.neighborhood_search()

    np.savetxt('test_data_actual_output_nsearch.csv', search.particle_neighbors.to_numpy(), "%d")

if __name__ == '__main__':
    test()

# np.savetxt('pos.csv', position.to_numpy().flatten(), "%.3f")