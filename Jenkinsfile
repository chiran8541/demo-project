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
		def buildFlag = false //Overwritten by yaml
                def deployFlag = false //Overwritten by yaml
		echo "${buildflag}"
		
		
	}
      }
	    } 
    }
}
  
  
		    

def getParams(section,specfile){
  def data = getYaml(specfile)
  def params = data[section]
  def parmMap = [:]
  for(String item in params) {
      def k = item.keySet()[0].toString()
      def v = item[k]
      parmMap[k] = v
  }
  return parmMap
}
