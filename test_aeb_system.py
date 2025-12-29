import unittest

# Modulul AEB (Sistemul)
class AEBModule:
    def check_collision(self, speed, distance):
        if speed < 30 and distance < 15:
            return "FULL_BRAKE"
        return "NO_ACTION"

# Testele Automate
class TestAEBSystem(unittest.TestCase):
    
    def test_ideal_case(self):
        # Scenariul 1: Frânare ideală
        current_speed = 29
        object_distance = 14.9
        system = AEBModule()
        result = system.check_collision(current_speed, object_distance)
        self.assertEqual(result, "FULL_BRAKE")

    def test_speed_limit_exceeded(self):
        # Scenariul 2: Viteză prea mare -> Nu frânează
        current_speed = 31
        object_distance = 14
        system = AEBModule()
        result = system.check_collision(current_speed, object_distance)
        self.assertEqual(result, "NO_ACTION")

    def test_distance_limit_exceeded(self):
        # Scenariul 3: Obstacol prea departe -> Nu frânează
        current_speed = 29
        object_distance = 16
        system = AEBModule()
        result = system.check_collision(current_speed, object_distance)
        self.assertEqual(result, "NO_ACTION")
