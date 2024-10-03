import math

def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    # Density of water (kg/m³)
    p = 998.2
    # Acceleration due to Earth's gravity (m/s²)
    g = 9.80665
    # Pressure in kPa
    P = (p * g * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    # Density of water (kg/m³)
    p = 998.2
    # Pressure loss in kPa
    P = (-friction_factor * pipe_length * p * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    water_density = 998.2
    # calculate with formula
    pressure_loss = -0.04 * water_density * fluid_velocity**2 * quantity_fittings / 2000

    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    # Density of water (kg/m³)
    water_density = 998.2
    # dinamic of water in Pa·s
    water_viscosity = 0.0010016
    # Calculate Reynolds numbers using the fomula
    reynolds_number = (water_density * hydraulic_diameter * fluid_velocity) / water_viscosity

    return reynolds_number

WATER_DENSITY = 998.2  
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500 
WATER_DYNAMIC_VISCOSITY = 0.0010016 

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calcula a perda de pressão devido à redução do diâmetro de um tubo"""
    
    # Calcula a constante k
    k = (0.1 + (50 / reynolds_number)) * (math.pow((larger_diameter / smaller_diameter), 4) - 1)
    
    # Calcula a perda de pressão (kPa) usando a densidade da água definida na constante
    pressure_loss = (-k * WATER_DENSITY * math.pow(fluid_velocity, 2)) / 2000
    
    return pressure_loss

def kpa_to_psi(kpa):
    return kpa * 0.145038

   
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_kpa = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    pressure_psi = kpa_to_psi(pressure_kpa)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure loss: {pressure_kpa:.2f} kPa ({pressure_psi:.2f} psi)")
if __name__ == "__main__":
    main()