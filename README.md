# Serverless Object Detection on AWS Lambda for Grassland Node Lite

### A live Tensorflow model deployed as an AWS Lambda function for miners running nodes without the processing power to run a full deep learning object detection model locally. 

This is the "server" in the mining client/server architecture for which the [node_lite](https://github.com/grasslandnetwork/node_lite) software is the "client".


If you have questions related to this software, search in the 'Issues' tab of this Github repo to see if it's been answered. If not, feel free to open a new issue and I'll get back to you as soon as I can.


### Uses [Serverless](https://serverless.com/) framework for turn-key deployment.

## Installation

1. Serverless CLI requires Node.js v6.5.0 or greater. But to ensure compatibility with Grassland's GUI you will need Node.js v8.10.0 or greater

2. Install the Serverless CLI using the command

```npm install -g serverless```

3. Get an AWS account. If you don't already have one, you can sign up for a [free trial](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/) that includes 1 million free Lambda requests per month.

4. Set-up your Provider (AWS) Credentials by following [these instructions](https://serverless.com/framework/docs/providers/aws/guide/credentials/) or [Watch the video on setting up credentials](https://www.youtube.com/watch?v=KngM5bfpttA)

You should have your AWS Keys set up as environment variables. You can include them in your ```~/.bashrc``` (Linux) file to ensure they are automatically set every time you load your shell. 

```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
# 'export' command is valid only for unix shells. In Windows - use 'set' instead of 'export'
```

To load your new environment variables and make them available to your shell, you'll either need to close and reopen your shell or type ```source ~/.bashrc```

5. Go to the AWS website and create two AWS S3 Buckets. One for the frames on which we will perform object detection, And one for the model.

6. Download the current eon's model from the [main website](https://www.grassland.network/) at the bottom under "Downloads" and upload it to the S3 bucket you made to hold the model

7. Clone this repo on your local machine and `cd` to the root directory

   Change the options in the files serverless.yml and env_var.sh to point to your AWS S3 buckets...

    Anywhere you see ```[REPLACE_ME: ...]``` replace it (including the brackets) with either the name of or the indicated S3 Bucket information you created in part 5 above.

   Then unzip the pre-compiled Tensorflow dependencies into the "vendor" directory (See 'Provisioning of Python Dependencies' below) and deploy from your command line using `serverless deploy`.

   For service removal:
   ```	   
   serverless remove
   ```			  
   DO NOT DELETE LAMBDA FUNCTIONS MANUALLY, OTHERWISE SERVERLESS WILL FAIL TO DEPLOY NEXT TIME!


   Once it's complete, it should show you your new Lambda function's URL. Set this URL as an environment variable on your system.

   ```
   export LAMBDA_DETECTION_URL=<your-lambda-url-here>
   ```

To complete the setup of your node, return to the instructions in the [Grassland Node's README](https://github.com/grasslandnetwork/node_lite)




#### Provisioning of Python dependencies
In the "vendored" folder, you have to provide the additional Python 3.6 dependencies required. These are Tensorflow 1.7.0, Pillow, Joblib and all of their dependencies except for the Tensorboard and Pip packages which were removed to get under the Lambda size limit. This should total ~257 MB unzipped. If you install Tensorflow 1.8 or higher, your "vendored" directory will breach the Lambda deployment limit of ~262 MB. These dependencies must be deployed along with the code into AWS Lambda. Because the Tensorflow and Pillow dependencies are large, I did not commit them to the repo. You can download the zipped vendored directory [here](https://downloads.grassland.network/packages/node_lite_object_detection/vendored.zip).



## Future Grassland Software Improvements
[Link to current list](https://gist.github.com/00hello/0199d393e872ed7645979f5daf7bd62c) of Grassland features and modules that will be built next


## License
#### Unless otherwise specified, this software is released under the terms of the Grassland License. It's identical to the Mozilla Public License 2.0 with the added restriction that the use of this Work or its Derivatives to gather data that comes from locations in which an uninformed third party would have no reasonable expectation of privacy is governed by our open data policy wherein all data gathered from such locations shall be made freely available to anyone with the same frequency, format and specifications to that of approved Grassland Node implementations. Approved Grassland Node implementations can be found on our Github page located here -> [https://github.com/grasslandnetwork/](https://github.com/grasslandnetwork/)

