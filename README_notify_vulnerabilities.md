# Tsunami Security Scanner Extension


![build](https://github.com/google/tsunami-security-scanner/workflows/tsunami-security-scanner/badge.svg)

![build](https://github.com/google/tsunami-security-scanner/workflows/notify_vulnerabilities/badge.svg)

This repository is a fork of the original Tsunami Security Scanner by Google. It has been extended to support scanning multiple IPs from a file and outputting results to local JSON files.

## Features
- Multiple IP Scanning: Scans multiple IPs listed in a file (targets.txt), with one IP per line.
- JSON Output: Outputs scan results to local JSON files, one for each scanned IP.
- Email Notification: Notifies of vulnerabilities via email using a customizable Python script.


## Added/Modified Components:

#### tsunami-security-scanner

- `targets.txt` - example for ip list format.
- `scan_servers.sh` - simple script to iterate over given file list and feed into tsunami.
- `Dockerfile` - modified to include custom files, replaced image entrypoint/cmd.

#### Notification Component

- `notify_vulnerabilities.py` - simple script to send notification (email) - this is given as an example - which can easaly be replaced __without effecting other components__.
- `notify_vulnerabilities/Dockerfile` - build and push to dockerhub

#### Kubernetes Configuration

- `job-tsunami-security-scanner.yaml` - kubernetes job for running scan for a given list of IPs. running scanner component as initContainer, and then running the notifier component - on the same local folder.
- `configmap-tsunami-targets.yaml` - example IPs list.
- `configmap-tsunami-notification-email.yaml` - required setting for notification send (email setting in this case, but can be replaced easaly with some other send method).
- `secret-tsunami-notification-email.yaml` - required _sensitive_ setting for send.
- `deployment-unauthenticated-jupyter-notebook.yaml` - example voulnerable target to test notification sending functionality, make sure to update IP list in configmap with the IP for deployed voulnerable target.

## Dockerhub
- https://hub.docker.com/r/amirtal122018/tsunami-security-scanner

- https://hub.docker.com/r/amirtal122018/notify_vulnerabilities