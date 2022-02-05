def readfile;
pipeline {
    agent any
	
    environment {
        AWS_ACCOUNT_ID="188274256193"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="beforeprod"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {  
	    stage('Dynamically Process Integrations'){
      steps{
        script{
		readFile = readProperties file: 'spec.yml'
		
		
		
	}
	      echo "${readfile}"
      }
	    } 
    }
}
