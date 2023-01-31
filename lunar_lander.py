# Simulates the Apollo LM's final descent to the Moon.
# CSC 101, Project 2
# Given code, Summer '22
# TODO: Complete this program.

import lunar_io
import lunar_physics

def main():
    time = 0
    altitude = 200.0
    velocity = -15.0
    fuel = 1200.0

    name1 = lunar_io.get_name()
    lunar_io.print_welcome(name1)

    while altitude > 0:
        throttle = lunar_io.print_status(time, altitude, velocity, fuel)
        
        if throttle == 0 and fuel == 0:
            throttle = 0
        elif throttle < 10:
            throttle = .1
        elif throttle > 100:
            throttle = 1
        else:
            throttle = throttle * .01

        fuel = lunar_physics.update_fuel(fuel, throttle)    
        acceleration = lunar_physics.update_acceleration(fuel, throttle)
        velocity = lunar_physics.update_velocity(velocity, acceleration)
        altitude = lunar_physics.update_altitude(altitude, velocity)
        time = time + 1
            
       
    lunar_io.print_landing(time, velocity, fuel)
    
    if velocity > -1.5 and velocity <= 0:
        lunar_io.print_success(name1)
    elif velocity > -3 and velocity <= -1.5:
        lunar_io.print_error()
    else:
        lunar_io.print_failure()

if __name__ == "__main__":
    main()
