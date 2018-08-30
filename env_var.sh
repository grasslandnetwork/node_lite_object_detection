#!/bin/bash
# run this file with 'source env_var.sh' or '. ./env_var.sh' to export variable
# into current shell environment

export TF_AWS_S3_MODEL_PATH='tensorflow/faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb'
export TF_AWS_MODEL_PROTOBUF_FILE_NAME='frozen_inference_graph.pb'
export TF_AWS_S3_MODEL_BUCKET_NAME='grassland-models-00'
