# This "utils.py" file is a modified version of https://github.com/Vetal1977/tf_aws_lambda/blob/1232355c591e1319a01902090f05572f2fdf9284/utils.py which is distributed under the MIT license

'''
Utilities for using in a project scope
'''
import io
import os
import zipfile

import boto3
import botocore

import settings
import numpy as np
from PIL import Image
import time



def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


def get_env_var_or_raise_exception(env_var_name):
    '''
    Get a value of the environment variable or raise an exception if it does not exist

    :param env_var_name: Environment variable name
    '''
    try:
        return os.environ[env_var_name]
    except Exception as _:
        raise Exception('Required environment variable {} not found!'.format(env_var_name))


def create_model_dir():
    '''
    Check target model directory for existence and create it if needed.
    We use /tmp directory, which is according to AWS Limits
    (see http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
    is Ephemeral disk capacity ("/tmp" space) and can be 512 MB big.

    :return: Path of the model directory
    '''
    ## Target directory for GAN model - it must be a subdirectory of /tmp
    # Target directory for Detection model - it must be a subdirectory of /tmpp
    # Check target directory for existence and create it if needed.
    #model_dir = '/tmp/gan_model'
    model_dir = '/tmp/detection_model'
    if not os.path.exists(model_dir):
        print('Going to create a model directory {}...'.format(model_dir))
        os.makedirs(model_dir)
        print('...success!')
    print('Model directory is {}'.format(model_dir))

    return model_dir


def download_model_from_bucket(model_dir):
    '''
    Downloads GAN model protobuf from S3 bucket if it was not downloaded yet
    '''
    # check the model file for existence and download if needed
    protobuf_file_name = get_env_var_or_raise_exception(settings.MODEL_PROTOBUF_FILE_NAME_ENV_VAR)
    model_path = model_dir + '/' + protobuf_file_name
    if not os.path.isfile(model_path):
        bucket_name = get_env_var_or_raise_exception(settings.S3_MODEL_BUCKET_NAME_ENV_VAR)
        s3_model_path = get_env_var_or_raise_exception(settings.S3_MODEL_PATH)
        print('Going to download a model file from S3 bucket {}/{}...'.format(
            bucket_name, s3_model_path
        ))

        # create S3 resource
        s3_res = boto3.resource('s3')
        target_model_path = model_dir + '/' + protobuf_file_name

        try:
            # download FILE
            s3_bucket = s3_res.Bucket(bucket_name)

            s3_bucket.download_file(
                s3_model_path,
                target_model_path)


        except botocore.exceptions.ClientError as exception:
            if exception.response['Error']['Code'] == "404":
                print("The object does not exist.")
            if exception.response['Error']['Code'] == "403":
                print("Access denied.")
            raise


def download_image_from_bucket(bucket_name, key):
    '''
    Download image from S3 bucket

    :param bucket_name: AWS S3 bucket name
    :param key: key in the bucket, efectively an image file name
    :return: image as byte array
    '''

    start_time = time.time()
    # create S3 resource
    s3_res = boto3.resource('s3')
    try:
        # download image into in-memory buffer
        print('Downloading the image from S3 bucket {}/{}'.format(bucket_name, key))
        s3_bucket = s3_res.Bucket(bucket_name)
        
        s3_bucket.download_file(str(key), '/tmp/'+str(key))
        print('Successfully downloaded the image')

        print("s3 Download Time:", time.time()-start_time)
        
        image = Image.open('/tmp/'+str(key))
        image_np = load_image_into_numpy_array(image)
        

        
        return image_np

    except botocore.exceptions.ClientError as exception:
        if exception.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
