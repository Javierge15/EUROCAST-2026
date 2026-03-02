# EUROCAST 2026

This repository contains a collection of resources and scripts related to video streaming and network metrics for various protocols ```RTP, SRT, TCP, UDP, WebRTC, and WebSockets``` in both station and vehicle contexts, as well as result analysis.

This code was created and used for the research paper "Comparative Evaluation of Real-Time Communication Protocols in a Real Vehicle Teleoperation Platform", and presented at the EUROCAST 2026 Congress in Las Palmas de Gran Canaria, Canarias, Spain.

## REPOSITORY STRUCTURE

- ### DOCS
  Contains presentation slides, speaker notes, the conference paper and related documentation produced for EUROCAST 2026.

- ### RESULTS
  Folder with analysis scripts and CSV files of metrics and telemetry for different experiments.

- ### STATION
  Implementation of the station-side technologies. Code designed for the teleoperation station part of the system.

  Each subfolder ```RTP, SRT, TCP, UDP, WebRTC, and WebSockets``` includes `docker-compose.yaml`, `Dockerfile`, and its own code as well as a README.md explaining how to use it.

- ### VEHICLE
  Implementation of the station-side technologies. Code designed for the teleoperation vehicle part of the system.

  Each subfolder ```RTP, SRT, TCP, UDP, WebRTC, and WebSockets``` includes `docker-compose.yaml`, `Dockerfile`, and its own code as well as a README.md explaining how to use it.
  
## SUPPORTED TECHNOLOGIES

### UDP
A connectionless protocol that prioritizes minimal latency over reliability, transmitting telemetry and video without retransmission delays—essential for maintaining real-time vehicle control responsiveness.

### TCP
A connection-oriented protocol that guarantees ordered delivery of critical control commands through a handshake process, ensuring no instruction is lost at the expense of potential jitter.

### RTP
A specialized media framework designed for time-sensitive streams, adding sequence numbers and timestamps to prevent frame misalignment in the vehicle's camera feeds.

### SRT
A latency-optimized transport protocol built for unstable networks (like 4G/5G), combining UDP speed with ARQ (Automatic Repeat Request) to maintain stable video links in mobile environments.

### WebRTC
A peer-to-peer communication framework designed for sub-second latency, enabling direct, high-performance video and audio exchange between the station and the vehicle.

### WebSockets
A persistent bi-directional channel that maintains a single open connection for continuous data exchange, ideal for real-time dashboard updates and low-bandwidth signaling.


---

> **Note:** This README provides a high-level overview of the repository. Refer to the specific protocol README.md for additional details. See the `DOCS/` folder for slides, the paper, and presentation notes used at EUROCAST 2026.