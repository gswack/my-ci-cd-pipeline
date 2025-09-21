## Overview
A python-based web application designed to demonstrate scalable development and modern DevOps practices. It leverages Docker to showcase infrastructure-as-code, automated CI/CD pipelines.

## 🧱 Tech Stack
- Docker  
- GitHub Actions (CI/CD)

## 🚀 How to Run Locally  
# Clone the repo
git clone https://github.com/gswack/my-ci-cd-pipeline.git
cd my-ci-cd-pipeline
# Run the Python app
python main.py
# Build Docker image
docker build -t gswack/my-ci-cd-pipeline .
# Run container locally
docker run -p 5000:5000 gswack/my-ci-cd-pipeline

## ⚙️ CI/CD Overview
This project uses **GitHub Actions** to automate testing and integration.
- The workflow is defined in `.github/workflows/ci.yaml`
- It runs automatically on:
  - Pushes to the `main` branch
  - Pull requests
- It installs dependencies and runs test scripts to ensure code quality
- Test results are visible directly in the GitHub Actions tab
- Failed runs trigger email or GitHub notifications with 

## How to run locally
'''bash
# Clone the repo
git clone https://github.com/gswack/my-ci-cd-pipeline.git
cd my-ci-cd-pipeline

# Run the Python app
python main.py

# Build Docker image
docker build -t gswack/my-ci-cd-pipeline .

# Run container locally
docker run -p 5000:5000 gswack/my-ci-cd-pipeline

## Project Structure
my-ci-cd-pipeline/
├── app/  
│   └── main.py
├── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml
        └── cd.yml
└── README.md

## License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with proper attribution.

See the LICENSE file for full details.

## Contributions
Contributions are welcome and appreciated! If you'd like to improve this project, feel free to:

Fork the repository
Create a new branch (git checkout -b feature-name)
Make your changes
Submit a pull request
Please ensure your code follows the existing style and passes all tests before submitting.
