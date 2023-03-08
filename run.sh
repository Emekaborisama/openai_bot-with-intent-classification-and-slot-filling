
# install docker first else if docker exist run the command below to build and run docker container 


docker build -t fast_api_chatbot . && docker run -d --name my-container fast_api_chatbot:latest
