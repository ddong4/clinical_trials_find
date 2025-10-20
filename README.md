# StudyBridge: A Clinical Trials Matching Platform

[Website Link](https://studybridge.ddong.dev/)

Small project developed to connect patients with relevant clinical trials. Given a transcript of a patient interview, the platform uses AI to extract key information and match the patient with suitable clinical trials listed on ClinicalTrials.gov.

## Features

- Transcript upload and processing with AI
- Matching algorithm for clinical trials on ClinicalTrials.gov
- User-friendly interface for research coordinators and patients to find recommendations.

## Approach

1. User research with a potential user journey [simulated here](docs/0_user_journey.png)
2. Design the system architecture and choose appropriate technologies. See [architecture brainstorm](docs/2_tech_stack_options.png)
3. Create general project structure and set up the development environment.
4. Implement the core features, including transcript processing and trial matching.

## Getting Started

Please reference [DEVELOPMENT.md](docs/DEVELOPMENT.md)

### Prerequisites
* Docker
* WSL (if on Windows)

### Quick Start
navigate to root folder and `docker compose up`