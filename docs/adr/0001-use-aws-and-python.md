# ADR 0001: Use AWS as the cloud platform and Python as the application language

- **Status:** Accepted
- **Date:** 2026-10-12

## Context

AeroOps needs managed networking, a relational database, messaging and container orchestration. The team is small and wants to optimise for delivery speed and a broadly adopted platform.

## Decision

- Cloud platform: **AWS**.
- Application language: **Python** with **FastAPI**.

## Consequences

- Managed services (RDS, SQS, SNS, EKS) reduce operational work.
- Python limits raw throughput compared with compiled languages; acceptable for current load, revisit if SLOs are not met.
- The design uses portable building blocks (containers, Kubernetes, PostgreSQL) to keep migration cost to another cloud bounded.

## Alternatives considered

- **Azure:** comparable services; no advantage for this workload.
- **Go/Java:** better raw performance, slower to build for this scope.
