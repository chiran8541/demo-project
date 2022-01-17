pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="188274256193"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="demoapp"
        IMAGE_TAG="first"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
   
    stages {
        
         stage('Logging into AWS ECR') {
            steps {
                script {
//                 sh "aws configure list"
                sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com"
                }
                 
            }
        }
       
  
    // Building Docker images
    stage('Building image & Push to ECR') {
      steps{
        script {
            if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                            buildno = "@buildno@"
                            currentbuildno = currentBuild.number
            sh """
                    sed -i -e 's#${buildno}#${currentbuildno}#' nonprod-td.json
                    cp nonprod-td.json /etc/
                    cd /etc
                    dockerImage = docker.build "${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}"
                    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com"
                    docker tag ${IMAGE_REPO_NAME}:V-${BUILD_NUMBER} ${REPOSITORY_URI}:V-${BUILD_NUMBER}"
                    docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}"
            """
        }
      }
    }
   
   
        
    stage('deploying to ECS') {
        environment {
        CLUSTER_NAME = "2FNV-ME005-MeterOps-ECS-Cluster"
        SERVICE_NAME = "ME005-UI-P2"
        AWS_PROFILE= "ME005-NonProdENV-Build"
        TD_FAMILY="2FNV-ME005-UI-P2-TD"
		FILE="nonprod-td.json"
        }
            steps{
                script {
                

                           sh """
                                
							   
                               TASK_REVISION=`aws ecs register-task-definition --family \${TD_FAMILY} --tags key=AppCode,value=ME005 key=AppName,value=MeterOps --cli-input-json file://nonprod-td.json --profile \${AWS_PROFILE} --query taskDefinition.revision --output text`
                                                           
                               aws ecs update-service --cluster \${CLUSTER_NAME} --service \${SERVICE_NAME} --task-definition \${TD_FAMILY}:\${TASK_REVISION} --desired-count 1 --profile \${AWS_PROFILE}
                               
                               rm -f *.json
							   docker rmi -f ${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}
                               docker rmi -f ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:V-${BUILD_NUMBER}
							   
                            """
                               }
                            }
                        }
            
    }
}
