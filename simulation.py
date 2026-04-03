from vehicle import Vehicle
from network import Network
import random

def run_simulation(num_vehicles=10, steps=50):
    vehicles = [Vehicle(i) for i in range(num_vehicles)]
    network = Network(packet_loss=0.2, latency=0.1)

    collisions = 0

    for _ in range(steps):
        for v in vehicles:
            v.move()

        # simulate sudden braking
        braking_vehicle = random.choice(vehicles)
        braking_vehicle.brake()

        for v in vehicles:
            if v != braking_vehicle:
                msg = network.transmit("BRAKE")

                if msg is None:
                    # vehicle didn't receive warning → collision risk
                    if abs(v.position - braking_vehicle.position) < 5:
                        collisions += 1
                else:
                    v.brake()

    return {
        "vehicles": num_vehicles,
        "collisions": collisions,
        "packet_loss": network.packet_loss
    }
