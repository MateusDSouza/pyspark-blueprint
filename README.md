# Python ETL Project Blueprint

This repository serves as a blueprint for Python-based ETL (Extract, Transform, Load) projects. It provides a modularized structure, pre-commit hooks for code quality, and a Dockerized testing environment using PySpark, eliminating the need for local installation of JDK and PySpark.

## Features

- **Modularized Code**: Clearly defined modules for Connectors, Extractors, Transformers, and Loaders to ensure scalability and reusability.
- **Pre-commit Hooks**: Automated checks for code quality, formatting, and linting using tools like `black`, `flake8`, and `mypy`.
- **Testing Framework**: Comprehensive tests to ensure code reliability, run in an isolated Docker container with PySpark.
- **Dockerized Environment**: A pre-configured Docker image for testing, avoiding the need for local installation of dependencies like JDK or PySpark.

---

## Getting Started

### Prerequisites

Ensure the following are installed and configured on your system:

1. Python: Version 3.11 or higher.

2. Docker: To run tests in an isolated environment.

3. Poetry: For dependency and virtual environment management.
curl -sSL https://install.python-poetry.org | python3 -

4. Dependencies: Install the required packages using Poetry.
poetry install

The project uses the following main dependencies:
- PySpark (3.5.2): For big data processing.
- ConfigParser (7.1.0): For configuration management.
- Black (24.8.0): For code formatting.
- Pre-commit (3.8.0): For automating code quality checks.
- Pytest (8.3.3): For testing.

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MateusDSouza/pyspark-blueprint.git
   cd pyspark-blueprint
---

## Usage

To implement your custom ETL logic, follow these steps:

1. **Extend the Abstract Classes**:
   - **Connectors**: Create classes to establish connections to external systems.
   - **Extractors**: Implement logic to retrieve data from specific sources.
   - **Transformers**: Define methods to process and transform the data.
   - **Loaders**: Write logic to load data into target systems.

2. **Add Unit Tests**:
   - Place your tests in the `tests` directory to ensure your implementations are properly validated.

3. **Run Tests**:
   - **Using Pre-commit Hooks**:
     - Tests are automatically run in a Dockerized environment as part of the pre-commit hooks. To trigger the hooks manually, use:
       ```bash
       pre-commit run --all-files
       ```

   - **From the Command Line**:
     - If you want to run the tests directly, use the following Docker commands:
       1. Build the Docker image:
          ```bash
          docker-compose build
          docker-compose up -d
          ```
       2. Run the tests in the Docker container:
          ```bash
          docker-compose run --rm test
          ```
