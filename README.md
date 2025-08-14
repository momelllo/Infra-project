# DevOps Infrastructure Provisioning & Configuration Automation Project

## 📌 Overview
This project is a **modular Python-based infrastructure provisioning simulator**.  
It allows a user to define virtual machines (VMs), validate the input, store configurations, and simulate provisioning.  
It also triggers a Bash script to **install and configure a service (Nginx)**, with all actions logged in a single file.

> **Note:** This version is a simulation. No real cloud resources are created.  
> In the future, AWS/Terraform integration will be added.

---

## 📂 Project Structure
Infra_Project/
├── configs/ # Stores instance configuration files
│ └── instances.json
├── logs/ # All logs stored here
│ └── provisioning.log
├── scripts/ # Bash automation scripts
│ └── install_service.sh
├── src/ # Python modules
│ ├── machine.py
│ └── machine_schema.py
├── infra_simulator.py # Main Python entry point
├── requirements.txt # Python dependencies
└── README.md # This file

---

## ⚙️ Requirements
- **Python 3.8+**
- **pip** (Python package manager)
- **bash** (Linux shell, included by default on Ubuntu/CentOS)
- On Linux: Ability to install packages via `apt` (Ubuntu/Debian) or `yum` (CentOS/RHEL/Fedora)
- On Windows: GitBash or WSL for running bash scripts (install step will fail gracefully)

---

## 📥 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/momelllo/Infra_Project.git
cd Infra_Project
2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux / GitBash
3. Install dependencies
pip install -r requirements.txt
🚀 Running the Project
Run the main script:
python infra_simulator.py

Steps:
The script will prompt you for:
Machine name
Operating system (CentOS or Ubuntu)
Number of CPU cores
RAM size (GB)
Storage size (GB)

Input is validated using Pydantic — invalid values will be rejected.

If validation passes:
Machine details are saved to configs/instances.json
The Bash script scripts/install_service.sh runs to install Nginx

All logs (Python + Bash) are saved in logs/provisioning.log

🗒️ Log Example (logs/provisioning.log)
2025-08-13 14:55:02,457 - INFO - ============================================
2025-08-13 14:55:02,457 - INFO - === Infrastructure Provisioning Tool Started ===
2025-08-13 14:55:02,458 - INFO - Machine created: TestVM (Ubuntu, CPU: 2, RAM: 4GB, Storage: 50GB)
----- [Service Installation Started] -----
Detected OS: ubuntu
Installing Nginx on Ubuntu/Debian...
Nginx installation completed successfully.
----- [Service Installation Completed] -----
2025-08-13 14:55:05,980 - INFO - Provisioning session completed
2025-08-13 14:55:05,980 - INFO - ============================================

🖥️ Testing Notes
On Windows, the Bash script will run but fail to install Nginx — this is expected.
On CentOS/Ubuntu, the script will attempt to install and start Nginx.

✏️ by Michael W