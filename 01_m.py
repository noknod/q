#!/usr/bin/env python


import os
import sys
import re

# 196.223.28.31 - - [16/Nov/2015:00:00:00 +0400] "GET /photo/manage.cgi HTTP/1.1" 200 0 "-" "Mozilla/6.66"


TEMPLATE = """
#!/usr/bin/env bash

OUT_DIR=out
NUM_REDUCERS=1 # > 0 to run the Reduce phase
CONFIG="--config /home/agorokhov/conf.empty"

hdfs dfs -rm -r -skipTrash out

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="Uniq users step1" \
    -D mapreduce.job.reduces=$NUM_REDUCERS \
    -files metric01_1_mapper.py,metric01_1_reducer.py \
    -mapper "./metric01_1_mapper.py" \
    -reducer "./metric01_1_reducer.py" \
    -input hdfs://{0} \
    -output out
"""



def main():
    """files = []
    with open('./dirs.txt', 'r') as infile:
        cnt = 1
        for line in infile.readlines():
            if cnt == 1:
                cnt = 2
            else:
                #print line.strip().split(' ')
                path = line.split(' ')[-1].strip()
                print path
                os.system('hdfs dfs -ls ' + path + ' > ./tmp.txt')
                tmp_cnt = 1
                with open('./tmp.txt', 'r') as tif:
                    for tmp_line in tif.readlines():
                        if tmp_cnt == 1:
                           tmp_cnt = 2
                        else:
                            file_path = tmp_line.split(' ')[-1].strip()
                            print file_path
                            files.append(file_path) 
                #break
    """
    files = []
    with open ('./files.txt', 'r' ) as infile:
        for file_path in infile.readlines():
            file_path = file_path.strip()
            files.append(file_path)

    for file_path in files[3:]:
            print(file_path)
            command = TEMPLATE.format(file_path)
            result_code = int(os.system(command))
            if result_code != 0:
                print '\n\n*********\n\nERROR\n\n*********\n\n'
                break
            #print(command)
            dir_path = file_path.split('/')[-2]
            command = 'hdfs dfs -mkdir hw1/metrics/{0}'.format(dir_path)
            result_command = int(os.system(command))
            if result_command != 0:
                print '\n\n---------\n\nERROR\n\n---------\n\n'
                break
            command = 'hdfs dfs -cp out/part-00000 hw1/metrics/{0}/m1_1_2.txt'.format(dir_path)
            result_command = int(os.system(command))
            if result_command != 0:
                print '\n\n++++++++++\n\nERROR\n\n++++++++++\n\n'
                break

            #print(command)
            #break

if __name__ == '__main__':
    main()

