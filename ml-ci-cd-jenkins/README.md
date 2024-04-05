# Setup Virtual Environment

```conda```
# Create a virtual environment named jenkins-env with Python 3.11
```
conda create -n jenkins-env python=3.11 -y
```

# Activate the virtual environment
```
conda activate jenkins-env
```

# Install the required packages from requirements.txt
```
pip install -r requirements.txt
```

# Install the current package in development mode
```
pip install .
```

# Test the FASTAPI

```
{
  "Gender": "Male",
  "Married": "No",
  "Dependents": "2",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 1000,
  "Loan_Amount_Term": 1,
  "Credit_History": "1.0",
  "Property_Area": "Rural"
}
```

# Docker Commands
``` ```
# Build a Docker image named loan_pred:v1
```docker build -t loan_pred:v1 .```

# Tag the Docker image for pushing to Docker Hub
```
docker tag loan_pred:v1 impathak/loanpred:v1
```

# Push the Docker image to Docker Hub
```
docker push impathak/loanpred:v1
```

# Run a Docker container named modelv1 based on the impathak/loanpred:v1 image
```
docker run -d -it --name modelv1 -p 8005:8005 impathak/loanpred:v1 bash

```

# Execute the training pipeline inside the running container
```
docker exec modelv1 python prediction_model/training_pipeline.py
```

# Run unit tests using pytest inside the running container
```
docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear
```

# Copy the test results XML file from the container to the local directory
```
docker cp modelv1:/code/src/TestResults.xml .
```

# Execute the main.py script inside the container in detached mode
```
docker exec -d -w /code modelv1 python main.py
```

# Start the FASTAPI server inside the container in detached mode
```
docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005
```




# Installation of Jenkins

# Import the Jenkins GPG key and add the repository to the system
```
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```

# Update the package index
```
sudo apt-get update
```

# Install Jenkins
```
sudo apt-get install jenkins
```

# Update the package index and install required dependencies
```
sudo apt update
```
```
sudo apt install fontconfig openjdk-17-jre
```

# Check Java version
```
java -version
```

# Enable Jenkins service to start on boot and start the service
```
sudo systemctl enable jenkins
```
```
sudo systemctl start jenkins
```

# Check the status of Jenkins service
```
sudo systemctl status jenkins
```


