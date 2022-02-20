**Wiem CHOUCHANE**

**Brunelle MALANDILA LEYA**

**M2 APP LS1**

&nbsp;

# Lab 4 - HDFS Architecture

## Benchmarking HDFS

- Quick test :

```
[wiem.chouchane@hadoop-edge01 ~]$ touch bonjour.txt
[wiem.chouchane@hadoop-edge01 ~]$ echo Hello > bonjour.txt
[wiem.chouchane@hadoop-edge01 ~]$ cat bonjour.txt
Hello
[wiem.chouchane@hadoop-edge01 ~]$ ls
average.py  basic.py  bonjour.txt  e_book.txt  lab3  local.txt  tree.py  tree.pyc
```

- Kerberos ticket intialization :

```
[wiem.chouchane@hadoop-edge01 ~]$ kinit wiem.chouchane
Password for wiem.chouchane@EFREI.ONLINE:
[wiem.chouchane@hadoop-edge01 ~]$
```

- What does the hadoop teragen/terasort command do ?

The ```teragen``` command generates rows of data to sort for the ```terasort``` command which samples the input data and sorts it into a total order.


- Use the teragen command to generate 100MB data file

As the ```teragen``` command expects a number of 100B rows, we will use 1 000 000 rows to reach 100MB data.

```
[wiem.chouchane@hadoop-edge01 ~]$ yarn jar /usr/odp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar \
> teragen -Dmapred.map.tasks=50 1000000 /user/wiem.chouchane/100_mb_sort_input
22/02/20 09:58:12 INFO impl.TimelineReaderClientImpl: Initialized TimelineReader URI=https://hadoop-master03.efrei.online:8199/ws/v2/timeline/, clusterId=yarn-cluster
22/02/20 09:58:13 INFO client.AHSProxy: Connecting to Application History server at hadoop-master03.efrei.online/163.172.102.23:10200
22/02/20 09:58:13 INFO hdfs.DFSClient: Created token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347493450, maxDate=1645952293450, sequenceNumber=12154, masterKeyId=188 on ha-hdfs:efrei
22/02/20 09:58:13 INFO security.TokenCache: Got dt for hdfs://efrei; Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347493450, maxDate=1645952293450, sequenceNumber=12154, masterKeyId=188)
22/02/20 09:58:13 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /user/wiem.chouchane/.staging/job_1640786961151_0074
22/02/20 09:58:13 INFO terasort.TeraGen: Generating 1000000 using 50
22/02/20 09:58:13 INFO mapreduce.JobSubmitter: number of splits:50
22/02/20 09:58:14 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1640786961151_0074
22/02/20 09:58:14 INFO mapreduce.JobSubmitter: Executing with tokens: [Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347493450, maxDate=1645952293450, sequenceNumber=12154, masterKeyId=188)]
22/02/20 09:58:14 INFO conf.Configuration: found resource resource-types.xml at file:/etc/hadoop/1.0.3.0-223/0/resource-types.xml
22/02/20 09:58:14 INFO impl.TimelineClientImpl: Timeline service address: hadoop-master03.efrei.online:8190
22/02/20 09:58:14 INFO impl.YarnClientImpl: Submitted application application_1640786961151_0074
22/02/20 09:58:14 INFO mapreduce.Job: The url to track the job: https://hadoop-master01.efrei.online:8090/proxy/application_1640786961151_0074/
22/02/20 09:58:14 INFO mapreduce.Job: Running job: job_1640786961151_0074
22/02/20 09:58:23 INFO mapreduce.Job: Job job_1640786961151_0074 running in uber mode : false
22/02/20 09:58:23 INFO mapreduce.Job:  map 0% reduce 0%
22/02/20 09:58:30 INFO mapreduce.Job:  map 2% reduce 0%
22/02/20 09:58:31 INFO mapreduce.Job:  map 14% reduce 0%
22/02/20 09:58:32 INFO mapreduce.Job:  map 26% reduce 0%
22/02/20 09:58:33 INFO mapreduce.Job:  map 36% reduce 0%
22/02/20 09:58:34 INFO mapreduce.Job:  map 38% reduce 0%
22/02/20 09:58:35 INFO mapreduce.Job:  map 58% reduce 0%
22/02/20 09:58:36 INFO mapreduce.Job:  map 70% reduce 0%
22/02/20 09:58:37 INFO mapreduce.Job:  map 78% reduce 0%
22/02/20 09:58:38 INFO mapreduce.Job:  map 88% reduce 0%
22/02/20 09:58:39 INFO mapreduce.Job:  map 100% reduce 0%
22/02/20 09:58:39 INFO mapreduce.Job: Job job_1640786961151_0074 completed successfully
22/02/20 09:58:39 INFO mapreduce.Job: Counters: 34
        File System Counters
                FILE: Number of bytes read=0
                FILE: Number of bytes written=13149390
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=4194
                HDFS: Number of bytes written=100000000
                HDFS: Number of read operations=300
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=100
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=50
                Other local map tasks=50
                Total time spent by all maps in occupied slots (ms)=496107
                Total time spent by all reduces in occupied slots (ms)=0
                Total time spent by all map tasks (ms)=165369
                Total vcore-milliseconds taken by all map tasks=165369
                Total megabyte-milliseconds taken by all map tasks=254006784
        Map-Reduce Framework
                Map input records=1000000
                Map output records=1000000
                Input split bytes=4194
                Spilled Records=0
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=4450
                CPU time spent (ms)=113810
                Physical memory (bytes) snapshot=13185810432
                Virtual memory (bytes) snapshot=170175361024
                Total committed heap usage (bytes)=13913030656
                Peak Map Physical memory (bytes)=279941120
                Peak Map Virtual memory (bytes)=3408351232
        org.apache.hadoop.examples.terasort.TeraGen$Counters
                CHECKSUM=2148987642402270
        File Input Format Counters
                Bytes Read=0
        File Output Format Counters
                Bytes Written=100000000
```

- Check :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -ls /user/wiem.chouchane/100_mb_sort_input
Found 51 items
-rw-r--r--   3 wiem.chouchane wiem.chouchane          0 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/_SUCCESS
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00000
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00001
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00002
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00003
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00004
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00005
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00006
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00007
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00008
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00009
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00010
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00011
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00012
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00013
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00014
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00015
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00016
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00017
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00018
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00019
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00020
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00021
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00022
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00023
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00024
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00025
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00026
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00027
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00028
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00029
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00030
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00031
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00032
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00033
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00034
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00035
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00036
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00037
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00038
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00039
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00040
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00041
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00042
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00043
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00044
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00045
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00046
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00047
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00048
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00049
```

- Use the terasort command to sort the previously generated data

```
[wiem.chouchane@hadoop-edge01 ~]$ yarn jar /usr/odp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar \
> terasort -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=25 /user/wiem.chouchane/100_mb_sort_input /user/wiem.chouchane/100_mb_sort_output
22/02/20 10:05:40 INFO terasort.TeraSort: starting
22/02/20 10:05:41 INFO hdfs.DFSClient: Created token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347941479, maxDate=1645952741479, sequenceNumber=12155, masterKeyId=188 on ha-hdfs:efrei
22/02/20 10:05:41 INFO security.TokenCache: Got dt for hdfs://efrei; Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347941479, maxDate=1645952741479, sequenceNumber=12155, masterKeyId=188)
22/02/20 10:05:41 INFO input.FileInputFormat: Total input files to process : 50
Spent 296ms computing base-splits.
Spent 2ms computing TeraScheduler splits.
Computing input splits took 298ms
Sampling 10 splits of 50
Making 25 from 100000 sampled records
Computing parititions took 315ms
Spent 614ms computing partitions.
22/02/20 10:05:42 INFO impl.TimelineReaderClientImpl: Initialized TimelineReader URI=https://hadoop-master03.efrei.online:8199/ws/v2/timeline/, clusterId=yarn-cluster
22/02/20 10:05:42 INFO client.AHSProxy: Connecting to Application History server at hadoop-master03.efrei.online/163.172.102.23:10200
22/02/20 10:05:42 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /user/wiem.chouchane/.staging/job_1640786961151_0075
22/02/20 10:05:42 INFO mapreduce.JobSubmitter: number of splits:50
22/02/20 10:05:42 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1640786961151_0075
22/02/20 10:05:42 INFO mapreduce.JobSubmitter: Executing with tokens: [Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645347941479, maxDate=1645952741479, sequenceNumber=12155, masterKeyId=188)]
22/02/20 10:05:42 INFO conf.Configuration: found resource resource-types.xml at file:/etc/hadoop/1.0.3.0-223/0/resource-types.xml
22/02/20 10:05:42 INFO impl.TimelineClientImpl: Timeline service address: hadoop-master03.efrei.online:8190
22/02/20 10:05:43 INFO impl.YarnClientImpl: Submitted application application_1640786961151_0075
22/02/20 10:05:43 INFO mapreduce.Job: The url to track the job: https://hadoop-master01.efrei.online:8090/proxy/application_1640786961151_0075/
22/02/20 10:05:43 INFO mapreduce.Job: Running job: job_1640786961151_0075
22/02/20 10:05:51 INFO mapreduce.Job: Job job_1640786961151_0075 running in uber mode : false
22/02/20 10:05:51 INFO mapreduce.Job:  map 0% reduce 0%
22/02/20 10:05:59 INFO mapreduce.Job:  map 16% reduce 0%
22/02/20 10:06:05 INFO mapreduce.Job:  map 18% reduce 0%
22/02/20 10:06:06 INFO mapreduce.Job:  map 44% reduce 0%
22/02/20 10:06:07 INFO mapreduce.Job:  map 100% reduce 0%
22/02/20 10:06:09 INFO mapreduce.Job:  map 100% reduce 48%
22/02/20 10:06:10 INFO mapreduce.Job:  map 100% reduce 68%
22/02/20 10:06:11 INFO mapreduce.Job:  map 100% reduce 100%
22/02/20 10:06:12 INFO mapreduce.Job: Job job_1640786961151_0075 completed successfully
22/02/20 10:06:13 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=104013350
                FILE: Number of bytes written=227867830
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=100006400
                HDFS: Number of bytes written=100000000
                HDFS: Number of read operations=275
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=50
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=50
                Launched reduce tasks=25
                Other local map tasks=4
                Data-local map tasks=46
                Total time spent by all maps in occupied slots (ms)=1820775
                Total time spent by all reduces in occupied slots (ms)=455908
                Total time spent by all map tasks (ms)=606925
                Total time spent by all reduce tasks (ms)=113977
                Total vcore-milliseconds taken by all map tasks=606925
                Total vcore-milliseconds taken by all reduce tasks=113977
                Total megabyte-milliseconds taken by all map tasks=932236800
                Total megabyte-milliseconds taken by all reduce tasks=233424896
        Map-Reduce Framework
                Map input records=1000000
                Map output records=1000000
                Map output bytes=102000000
                Map output materialized bytes=104007500
                Input split bytes=6400
                Combine input records=0
                Combine output records=0
                Reduce input groups=1000000
                Reduce shuffle bytes=104007500
                Reduce input records=1000000
                Reduce output records=1000000
                Spilled Records=2000000
                Shuffled Maps =1250
                Failed Shuffles=0
                Merged Map outputs=1250
                GC time elapsed (ms)=16714
                CPU time spent (ms)=230450
                Physical memory (bytes) snapshot=66050535424
                Virtual memory (bytes) snapshot=267194114048
                Total committed heap usage (bytes)=67689250816
                Peak Map Physical memory (bytes)=1179590656
                Peak Map Virtual memory (bytes)=3407011840
                Peak Reduce Physical memory (bytes)=333111296
                Peak Reduce Virtual memory (bytes)=3886354432
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=100000000
        File Output Format Counters
                Bytes Written=100000000
22/02/20 10:06:13 INFO terasort.TeraSort: done
```

- Validate the data generated by the sort :

```
[wiem.chouchane@hadoop-edge01 ~]$ yarn jar /usr/odp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar \
> teravalidate -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=25 /user/wiem.chouchane/100_mb_sort_output /user/wiem.chouchane/100_mb_validate_output
22/02/20 10:09:24 INFO impl.TimelineReaderClientImpl: Initialized TimelineReader URI=https://hadoop-master03.efrei.online:8199/ws/v2/timeline/, clusterId=yarn-cluster
22/02/20 10:09:25 INFO client.AHSProxy: Connecting to Application History server at hadoop-master03.efrei.online/163.172.102.23:10200
22/02/20 10:09:25 INFO hdfs.DFSClient: Created token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645348165372, maxDate=1645952965372, sequenceNumber=12156, masterKeyId=188 on ha-hdfs:efrei
22/02/20 10:09:25 INFO security.TokenCache: Got dt for hdfs://efrei; Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645348165372, maxDate=1645952965372, sequenceNumber=12156, masterKeyId=188)
22/02/20 10:09:25 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /user/wiem.chouchane/.staging/job_1640786961151_0076
22/02/20 10:09:25 INFO input.FileInputFormat: Total input files to process : 25
Spent 34ms computing base-splits.
Spent 1ms computing TeraScheduler splits.
22/02/20 10:09:25 INFO mapreduce.JobSubmitter: number of splits:25
22/02/20 10:09:26 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1640786961151_0076
22/02/20 10:09:26 INFO mapreduce.JobSubmitter: Executing with tokens: [Kind: HDFS_DELEGATION_TOKEN, Service: ha-hdfs:efrei, Ident: (token for wiem.chouchane: HDFS_DELEGATION_TOKEN owner=wiem.chouchane@EFREI.ONLINE, renewer=yarn, realUser=, issueDate=1645348165372, maxDate=1645952965372, sequenceNumber=12156, masterKeyId=188)]
22/02/20 10:09:26 INFO conf.Configuration: found resource resource-types.xml at file:/etc/hadoop/1.0.3.0-223/0/resource-types.xml
22/02/20 10:09:26 INFO impl.TimelineClientImpl: Timeline service address: hadoop-master03.efrei.online:8190
22/02/20 10:09:26 INFO impl.YarnClientImpl: Submitted application application_1640786961151_0076
22/02/20 10:09:26 INFO mapreduce.Job: The url to track the job: https://hadoop-master01.efrei.online:8090/proxy/application_1640786961151_0076/
22/02/20 10:09:26 INFO mapreduce.Job: Running job: job_1640786961151_0076
22/02/20 10:09:34 INFO mapreduce.Job: Job job_1640786961151_0076 running in uber mode : false
22/02/20 10:09:34 INFO mapreduce.Job:  map 0% reduce 0%
22/02/20 10:09:41 INFO mapreduce.Job:  map 36% reduce 0%
22/02/20 10:09:42 INFO mapreduce.Job:  map 100% reduce 0%
22/02/20 10:09:46 INFO mapreduce.Job:  map 100% reduce 100%
22/02/20 10:09:47 INFO mapreduce.Job: Job job_1640786961151_0076 completed successfully
22/02/20 10:09:48 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=2156
                FILE: Number of bytes written=6853752
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=100003225
                HDFS: Number of bytes written=23
                HDFS: Number of read operations=80
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=25
                Launched reduce tasks=1
                Data-local map tasks=25
                Total time spent by all maps in occupied slots (ms)=430839
                Total time spent by all reduces in occupied slots (ms)=10616
                Total time spent by all map tasks (ms)=143613
                Total time spent by all reduce tasks (ms)=2654
                Total vcore-milliseconds taken by all map tasks=143613
                Total vcore-milliseconds taken by all reduce tasks=2654
                Total megabyte-milliseconds taken by all map tasks=220589568
                Total megabyte-milliseconds taken by all reduce tasks=5435392
        Map-Reduce Framework
                Map input records=1000000
                Map output records=75
                Map output bytes=2000
                Map output materialized bytes=2300
                Input split bytes=3225
                Combine input records=0
                Combine output records=0
                Reduce input groups=51
                Reduce shuffle bytes=2300
                Reduce input records=75
                Reduce output records=1
                Spilled Records=150
                Shuffled Maps =25
                Failed Shuffles=0
                Merged Map outputs=25
                GC time elapsed (ms)=2579
                CPU time spent (ms)=51670
                Physical memory (bytes) snapshot=29367644160
                Virtual memory (bytes) snapshot=88910200832
                Total committed heap usage (bytes)=29853483008
                Peak Map Physical memory (bytes)=1178206208
                Peak Map Virtual memory (bytes)=3406876672
                Peak Reduce Physical memory (bytes)=289476608
                Peak Reduce Virtual memory (bytes)=3878621184
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=100000000
        File Output Format Counters
                Bytes Written=23
```

- List the created directory and print the size of each directory

Terasort input directory :
```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -ls /user/wiem.chouchane/100_mb_sort_input
Found 51 items
-rw-r--r--   3 wiem.chouchane wiem.chouchane          0 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/_SUCCESS
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00000
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00001
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00002
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00003
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00004
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00005
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00006
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00007
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00008
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00009
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00010
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00011
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00012
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00013
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00014
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00015
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00016
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00017
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00018
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00019
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00020
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00021
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00022
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00023
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00024
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00025
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00026
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00027
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00028
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00029
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00030
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00031
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00032
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00033
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00034
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00035
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00036
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00037
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00038
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00039
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00040
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00041
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00042
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00043
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00044
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00045
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00046
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00047
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00048
-rw-r--r--   3 wiem.chouchane wiem.chouchane    2000000 2022-02-20 09:58 /user/wiem.chouchane/100_mb_sort_input/part-m-00049
```

Terasort output directory :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -ls /user/wiem.chouchane/100_mb_sort_output
Found 27 items
-rw-r--r--   1 wiem.chouchane wiem.chouchane          0 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/_SUCCESS
-rw-r--r--  10 wiem.chouchane wiem.chouchane        264 2022-02-20 10:05 /user/wiem.chouchane/100_mb_sort_output/_partition.lst
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3932700 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00000
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3936000 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00001
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4013900 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00002
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4021700 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00003
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4022900 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00004
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3993500 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00005
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4002100 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00006
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4015100 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00007
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4046300 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00008
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4038600 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00009
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4082500 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00010
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4104900 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00011
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3957900 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00012
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3933800 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00013
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4077300 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00014
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3981500 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00015
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3994100 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00016
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4087800 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00017
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3977800 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00018
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4012000 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00019
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3958300 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00020
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3876200 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00021
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3966500 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00022
-rw-r--r--   1 wiem.chouchane wiem.chouchane    4028800 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00023
-rw-r--r--   1 wiem.chouchane wiem.chouchane    3937800 2022-02-20 10:06 /user/wiem.chouchane/100_mb_sort_output/part-r-00024
```

Teravalidate output directory :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -ls /user/wiem.chouchane/100_mb_validate_output
Found 2 items
-rw-r--r--   3 wiem.chouchane wiem.chouchane          0 2022-02-20 10:09 /user/wiem.chouchane/100_mb_validate_output/_SUCCESS
-rw-r--r--   3 wiem.chouchane wiem.chouchane         23 2022-02-20 10:09 /user/wiem.chouchane/100_mb_validate_output/part-r-00000
```

Terasort input directory size :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -count -h /user/wiem.chouchane/100_mb_sort_input
           1           51             95.4 M /user/wiem.chouchane/100_mb_sort_input
```

The terasort input directory size is 95.4 M which is approximately 100MB (but is more SI than IEC compliant).

Terasort output directory size :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -count -h /user/wiem.chouchane/100_mb_sort_output
           1           27             95.4 M /user/wiem.chouchane/100_mb_sort_output

```

The terasort output directory size is 95.4 M which is approximately 100MB (but is more SI than IEC compliant), it's the same as the input directory size, which is normal as terasort is only expected to sort data.

Teravalidate output directory size :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -count -h /user/wiem.chouchane/100_mb_validate_output
           1            2                 23 /user/wiem.chouchane/100_mb_validate_output

```

As for the teravalidate output directory size, if we display the validation output :

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -cat /user/wiem.chouchane/100_mb_validate_output/part-r-00000
checksum        7a27e2d0d55de
```

it shows the validation checksum, which is 23 bytes long as described by the -count -h output.

- What can you tell about speed of read/write ?

In the HDFS output of the ```teragen``` command :

```
File System Counters
                FILE: Number of bytes read=0
                FILE: Number of bytes written=13149390
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=4194
                HDFS: Number of bytes written=100000000
                HDFS: Number of read operations=300
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=100
                HDFS: Number of bytes read erasure-coded=0
```

```
22/02/20 09:58:14 INFO mapreduce.Job: Running job: job_1640786961151_0074
22/02/20 09:58:39 INFO mapreduce.Job: Job job_1640786961151_0074 completed successfully
```

It shows that HDFS proceeded to read 4194 bytes in 300 operations which makes a rate of almost 13 bytes read per operation. However, it wrote 100000000 bytes in 100 operations, which makes a rate of 1 000 000 bytes written per operation. Also, it began at 09:58:14 AM and ended at 09:58:39 AM, which means it performed all of this in 25 seconds (which is pretty fast).

In the HDFS output of the ```terasort``` command :

```
File System Counters
                FILE: Number of bytes read=104013350
                FILE: Number of bytes written=227867830
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=100006400
                HDFS: Number of bytes written=100000000
                HDFS: Number of read operations=275
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=50
                HDFS: Number of bytes read erasure-coded=0
```

```
22/02/20 10:05:43 INFO mapreduce.Job: Running job: job_1640786961151_0075
22/02/20 10:06:12 INFO mapreduce.Job: Job job_1640786961151_0075 completed successfully
```

It shows that HDFS proceeded to read 100006400 bytes in 275 operations which makes a rate of almost 363 660 bytes read per operation. However, it wrote 100000000 bytes in 50 operations, which makes a rate of 2 000 000 bytes written per operation. Also, it began at 10:05:43 AM and ended at 10:06:12 AM, which means it performed all of this in 29 seconds (which is also pretty fast).

