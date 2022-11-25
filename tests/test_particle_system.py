import taichi as ti
import numpy as np
ti.init()

import sys
sys.path.append(".")
sys.path.append("..")

from config_builder import SimConfig
from particle_system import ParticleSystem


class get_ps():
    def __init__(self, ps) -> None:
        self.ps = ps
        print(ps)

if __name__ == '__main__':
    config = SimConfig(scene_file_path="./data/scenes/dragon_bath.json")
    ps = ParticleSystem(config, GGUI=True)
    a = get_ps(ps)