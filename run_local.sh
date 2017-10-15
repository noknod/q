#!/usr/bin/env bash

OUT_DIR=out
NUM_REDUCERS=1 # > 0 to run the Reduce phase
CONFIG="--config /home/agorokhov/conf.empty"

hdfs ${CONFIG} dfs -rm -r -skipTrash ${OUT_DIR}

yarn ${CONFIG} jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="Uniq users step1" \
    -D mapreduce.job.reduces=$NUM_REDUCERS \
    -files metric01_1_mapper.py, metric01_1_reducer.py \
    -mapper "./metric01_1_mapper.py" \
    -reducer "./metric01_1_reducer.py" \
    -input in \
    -output ${OUT_DIR}

# TODO:
# - run in distributed mode (on the cluster)
# - implement the reducer
