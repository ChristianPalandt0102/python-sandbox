#!/bin/bash

# Termux Installer Script for Python Sandbox

# Update Package List and Upgrade Packages
echo "Updating package list..."
pkg update -y

echo "Upgrading packages..."
pkg upgrade -y

# Install dependencies
echo "Installing dependencies..."
pkg install -y python python-dev python3 python3-dev git

# Set up virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Directory structure creation
echo "Creating directory structure..."
mkdir -p ~/python-sandbox/src
mkdir -p ~/python-sandbox/config

# Configuration files creation
echo "Creating configuration files..."
cat <<EOL > ~/python-sandbox/config/config.yaml
# Configuration file for Python Sandbox

setting1: value1
setting2: value2
EOL

# Startup script creation
cat <<EOL > ~/python-sandbox/start.sh
#!/bin/bash
source venv/bin/activate
python ~/python-sandbox/src/main.py
EOL
chmod +x ~/python-sandbox/start.sh

# Status checker script creation
cat <<EOL > ~/python-sandbox/status.sh
#!/bin/bash

if pgrep -f "python ~/python-sandbox/src/main.py" > /dev/null
then
    echo "Python application is running"
else
    echo "Python application is not running"
fi
EOL
chmod +x ~/python-sandbox/status.sh

# Cleanup script creation
cat <<EOL > ~/python-sandbox/cleanup.sh
#!/bin/bash

rm -rf ~/python-sandbox/src/*
echo "Cleanup done."
EOL
chmod +x ~/python-sandbox/cleanup.sh

# Documentation
cat <<EOL > ~/python-sandbox/README.md
# Python Sandbox

This script sets up a Python development environment in Termux.

## Installation

Run the `install.sh` script to set up the environment and dependencies.

## Scripts

- `start.sh`: Starts the Python application.
- `status.sh`: Checks if the Python application is running.
- `cleanup.sh`: Cleans up the project directory.
EOL

# Print completion message
echo "Installation complete!"