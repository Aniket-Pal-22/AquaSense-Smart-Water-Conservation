# AquaSense simulation script
import random
import time


class AquaSenseTapSimulator:
    def __init__(self, flow_rate_lpm: float = 6.0, max_open_seconds: int = 15):
        self.flow_rate_lpm = flow_rate_lpm
        self.max_open_seconds = max_open_seconds
        self.valve_open = False
        self.water_saved_liters = 0.0

    def run_cycle(self, user_present: bool, simulated_duration_sec: float, baseline_waste_liters: float):
        if user_present:
            effective_sec = min(simulated_duration_sec, self.max_open_seconds)
            self.valve_open = True
            dispensed = (self.flow_rate_lpm / 60.0) * effective_sec
            saved_in_cycle = max(0.0, baseline_waste_liters - dispensed)
            self.water_saved_liters += saved_in_cycle
            self.valve_open = False
            print(
                f"[ACTIVE] Dispensed: {dispensed:.2f} L | "
                f"Estimated Saved vs. Unattended Flow: {saved_in_cycle:.2f} L"
            )
        else:
            self.valve_open = False
            self.water_saved_liters += baseline_waste_liters
            print(
                f"[IDLE/BLOCKED] No user detected. Valve kept closed. "
                f"Prevented waste: {baseline_waste_liters:.2f} L"
            )


if __name__ == "__main__":
    sim = AquaSenseTapSimulator(flow_rate_lpm=6.0, max_open_seconds=12)
    print("--- Running AquaSense Simulation ---")
    sim.run_cycle(user_present=True, simulated_duration_sec=8.0, baseline_waste_liters=4.5)
    time.sleep(0.5)
    sim.run_cycle(user_present=False, simulated_duration_sec=10.0, baseline_waste_liters=3.0)
    time.sleep(0.5)
    sim.run_cycle(user_present=True, simulated_duration_sec=20.0, baseline_waste_liters=6.0)
    print(f"\nTotal Water Saved in Simulation: {sim.water_saved_liters:.2f} Liters")
