# Defines functions for simulating physics.
# CSC 101, Project 2
# Given code, Summer '22


def update_fuel(fuel, throttle):
    """
    Compute the amount of fuel.
    TODO: Complete this function.

    :param fuel: An amount of fuel at time (t - 1)
    :param throttle: A throttle fraction at time t
    :return: The amount of fuel at time t
    """
    
    fuel =  fuel - (15.54 * throttle)
    if fuel < 0:
       return 0
    else:
       return fuel

def update_acceleration(fuel, throttle):
    """
    Compute the acceleration.
    TODO: Complete this function.

    :param fuel: An amount of fuel at time t
    :param throttle: A throttle fraction at time t
    :return: The acceleration at time t
    """

    return ((46710 * throttle)/(7606 + fuel)) - 1.63  
  

def update_velocity(velocity, acceleration):
    """
    Compute the velocity.
    TODO: Complete this function.

    :param velocity: A velocity at time (t - 1)
    :param acceleration: An acceleration at time t
    :return: The velocity at time t
    """
    
    return velocity + acceleration    


def update_altitude(altitude, velocity):
    """
    Compute the altitude.
    TODO: Complete this function.

    :param altitude: An altitude at time (t - 1)
    :param velocity: A velocity at time t
    :return: The altitude at time t
    """
    altitude = altitude + velocity
    if altitude <= 0:
        return 0
    else: 
        return altitude

