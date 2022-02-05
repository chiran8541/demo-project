pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="188274256193"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="beforeprod"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {  
	    stage('pre-build') {
		    steps {
		     sh '''
			    mkdir -p /tmp/demo
			    ls -lrt
		    	    cp ${workspace}/spec.yml /tmp/demo
		            cp ${workspace}/Dockerfile /tmp/demp
			    specFilePath = /tmp/demo/spec.yml
			    '''
	    }
	    }
	    
	    stage('loading envfor flag') {
		    steps{
		    script{
			   
			    def buildflag = false 
			    def deployflag = false
			    buildflag= getParam('build_to_ECR','build',specFilePath)
			    deployflag= getParam('deploy_to_ECS','build',specFilePath)
			    
			    
		    }
		    }
	    }
		    
     
  
    // Building Docker images
    
    stage('Building image & Push to ECR') {
      steps{
        script {
		if (buildflag){
            if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                            buildno = "@buildno@"
                            currentbuildno = currentBuild.number
            sh """
                    
		    cd /tmp/demo
		    sed -i -e 's#${buildno}#${currentbuildno}#' update-td.json
		    pwd
                    docker build -t "${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}" .
                    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin "${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com"
                    docker tag ${IMAGE_REPO_NAME}:V-${BUILD_NUMBER} ${REPOSITORY_URI}:V-${BUILD_NUMBER}
                    docker push "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}"
            """
        }
      }
    }
    }
	    }
   
	    
    stage('deploying to ECS') {
        environment {
        CLUSTER_NAME = "newCluster"
        SERVICE_NAME = "newService"
        TD_FAMILY="newTD"
	FILE="update-td.json"
        }
            steps{
                script {
                

                           sh """
                                
							   
                               TASK_REVISION=`aws ecs register-task-definition --family \${TD_FAMILY} --cli-input-json file://update-td.json --query taskDefinition.revision --output text`
                                                           
                               aws ecs update-service --cluster \${CLUSTER_NAME} --service \${SERVICE_NAME} --task-definition \${TD_FAMILY}:\${TASK_REVISION} --desired-count 1
                               
                               rm -f *.json
			       docker rmi -f ${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}
                               docker rmi -f ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}
							   
                            """
                               }
                            }
                        }
            
    }
}
