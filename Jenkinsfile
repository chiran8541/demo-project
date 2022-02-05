pipeline {
    agent any
	
    environment {
        AWS_ACCOUNT_ID="188274256193"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="beforeprod"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {  
  
    // Building Docker images
    stage('Building image & Push to ECR') {
	    steps{
		    script {
			    def constants = load 'flag.groovy'
                            def build_flag = constants.build_to_ECR
                    env.FILENAME = readFile 'flag.groovy'
			    
                }
		    echo "${env.FILENAME['build_to_ECR']}"
		    
	   	     
	    }
    }

            
    }
}
