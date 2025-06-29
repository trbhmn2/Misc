import math

class CarSimulation:
    def __init__(self, specs):
        self.specs = specs
        self.velocity = 0
        self.position = 0
        self.time_step = 0.1
        self.gravity = 9.81
        
    def calculate_friction(self):
        aero_factor = math.exp(-self.specs['aerodynamics'] / 100)
        wheel_factor = (self.specs['front_wheel_size'] + self.specs['rear_wheel_size']) / 100
        friction = self.specs['wheel_friction'] * aero_factor * wheel_factor
        return friction / 10
        
    def calculate_acceleration(self, force):
        friction = self.calculate_friction()
        net_force = force - friction - (self.specs['weight'] * self.gravity * 0.1)
        return net_force / self.specs['weight']
        
    def apply_energy_loss(self):
        efficiency = 1 - (self.specs['energyLoss'] / 200)
        self.velocity *= efficiency
        
    def apply_drift(self):
        straight_factor = self.specs['straightness'] / 100
        smooth_factor = self.specs['ride_smoothness'] / 100
        self.velocity *= (straight_factor * 0.8 + smooth_factor * 0.2)
        
    def simulate(self, force_input, duration):
        total_time = 0
        force_duration = force_input * 0.8
        
        while total_time <= duration:
            if total_time < force_duration:
                current_force = force_input * (1 - total_time / force_duration)
                acceleration = self.calculate_acceleration(current_force)
                self.velocity += acceleration * self.time_step
                
            self.apply_energy_loss()
            self.apply_drift()
            self.position += self.velocity * self.time_step
            
            if total_time % 1 < self.time_step:
                print(f"T+{int(total_time)}s: Vel={self.velocity:.1f}m/s, Pos={self.position:.1f}m")
                
            total_time += self.time_step
            
        return self.position

car_specs = {
    "weight": 1250,
    "wheel_friction": 0.8, 
    "front_wheel_size": 0.7,
    "rear_wheel_size": 0.7,
    "aerodynamics": 0.85,
    "energyLoss": 15,
    "straightness": 0.92,
    "ride_smoothness": 0.88
}

sim = CarSimulation(car_specs)
force = int(input("Engine force (N): "))
result = sim.simulate(force, 60)
print(f"\nFinal distance: {result:.1f} meters")
