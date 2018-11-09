# Serverless Object Detection on AWS Lambda for Grassland Node Lite

### A live Tensorflow model deployed as an AWS Lambda function for miners running nodes without the processing power to run a full deep learning object detection model locally. 

This is the "server" in the mining client/server architecture for which the [node_lite](https://github.com/grasslandnetwork/node_lite) software is the "client". 

Uses [Serverless](https://serverless.com/) framework for turn-key deployment. Just change the options in the settings files (serverless.yml, env_var.sh, settings.py) to point to your AWS S3 buckets, unzip the pre-compiled Tensorflow dependencies into the "vendor" directory and deploy from your command line using `serverless deploy`.


#### Provisioning of Python dependencies
In the "vendored" folder, you have to provide the additional Python 3.6 dependencies required. These are Tensorflow 1.7.0, Pillow, Joblib and all of their dependencies except for the Tensorboard and Pip packages which were removed to get under the Lambda size limit. This should total ~257 MB unzipped. If you install Tensorflow 1.8 or higher, your "vendored" directory will breach the Lambda deployment limit of ~262 MB. These dependencies must be deployed along with the code into AWS Lambda. Because the Tensorflow and Pillow dependencies are large, I did not commit them to the repo. You can download the zipped vendored directory [here](https://downloads.grassland.network/packages/node_lite_object_detection/vendored.zip).


#### This software is released under the terms of the Grassland License. It's identical to the MIT license with the added restriction that the use of this Work or its Derivatives to gather data that comes from locations in which an uninformed third party would have no reasonable expectation of privacy is governed by our open data policy wherein all data gathered from such locations shall be sent to a registered Grassland Network server with the same frequency, format and specifications to that of approved Grassland Node implementations. Approved Grassland Node implementations can be found on our Github page located here -> [https://github.com/grasslandnetwork/](https://github.com/grasslandnetwork/)
