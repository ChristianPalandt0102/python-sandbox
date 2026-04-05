#!/bin/bash
#! 



echo "Installing sandbox server backend-system..."

apt update
apt install -y python python-pip nodejs npm


python -m venv vm01

source vm01/bin/activate
pip install --upgrade pip
pip install asyncio flask cargo-venv virtual-glob virtual-uv 


mkdir -p data web/build

node node/director.js &
python  python/main.py
