import matplotlib.pyplot as plt
from vehicle import Vehicle
from network import Network
import random



def run_simulation(num_vehicles=10, steps=50):
    vehicles = [Vehicle(i) for i in range(num_vehicles)]
    network = Network(packet_loss=0.2, latency=0.1)

    collisions = 0
    collisions_history = []

    for _ in range(steps):
        for v in vehicles:
            v.move()

        braking_vehicle = random.choice(vehicles)
        braking_vehicle.brake()

        step_collisions = 0

        for v in vehicles:
            if v != braking_vehicle:
                msg = network.transmit("BRAKE")

                if msg is None:
                    if abs(v.position - braking_vehicle.position) < 5:
                        collisions += 1
                        step_collisions += 1
                else:
                    v.brake()

        collisions_history.append(step_collisions)

    return {
        "total_collisions": collisions,
        "history": collisions_history
    }

def plot_results(collisions_history):
    plt.figure()
    plt.plot(collisions_history)
    plt.title("Collisions over time")
    plt.xlabel("Simulation step")
    plt.ylabel("Number of collisions")
    plt.grid()
    plt.show()
