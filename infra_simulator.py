import json
import logging
import subprocess
import os
from pydantic import ValidationError
from src.machine import Machine
from src.machine_schema import MachineSchema

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Logging setup
logging.basicConfig(
    filename="logs/provisioning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("============================================")
    logging.info("=== Infrastructure Provisioning Tool Started ===")

    try:
        # Collect and validate user input
        data = {
            "name": input("Enter machine name: "),
            "os": input("Enter operating system (CentOS/Ubuntu): "),
            "cpu": int(input("Enter number of CPU cores: ")),
            "ram": float(input("Enter RAM size (GB): ")),
            "storage": float(input("Enter storage size (GB): "))
        }

        validated = MachineSchema(**data)

    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return
    except ValueError as e:
        logging.error(f"Invalid number format: {e}")
        return

    # Create machine object
    machine = Machine(
        validated.name,
        validated.os,
        validated.cpu,
        validated.ram,
        validated.storage
    )

    # Save to configs/instances.json
    try:
        with open("configs/instances.json", "r") as f:
            instances = json.load(f)
    except FileNotFoundError:
        instances = []

    instances.append(machine.to_dict())

    with open("configs/instances.json", "w") as f:
        json.dump(instances, f, indent=4)

    logging.info(f"Provisioned machine: {machine.name}")
    logging.info("=== Provisioning completed successfully ===")

    # Run the service installation script
    try:
        subprocess.run(
            ["bash", "scripts/install_service.sh"],
            check=True
        )
        logging.info("Service installation script completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Service installation failed. Return code: {e.returncode}")

    logging.info("Provisioning session completed")
    logging.info("============================================")

if __name__ == "__main__":
    main()