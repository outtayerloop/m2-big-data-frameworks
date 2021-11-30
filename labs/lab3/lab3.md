**Wiem CHOUCHANE**

**M2 APP SL1**

**Big Data & ML**

&nbsp;

# Lab 3 - Apache Spark

## Tutorial

2.2 We will display the number of lines of the ```trees.csv``` file with the following Python script :

```python
#!/ usr/bin/env python
from pyspark import SparkConf , SparkContext
appName = "numberOfTrees"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)
# Open the file
file = sc.textFile("hdfs://efrei/user/wiem.chouchane/trees.csv")
# Display the number of lines
number = file.count()
print("Number of lines : ", number - 1)
```

To run this script, we will use the PySpark console while manually typing the code lines to run. For this we will first open the PySpark console :

```shell
pyspark
```

Output :

```
Python 2.7.5 (default, Nov 16 2020, 22:23:17)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
21/11/30 11:20:04 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4440. Attempting port 4441.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4441. Attempting port 4442.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4442. Attempting port 4443.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4443. Attempting port 4444.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4444. Attempting port 4445.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI' could not bind on port 4041. Attempting port 4042.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI' could not bind on port 4042. Attempting port 4043.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI' could not bind on port 4043. Attempting port 4044.
21/11/30 11:20:04 WARN Utils: Service 'SparkUI' could not bind on port 4044. Attempting port 4045.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.4.7.1.0.3.0-223
      /_/

Using Python version 2.7.5 (default, Nov 16 2020 22:23:17)
SparkSession available as 'spark'.
>>>

```

Then we will copy each code line from our python script above and run them individually. When launching the PySpark console, the sc variable already seems initialized so we will first type the following instruction to stop the current Spark session to replace it by our new one :

```python
sc.stop()
```

Then we will be able to run each code line one by one in the console.

Output :

```
>>> sc.stop()
>>> from pyspark import SparkConf , SparkContext
>>> appName = "numberOfTrees"
>>> conf = SparkConf().setAppName(appName)
>>> sc = SparkContext(conf=conf)
21/11/30 11:27:01 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4440. Attempting port 4441.
21/11/30 11:27:01 WARN Utils: Service 'SparkUI (HTTPS)' could not bind on port 4441. Attempting port 4442.
21/11/30 11:27:01 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
21/11/30 11:27:01 WARN Utils: Service 'SparkUI' could not bind on port 4041. Attempting port 4042.
>>> file = sc.textFile("hdfs://efrei/user/wiem.chouchane/trees.csv")
>>> number = file.count()
>>> print("Number of lines : ", number - 1)
('Number of lines : ', 97)
>>>
```

Here we added a - 1 at the end of the line count because we did not want to take into account the first row which contains the column titles.

To exit the PySpark console, simply type :

```python
exit()
```

As the next steps will require more scripts we will not use the PySpark shell anymore. Also, as said in class, the spark-submit command does not work with the current cluster's configuration (it has issues with Spark context initialization) so we will do everything on Databricks for the next questions

2.3 







