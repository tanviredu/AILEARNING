#!/bin/bash

# Update package list and install dependencies (Git, Make, GCC)
echo "Installing required dependencies..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update
    sudo apt install -y git make gcc
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install git make gcc
else
    echo "Unsupported OS. Please install dependencies manually."
    exit 1
fi

# Clone Cosmopolitan C Library repository
echo "Cloning Cosmopolitan repository..."
git clone https://github.com/jart/cosmopolitan.git
cd cosmopolitan || exit 1

# Build Cosmopolitan C Library
echo "Building Cosmopolitan C Library..."
make

# Check if build was successful
if [ -f "cosmopolitan.o" ]; then
    echo "Cosmopolitan C Library built successfully!"
else
    echo "Build failed. Please check the errors."
    exit 1
fi

# Notify user to use Cosmopolitan in their C projects
echo "Cosmopolitan is built and ready to be used in your C
