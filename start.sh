#!/bin/bash

# Function to print the banner in RGB colors
print_banner() {
    echo -e "\e[38;2;255;0;0m"
    echo " ______     ______     ______     ______     __  __        ______     __     ______  "
    echo -e "\e[38;2;255;127;0m/\  ___\   /\  == \   /\  __ \   /\  ___\   /\ \/ /       /\___  \   /\ \   /\  == \ "
    echo -e "\e[38;2;255;255;0m\ \ \____  \ \  __<   \ \  __ \  \ \ \____  \ \  _\"-.     \/_/  /__  \ \ \  \ \  _-/ "
    echo -e "\e[38;2;0;255;0m \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\      /\_____\  \ \_\  \ \_\   "
    echo -e "\e[38;2;0;0;255m  \/_____/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/      \/_____/   \/_/   \/_/   "
    echo -e "\e[0m"  # Reset color
    echo -e "\e[38;2;0;255;255m"  # Set color for menu text
    echo "===================================="
    echo -e "      \e[38;2;255;0;255mCodex By 222-Xp01T Version 1.0\e[0m"  # Menu title in purple
    echo "===================================="
}

# Function to install packages
install_packages() {
    pkg update && pkg upgrade -y

    if ! command -v python &> /dev/null; then
        pkg install python -y
    fi

    if ! command -v bash &> /dev/null; then
        pkg install bash -y
    fi

    if ! python -c "import pyzipper" &> /dev/null; then
        pip install pyzipper
    fi
}

# Function to run the Python script
run_script() {
    python apw82dn6kojzwzamobt3v363pfuhas5tuz7sf7zp.py
}

# Main script
clear  # Clear the terminal
print_banner
echo -e "\e[38;2;255;0;0mtype [1] to install the package\e[0m"  # Red
echo -e "\e[38;2;255;127;0mKetik 2 Type [2] to run the script\e[0m"  # Orange
echo "===================================="
read -p "Pilihan Anda: " choice

case $choice in
    1)
        echo -e "\e[38;2;0;255;0mMenginstall paket...\e[0m"  # Green
        install_packages
        echo -e "\e[38;2;255;255;0mSemua paket telah diinstall atau sudah ada.\e[0m"  # Yellow
        ;;
    2)
        echo -e "\e[38;2;0;255;255mMenjalankan script...\e[0m"  # Cyan
        run_script
        ;;
    *)
        echo -e "\e[38;2;255;0;255mPilihan tidak valid. Silakan coba lagi.\e[0m"  # Magenta
        ;;
esac