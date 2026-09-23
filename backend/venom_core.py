<<<<<<< HEAD
# VENOM CORE PIPELINE INITIALIZED
=======
import sys
import os

STATE_FILE = "backend/.venom_workers"

def get_worker_count():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 4
    return 4  # Default baseline

def set_worker_count(count):
    with open(STATE_FILE, "w") as f:
        f.write(str(count))
    print(f"[VENOM CORE] Scaled active Venom Jr nodes to: {count}")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "scale":
        try:
            target = int(sys.argv[2])
            set_worker_count(target)
        except ValueError:
            print("Error: Scale target must be an integer.")
    else:
        print(f"Venom Core active. Current Venom Jr nodes: {get_worker_count()}")
>>>>>>> fc1d2519815b76b6bdce3e197435d5738a63869d
