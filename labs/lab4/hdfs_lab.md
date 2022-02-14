**Wiem CHOUCHANE**

**Brunelle MALANDILA LEYA**

**M2 APP LS1**

&nbsp;

# Lab 4 - HDFS

### 1.2 Working with the Hadoop cluster

- **Create a new text document called bonjour.txt, put something in it**

```shell
touch bonjour.txt
```

- **List the files with ls, display the bonjour.txt file, edit it with nano or vi**

ls

```
average.py  basic.py  bonjour.txt  lab3  tree.py  tree.pyc
```

cat bonjour.txt

```

```

nano bonjour.txt

cat bonjour.txt

```
Hello !
```

### 1.3 Working on HDFS

#### 1.3.1 Kerberos

kinit wiem.chouchane

#### 1.3.2 Basic HDFS Commands

hdfs dfs -ls

```
Found 2 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
```

hdfs dfs -ls /

```
Found 13 items
drwxrwxrwt   - yarn   hadoop          0 2021-12-14 23:25 /app-logs
drwxr-xr-x   - hdfs   hdfs            0 2021-09-28 10:18 /apps
drwxr-xr-x   - yarn   hadoop          0 2021-09-02 20:56 /ats
drwxr-xr-x   - hdfs   hdfs            0 2021-09-02 20:56 /atsv2
drwxr-xr-x   - mapred hdfs            0 2021-09-02 20:56 /mapred
drwxrwxrwx   - mapred hadoop          0 2021-09-02 20:56 /mr-history
drwxr-xr-x   - hdfs   hdfs            0 2021-09-02 20:56 /odp
drwxr-xr-x   - hdfs   hdfs            0 2021-09-02 20:56 /ranger
drwxr-xr-x   - hdfs   hdfs            0 2021-09-02 20:56 /services
drwxrwxrwx   - spark  hadoop          0 2021-12-01 11:46 /spark2-history
drwxrwxrwx   - hdfs   hdfs            0 2021-12-30 10:46 /tmp
drwxr-xr-x   - hdfs   hdfs            0 2022-01-31 10:17 /user
drwxr-xr-x   - hdfs   hdfs            0 2021-09-02 20:58 /warehouse
```

hdfs dfs -ls /

```
drwxr-xr-x   - wiem.chouchane                     wiem.chouchane                              0 2022-02-14 09:03 /user/wiem.chouchane
```

hdfs dfs -ls -R -h /

```
chenut.db
drwxrwxrwx+  - hive                               hadoop                                       0 2021-11-04 15:44 /warehouse/tablespace/external/hive/williamchenut.db/trees_external
drwxr-xr-x+  - hive                               hadoop                                       0 2021-11-04 14:57 /warehouse/tablespace/external/hive/wzouitene.db
drwxrwxrwx+  - hive                               hadoop                                       0 2021-11-04 14:57 /warehouse/tablespace/external/hive/wzouitene.db/trees_external
drwxr-xr-x+  - hive                               hadoop                                       0 2021-10-13 03:07 /warehouse/tablespace/external/hive/ymaassouli.db
drwxrwxrwx+  - hive                               hadoop                                       0 2021-10-13 03:07 /warehouse/tablespace/external/hive/ymaassou
```

hdfs dfs -mkdir dossier 

hdfs dfs -ls /user/wiem.chouchane

```
[wiem.chouchane@hadoop-edge01 ~]$ hdfs dfs -ls /user/wiem.chouchane
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 /user/wiem.chouchane/.Trash
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 /user/wiem.chouchane/dossier
```

hdfs dfs -put bonjour.txt

hdfs dfs -ls -R

```
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current/user
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:14 .Trash/Current/user/wiem.chouchane
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-12-01 11:56 .Trash/Current/user/wiem.chouchane/.sparkStaging
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:03 .Trash/Current/user/wiem.chouchane/bonjour.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane      16680 2021-11-30 09:44 .Trash/Current/user/wiem.chouchane/trees.csv
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane        384 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount/job.properties
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib
-rw-r--r--   3 wiem.chouchane wiem.chouchane     316498 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib/hadoop-mapreduce-examples-3.2.2.1.0.3.0-223.jar
-rw-r--r--   3 wiem.chouchane wiem.chouchane       1895 2021-11-29 22:25 .Trash/Current/user/wiem.chouchane/wordcount/workflow.xml
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:14 bonjour.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 dossier
```

hdfs dfs -cat bonjour.txt

```
Hello !
```

hdfs dfs -cat bonjour.txt | more

```
Hello !
```

hdfs dfs -tail bonjour.txt

```
Hello !
```

hdfs dfs -rm bonjour.txt

```
22/02/14 09:18:32 INFO fs.TrashPolicyDefault: Moved: 'hdfs://efrei/user/wiem.chouchane/bonjour.txt' to trash at: hdfs://efrei/user/wiem.chouchane/.Trash/Current/user/wiem.chouchane/bonjour.txt1644826712962
```

hdfs dfs -ls

```
Found 2 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 dossier
```

hdfs dfs -copyFromLocal bonjour.txt

hdfs dfs -ls

```
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 bonjour.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 dossier
```

hdfs dfs -chmod go+w bonjour.txt

hdfs dfs -ls

```
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
-rw-rw-rw-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 bonjour.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 dossier
```

hdfs dfs -chmod go-r bonjour.txt

hdfs dfs -ls

```
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 bonjour.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:11 dossier
```

hdfs dfs -mv bonjour.txt dossier/bonjour.txt

hdfs dfs -ls -R

```
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current/user
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:18 .Trash/Current/user/wiem.chouchane
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-12-01 11:56 .Trash/Current/user/wiem.chouchane/.sparkStaging
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:03 .Trash/Current/user/wiem.chouchane/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:14 .Trash/Current/user/wiem.chouchane/bonjour.txt1644826712962
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane      16680 2021-11-30 09:44 .Trash/Current/user/wiem.chouchane/trees.csv
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane        384 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount/job.properties
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib
-rw-r--r--   3 wiem.chouchane wiem.chouchane     316498 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib/hadoop-mapreduce-examples-3.2.2.1.0.3.0-223.jar
-rw-r--r--   3 wiem.chouchane wiem.chouchane       1895 2021-11-29 22:25 .Trash/Current/user/wiem.chouchane/wordcount/workflow.xml
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:22 dossier
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 dossier/bonjour.txt
```

hdfs dfs -get dossier/bonjour.txt demat.txt

ls

```
average.py  basic.py  bonjour.txt  demat.txt  lab3  tree.py  tree.pyc
```

cat demat.txt

```
Hello !
```

hdfs dfs -get dossier/bonjour.txt demat.txt

ls

```
average.py  basic.py  bonjour.txt  demat.txt  lab3  tree.py  tree.pyc
```

cat demat.txt

```
Hello !
```

clear

hdfs dfs -cp dossier/bonjour.txt dossier/salut.txt

hdfs dfs -ls -R /user/wiem.chouchane/dossier

```
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 /user/wiem.chouchane/dossier/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:24 /user/wiem.chouchane/dossier/salut.txt
```

hdfs dfs -cat /user/wiem.chouchane/dossier/salut.txt
```
Hello !
```

hdfs dfs -count -h /user/wiem.chouchane
```
          15            8            327.6 K /user/wiem.chouchane
```

hdfs dfs -rm dossier/bonjour.txt
```
22/02/14 09:26:40 INFO fs.TrashPolicyDefault: Moved: 'hdfs://efrei/user/wiem.chouchane/dossier/bonjour.txt' to trash at: hdfs://efrei/user/wiem.chouchane/.Trash/Current/user/wiem.chouchane/dossier/bonjour.txt
```

hdfs dfs -ls -R dossier
```
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:24 dossier/salut.txt
```

hdfs dfs -rm -r -skipTrash dossier
```
Deleted dossier
```

hdfs dfs -ls -R
```
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current/user
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:26 .Trash/Current/user/wiem.chouchane
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-12-01 11:56 .Trash/Current/user/wiem.chouchane/.sparkStaging
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:03 .Trash/Current/user/wiem.chouchane/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:14 .Trash/Current/user/wiem.chouchane/bonjour.txt1644826712962
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/output
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:26 .Trash/Current/user/wiem.chouchane/dossier
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 .Trash/Current/user/wiem.chouchane/dossier/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane      16680 2021-11-30 09:44 .Trash/Current/user/wiem.chouchane/trees.csv
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane        384 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount/job.properties
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib
-rw-r--r--   3 wiem.chouchane wiem.chouchane     316498 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib/hadoop-mapreduce-examples-3.2.2.1.0.3.0-223.jar
-rw-r--r--   3 wiem.chouchane wiem.chouchane       1895 2021-11-29 22:25 .Trash/Current/user/wiem.chouchane/wordcount/workflow.xml
```


rm demat.txt bonjour.txt

ls

```
average.py  basic.py  lab3  tree.py  tree.pyc
```


#### 1.3.3 Uploading a file to HDFS

wget https://www.gutenberg.org/files/84/84-0.txt

```
--2022-02-14 09:33:25--  https://www.gutenberg.org/files/84/84-0.txt
Resolving www.gutenberg.org (www.gutenberg.org)... 152.19.134.47, 2610:28:3090:3000:0:bad:cafe:47
Connecting to www.gutenberg.org (www.gutenberg.org)|152.19.134.47|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 448821 (438K) [text/plain]
Saving to: ‘84-0.txt’

100%[====================================================================================================================>] 448,821      878KB/s   in 0.5s

2022-02-14 09:33:26 (878 KB/s) - ‘84-0.txt’ saved [448821/448821]
```

ls
```
84-0.txt  average.py  basic.py  lab3  tree.py  tree.pyc
```

mv 84-0.txt e_book.txt

ls
```
average.py  basic.py  e_book.txt  lab3  tree.py  tree.pyc
```

hdfs dfs -mkdir raw

hdfs dfs -ls
```
Found 2 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:34 raw
```

hdfs dfs -put e_book.txt raw/

hdfs dfs -ls -R
```
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current/user
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:35 .Trash/Current/user/wiem.chouchane
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-12-01 11:56 .Trash/Current/user/wiem.chouchane/.sparkStaging
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:03 .Trash/Current/user/wiem.chouchane/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:14 .Trash/Current/user/wiem.chouchane/bonjour.txt1644826712962
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/output
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:26 .Trash/Current/user/wiem.chouchane/dossier
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 .Trash/Current/user/wiem.chouchane/dossier/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:35 .Trash/Current/user/wiem.chouchane/e_book.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane      16680 2021-11-30 09:44 .Trash/Current/user/wiem.chouchane/trees.csv
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane        384 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount/job.properties
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib
-rw-r--r--   3 wiem.chouchane wiem.chouchane     316498 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib/hadoop-mapreduce-examples-3.2.2.1.0.3.0-223.jar
-rw-r--r--   3 wiem.chouchane wiem.chouchane       1895 2021-11-29 22:25 .Trash/Current/user/wiem.chouchane/wordcount/workflow.xml
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:35 raw
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:35 raw/e_book.txt
```

hdfs dfs -cp raw/e_book.txt e_book_copy.txt

hdfs dfs -ls
```
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:37 e_book_copy.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:35 raw
```

hdfs dfs -mv e_book_copy.txt input.txt

hdfs dfs -ls
```
Found 3 items
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:37 input.txt
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:35 raw
```

hdfs dfs -rm input.txt
```
22/02/14 09:40:25 INFO fs.TrashPolicyDefault: Moved: 'hdfs://efrei/user/wiem.chouchane/input.txt' to trash at: hdfs://efrei/user/wiem.chouchane/.Trash/Current/user/wiem.chouchane/input.txt
```

hdfs dfs -ls -R
```
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:02 .Trash/Current/user
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:40 .Trash/Current/user/wiem.chouchane
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-12-01 11:56 .Trash/Current/user/wiem.chouchane/.sparkStaging
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:03 .Trash/Current/user/wiem.chouchane/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:14 .Trash/Current/user/wiem.chouchane/bonjour.txt1644826712962
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:10 .Trash/Current/user/wiem.chouchane/data/output
drwx------   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:26 .Trash/Current/user/wiem.chouchane/dossier
-rw--w--w-   3 wiem.chouchane wiem.chouchane          8 2022-02-14 09:19 .Trash/Current/user/wiem.chouchane/dossier/bonjour.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:35 .Trash/Current/user/wiem.chouchane/e_book.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:37 .Trash/Current/user/wiem.chouchane/input.txt
-rw-r--r--   3 wiem.chouchane wiem.chouchane      16680 2021-11-30 09:44 .Trash/Current/user/wiem.chouchane/trees.csv
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/input
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-29 22:19 .Trash/Current/user/wiem.chouchane/wordcount/data/output
-rw-r--r--   3 wiem.chouchane wiem.chouchane        384 2021-11-29 22:26 .Trash/Current/user/wiem.chouchane/wordcount/job.properties
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib
-rw-r--r--   3 wiem.chouchane wiem.chouchane     316498 2021-11-17 12:07 .Trash/Current/user/wiem.chouchane/wordcount/lib/hadoop-mapreduce-examples-3.2.2.1.0.3.0-223.jar
-rw-r--r--   3 wiem.chouchane wiem.chouchane       1895 2021-11-29 22:25 .Trash/Current/user/wiem.chouchane/wordcount/workflow.xml
drwxr-xr-x   - wiem.chouchane wiem.chouchane          0 2022-02-14 09:35 raw
-rw-r--r--   3 wiem.chouchane wiem.chouchane     448821 2022-02-14 09:35 raw/e_book.txt
```

hdfs dfs -get raw/e_book.txt local.txt

ls
```
average.py  basic.py  e_book.txt  lab3  local.txt  tree.py  tree.pyc
```