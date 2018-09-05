# Serverless Object Detection on AWS Lambda for Grassland Node Lite

### A live Tensorflow model deployed as an AWS Lambda function for miners running nodes without the processing power to run a full deep learning object detection model locally. 

This is the "server" in the mining client/server architecture for which the [node_lite](https://github.com/grasslandnetwork/node_lite) software is the "client". 

Uses [Serverless](https://serverless.com/) framework for turn-key deployment. Just change the options in the settings files (serverless.yml, env_var.sh, settings.py) to point to your AWS S3 buckets, unzip the pre-compiled Tensorflow dependencies into the "vendor" directory and deploy from your command line using `serverless deploy`.
