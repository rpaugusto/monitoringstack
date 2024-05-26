# Monitoring Stack with Grafana, Prometheus, and Blackbox Exporter

This project sets up a monitoring stack using Docker Compose, featuring Grafana, Grafana Image Renderer, Prometheus, and Blackbox Exporter. The stack is pre-configured for easy deployment and monitoring.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Provisioning](#provisioning)
  - [Dashboards](#dashboards)
  - [Data Sources](#data-sources)
- [Monitoring Grafana Metrics with Prometheus](#monitoring-grafana-metrics-with-prometheus)
- [Directory Structure](#directory-structure)
- [Vagrant Setup](#vagrant-setup)
- [License](#license)

## Prerequisites

- Docker
- Docker Compose
- Vagrant
- VirtualBox

## Installation

1. Clone the repository.
2. Create a `.env` file in the root directory with the necessary environment variables for Grafana.
3. Start the services using Docker Compose.

## Configuration

- Grafana is configured to use a predefined set of plugins and settings specified in the `.env` file.
- Prometheus is set up to scrape metrics from Grafana and other services.

## Usage

- Access Grafana at `http://localhost:3000` with the credentials set in the `.env` file.
- Access Prometheus at `http://localhost:9090`.
- Access Blackbox Exporter at `http://localhost:9115`.

## Provisioning

### Dashboards

- Place your dashboard JSON files in the `grafana/dashboards` directory.
- Update the provisioning configuration to include your dashboards.

### Data Sources

- Define your data sources in the `grafana/provisioning/datasources/datasources.yml` file.

## Monitoring Grafana Metrics with Prometheus

- Update the Prometheus configuration to scrape metrics from Grafana.
- Restart Prometheus to apply the changes.

## Directory Structure
```
>  monitoringstack/
>  │   monitoring-setup/
>  │   ├── docker-compose.yml
>  │   ├── .env
>  │   ├── prometheus/
>  │   │   └── prometheus.yml
>  │   ├── blackbox/
>  │   │   └── blackbox.yml
>  │   ├── grafana/
>  │   │   ├── dashboards/
>  │   │   │   ├── blackbox-exporter.json
>  │   │   │   └── sample-dashboard.json
>  │   │   └── provisioning/
>  │   │       ├── datasources/
>  │   │       │   └── datasources.yml
>  │   │       └── dashboards/
>  │   │           └── dashboards.yml
>  │   └── zabbix/
>  └── Vagrantfile
```

## Vagrant Setup

- This project uses Vagrant to create a virtual machine running Ubuntu (version specified in the `Vagrantfile`).
- The VM is configured with Docker and Docker Compose to manage the monitoring stack.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.