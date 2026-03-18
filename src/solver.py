from dataclasses import dataclass

@dataclass
class BarnConfig:
    NX: int = 90
    NY: int = 40
    dt: float = 0.04
    nu: float = 0.012
    barn_x0: int = 14
    barn_x1: int = 76
    floor_j: int = 36
    eave_j: int = 7
    ridge_j: int = 2
    ridge_cx: int = 45
    fan_j0: int = 10
    fan_j1: int = 30
    out_temp: float = 28.0
    out_ch4: float = 0.0003
    wind_speed: float = 3.5
    fan_speed_pct: float = 60.0
    ridge_open_pct: float = 50.0
    n_cows: int = 12
    cow_heat_dt: float = 0.12
    cow_ch4_dt: float = 0.0001
    n_mof_units: int = 4
    mof_absorption: float = 0.12
    mof_suction: float = 0.04
    n_steps: int = 400
    steps_per_save: int = 50

class BarnGeometry:
    def roof_j(self):
        # Implementation to determine the roof index
d        pass

    def is_wall(self):
        # Implementation to check if a point is a wall
        pass

    def is_interior(self):
        # Implementation to check if a point is interior
        pass

    @property
    def wall_mask(self):
        # Implementation for wall mask property
        pass

    @property
    def interior_mask(self):
        # Implementation for interior mask property
        pass

    def mof_positions(self):
        # Implementation to get MOF positions
        pass

    def cow_positions(self):
        # Implementation to get cow positions
        pass

class CFDSolver:
    def __init__(self):
        self.u = None
        self.v = None
        self.p = None
        self.T = None
        self.ch4 = None

    def reset(self):
        # Implementation to reset the fields
        pass

    @property
    def u_center(self):
        # Implementation for u_center property
        pass

    @property
    def v_center(self):
        # Implementation for v_center property
        pass

    @property
    def velocity_magnitude(self):
        # Implementation for velocity magnitude property
        pass

    def _apply_bc(self):
        # Implementation for boundary conditions
        pass

    def _advect(self):
        # Implementation for semi-Lagrangian advection
        pass

    @staticmethod
    def _diffuse():
        # Implementation for diffusion
        pass

    def _solve_pressure(self):
        # Implementation using Gauss-Seidel iteration
        pass

    def step(self):
        # Implementation for a single time step
        pass

    def run(self):
        # Implementation to run the solver
        pass

    def metrics(self):
        # Implementation to return metrics
        return {}