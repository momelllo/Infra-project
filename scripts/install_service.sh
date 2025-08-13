#!/bin/bash

LOG_FILE="logs/provisioning.log"

# Ensure logs directory exists
mkdir -p logs

echo "----- [Service Installation Started] -----" >> "$LOG_FILE"

# Detect OS type
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
else
    echo "Unable to detect OS." >> "$LOG_FILE"
    exit 1
fi

echo "Detected OS: $OS" >> "$LOG_FILE"

# Install nginx based on OS
if [[ "$OS" == "ubuntu" || "$OS" == "debian" ]]; then
    if dpkg -l | grep -q nginx; then
        echo "Nginx is already installed." >> "$LOG_FILE"
    else
        echo "Installing Nginx on Ubuntu/Debian..." >> "$LOG_FILE"
        sudo apt-get update >> "$LOG_FILE" 2>&1
        sudo apt-get install -y nginx >> "$LOG_FILE" 2>&1
    fi
elif [[ "$OS" == "centos" || "$OS" == "rhel" || "$OS" == "fedora" ]]; then
    if rpm -qa | grep -q nginx; then
        echo "Nginx is already installed." >> "$LOG_FILE"
    else
        echo "Installing Nginx on CentOS/RHEL/Fedora..." >> "$LOG_FILE"
        sudo yum install -y epel-release >> "$LOG_FILE" 2>&1
        sudo yum install -y nginx >> "$LOG_FILE" 2>&1
    fi
else
    echo "Unsupported OS: $OS" >> "$LOG_FILE"
    exit 1
fi

# Enable and start Nginx
sudo systemctl enable nginx >> "$LOG_FILE" 2>&1
sudo systemctl start nginx >> "$LOG_FILE" 2>&1

echo "Nginx installation completed successfully." >> "$LOG_FILE"
echo "----- [Service Installation Completed] -----" >> "$LOG_FILE"
exit 0