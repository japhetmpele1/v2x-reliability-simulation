from simulation import run_simulation, plot_results

if __name__ == "__main__":
    results = run_simulation(num_vehicles=20, steps=100)

    print("Total collisions:", results["total_collisions"])

    plot_results(results["history"])
