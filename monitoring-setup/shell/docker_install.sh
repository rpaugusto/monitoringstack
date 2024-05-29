#!/bin/bash

## Check if the script is being run with root privileges
#if [ "$EUID" -ne 0 ]; then
#  echo "Please run this script with root privileges (e.g., using 'sudo')."
#  exit 1
#fi

# Install Docker dependencies
dependencies() {
  # Update the apt package index and install required packages
  sudo apt-get update
  sudo apt-get install -y \
       apt-transport-https \
       ca-certificates \
       software-properties-common \
       curl \
       gnupg \
       lsb-release \
       unzip \
       python \
       python-pip
}

# Install Docker
install_docker() {
  # Remove old versions of Docker if present
  sudo apt-get remove -y docker docker-engine docker.io containerd runc

  # Add Docker repository
  curl -fsSL http://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] http://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

  # Install Docker
  sudo apt-get update
  sudo apt-get install -y docker-ce docker-ce-cli containerd.io

  # Enable and start Docker service
  sudo systemctl enable docker
  sudo systemctl start docker

  # Add the current user to the 'docker' group to use Docker without 'sudo'
  sudo newgrp docker
  sudo usermod -aG docker $USER

  # Confirm and test if docker running
  sudo chmod 666 /var/run/docker.sock
  docker version

}

# Install Docker Compose
install_docker_compose() {
  # Download the latest version of Docker Compose
  sudo curl -fsSL http://github.com/docker/compose/releases/latest/download/docker-compose-Linux-x86_64 -o /usr/local/bin/docker-compose

  # Apply executable permissions
  sudo chmod +x /usr/local/bin/docker-compose
  docker-compose version
}

# Run the installation functions
dependencies
install_docker
install_docker_compose

echo "Docker and Docker Compose installation completed successfully."

#EOF