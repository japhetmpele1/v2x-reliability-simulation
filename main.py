from simulation import run_simulation

if __name__ == "__main__":
    results = run_simulation(num_vehicles=20, steps=100)
    print(results)
