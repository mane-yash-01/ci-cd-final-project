# CI/CD Final Project

## Project Overview

This project demonstrates Continuous Integration and Continuous Delivery using GitHub Actions, Tekton, and OpenShift.

## Objectives

- Automate code linting with flake8.
- Run automated unit tests with nose.
- Define reusable Tekton cleanup and testing tasks.
- Prepare the project for an OpenShift CI/CD pipeline.

## Technologies Used

- Python
- Git and GitHub
- GitHub Actions
- flake8
- nose
- Tekton
- Red Hat OpenShift

## Project Structure

- app.py: Sample Python application.
- test_app.py: Unit tests.
- .github/workflows/workflow.yml: GitHub Actions workflow.
- .tekton/tasks.yml: Tekton cleanup and testing tasks.
- requirements.txt: Python development dependencies.

## Current Status

The application, automated testing configuration, and CI/CD workflow definitions are being prepared. OpenShift deployment and pipeline execution require access to an OpenShift cluster.
