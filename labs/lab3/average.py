from tree import Tree

from pyspark import SparkConf , SparkContext
appName = 'lab3'
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

# with reduce()
trees_csv = sc.textFile('hdfs://efrei/user/wiem.chouchane/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_height() is not None)
tree_heights_sum = trees.map(lambda tree: tree.get_height()).reduce(lambda total, height: total + height)
average_tree_height = tree_heights_sum / trees.count()
print(average_tree_height)