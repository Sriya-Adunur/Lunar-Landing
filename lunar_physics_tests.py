# Tests functions for simulating physics.
# CSC 101, Project 2
# Given tests, Summer '22

import unittest
import lunar_physics


class TestLunarPhysics(unittest.TestCase):
    def test01_update_fuel(self):
        fuel = lunar_physics.update_fuel(1200.0, 0.1)
        self.assertAlmostEqual(fuel, 1198.446)

    def test02_update_acceleration(self):
        acceleration = lunar_physics.update_acceleration(1198.446, 0.1)
        self.assertAlmostEqual(acceleration, -1.0994726)

    def test03_update_velocity(self):
        velocity = lunar_physics.update_velocity(-15.0, -1.0994726)
        self.assertAlmostEqual(velocity, -16.0994726)

    def test04_update_altitude(self):
        altitude = lunar_physics.update_altitude(200.0, -16.0994726)
        self.assertAlmostEqual(altitude, 183.9005274)


if __name__ == "__main__":
    unittest.main()
