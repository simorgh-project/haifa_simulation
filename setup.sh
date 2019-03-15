#!/bin/bash

# Create a virtual environment on mac and linux
python3 -m virtualenv venv

# Activate virtual environment
source venv/bin/active

# Install selenium
pip install -U selenium

# Install paramiko
pip install -U paramiko
