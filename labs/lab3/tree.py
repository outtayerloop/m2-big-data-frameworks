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