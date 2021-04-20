import groovy.json.JsonOutput
pipeline {
  agent any
  environment {
    GIT_COMMIT = sh (script: "git log -n 1 --pretty=format:'%h' --abbrev=7", returnStdout: true)
  }
  stages {
    stage('Test') {
      agent{
       docker{
           image 'python:3.8'
           reuseNode true
           args '-u root:root'
       }
     }
      steps {
       script {
            sh 'pip install --user -r requirements/test.txt'
            sh 'python -m unittest discover -s ./test --pattern \'*.py\' '
        }
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("dsp/eland-preprocessing:${env.BUILD_NUMBER}_${GIT_COMMIT}")
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry('http://dockerhub.vpon.com') {
            dockerImage.push("${env.BUILD_NUMBER}_${GIT_COMMIT}")
             dockerImage.push('latest')
          }
        }
      }
    }
  }
  post {
          success {
            script {
              def data = [
                attachments:[
                [
                  "color" : "#36a64f",
                  "title" : "Jenkins-Test-Result",
                  "title_link" : "$env.BUILD_URL",
                  "fields" :[
                    [
                      "title": "JobName",
                      "value": "$env.JOB_NAME",
                    ],,
                    [
                      "title": "BranchName",
                      "value": "$env.BRANCH_NAME",
                    ],
                    [
                      "title": "CommitHash",
                      "value": "$GIT_COMMIT",
                    ],
                    [
                      "title": "BuildNumber",
                      "value": "$BUILD_NUMBER",
                    ],
                    [
                      "title": "ImageName",
                      "value": "dsp/eland-preprocessing:${env.BUILD_NUMBER}_${GIT_COMMIT}",
                    ]
                  ]
                ]
              ]
            ]
              def json = JsonOutput.toJson(data)
              slackSend(json)
            }
          }
          failure {
            script {
            def data = [
                attachments:[
                [
                  "color" : "#FF0000",
                  "title" : "Jenkins-Test-Result",
                  "title_link" : "$env.BUILD_URL",
                  "fields" :[
                    [
                      "title": "JobName",
                      "value": "$env.JOB_NAME",
                    ],,
                    [
                      "title": "BranchName",
                      "value": "$env.BRANCH_NAME",
                    ],
                    [
                      "title": "CommitHash",
                      "value": "$GIT_COMMIT",
                    ],
                    [
                      "title": "BuildNumber",
                      "value": "$BUILD_NUMBER",
                    ]
                  ]
                ]
              ]
            ]
              def message = JsonOutput.toJson(data)
              slackSend(message.toString())
            }
          }
  }
}

def slackSend(message){
  def s ='''
    curl -X POST -H \'Content-type: application/json\' --data \'%s\' https://hooks.slack.com/services/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
  '''
  sh String.format(s,message)
}
