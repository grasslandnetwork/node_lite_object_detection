#!/bin/bash
# run this file with 'source env_var.sh' or '. ./env_var.sh' to export variable
# into current shell environment

export TF_AWS_S3_MODEL_PATH='[REPLACE_ME: path/to/model/file/inside/bucket/]eon_0.pb'
export TF_AWS_MODEL_PROTOBUF_FILE_NAME='eon_0.pb'
export TF_AWS_S3_MODEL_BUCKET_NAME='[REPLACE_ME: GRASSLAND_MODEL_BUCKET]'
