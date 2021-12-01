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

By submitting a job, we would use the following command (if the Python script was named ```basic.py```) :

```shell
spark-submit --master=yarn --py-files basic.py basic.py
```

Simplified output :
```
21/12/01 11:49:29 INFO storage.BlockManagerInfo: Added broadcast_1_piece0 in memory on hadoop-worker03.efrei.online:39477 (size: 4.7 KB, free: 366.3 MB)
21/12/01 11:49:29 INFO storage.BlockManagerInfo: Added broadcast_1_piece0 in memory on hadoop-worker02.efrei.online:36796 (size: 4.7 KB, free: 366.3 MB)
21/12/01 11:49:30 INFO storage.BlockManagerInfo: Added broadcast_0_piece0 in memory on hadoop-worker03.efrei.online:39477 (size: 34.6 KB, free: 366.3 MB)
21/12/01 11:49:30 INFO storage.BlockManagerInfo: Added broadcast_0_piece0 in memory on hadoop-worker02.efrei.online:36796 (size: 34.6 KB, free: 366.3 MB)
21/12/01 11:49:31 INFO scheduler.TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 1961 ms on hadoop-worker03.efrei.online (executor 1) (1/2)
21/12/01 11:49:31 INFO python.PythonAccumulatorV2: Connected to AccumulatorServer at host: 127.0.0.1 port: 58662
21/12/01 11:49:31 INFO scheduler.TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 2117 ms on hadoop-worker02.efrei.online (executor 2) (2/2)
21/12/01 11:49:31 INFO cluster.YarnScheduler: Removed TaskSet 0.0, whose tasks have all completed, from pool
21/12/01 11:49:31 INFO scheduler.DAGScheduler: ResultStage 0 (count at /home/wiem.chouchane/basic.py:8) finished in 2.170 s
21/12/01 11:49:31 INFO scheduler.DAGScheduler: Job 0 finished: count at /home/wiem.chouchane/basic.py:8, took 2.247753 s
('Number of lines : ', 97)
```

2.3 We will first create the Tree class :

```python
class Tree(object):

    def __init__(self, line):
        self.fields = line.split(';')

    def __str__(self):
        return 'Tree[%s]' % ', '.join(self.fields)

    def get_height(self):
        if self.fields[6] is not None and self.fields[6] != '':
            return float(self.fields[6])
        else:
            return None
        
    def get_kind(self):
        if self.fields[3] is not None and self.fields[3] != '':
            return self.fields[3]
        else:
            return None
        
    def get_name(self):
        if self.fields[9] is not None and self.fields[9] != '':
            return self.fields[9]
        else:
            return None
        
    def get_year(self):
        if self.fields[5] is not None and self.fields[5] != '':
            return int(self.fields[5])
        else:
            return None
        
    def get_district(self):
        if self.fields[1] is not None and self.fields[1] != '':
            return self.fields[1]
        else:
            return None
```

We will first use the ```reduce()``` function to compute the average height of trees :

```python
# with reduce()
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_height() is not None)
tree_heights_sum = trees.map(lambda tree: tree.get_height()).reduce(lambda total, height: total + height)
average_tree_height = tree_heights_sum / trees.count()
average_tree_height
```

Output :
```
Out[110]: 22.3125
```

With spark-submit, we would create a file named ```tree.py``` where we would put our class Tree and another file ```average.py``` with the following content :

```python
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
```

And then we would submit our job with the following command :

```shell
spark-submit --master=yarn --py-files average.py,tree.py average.py
```

Simplified output :
```
21/12/01 11:56:20 INFO storage.BlockManagerInfo: Added broadcast_3_piece0 in memory on hadoop-worker02.efrei.online:37284 (size: 5.6 KB, free: 366.3 MB)
21/12/01 11:56:20 INFO storage.BlockManagerInfo: Added broadcast_3_piece0 in memory on hadoop-worker01.efrei.online:43612 (size: 5.6 KB, free: 366.3 MB)
21/12/01 11:56:20 INFO scheduler.TaskSetManager: Finished task 0.0 in stage 2.0 (TID 3) in 96 ms on hadoop-worker02.efrei.online (executor 2) (1/2)
21/12/01 11:56:20 INFO scheduler.TaskSetManager: Finished task 1.0 in stage 2.0 (TID 4) in 144 ms on hadoop-worker01.efrei.online (executor 1) (2/2)
21/12/01 11:56:20 INFO cluster.YarnScheduler: Removed TaskSet 2.0, whose tasks have all completed, from pool
21/12/01 11:56:20 INFO scheduler.DAGScheduler: ResultStage 2 (count at /home/wiem.chouchane/average.py:13) finished in 0.150 s
21/12/01 11:56:20 INFO scheduler.DAGScheduler: Job 2 finished: count at /home/wiem.chouchane/average.py:13, took 0.153032 s
22.3125
```

(The mean is printed in the last line).

The output is the same for the next 2 versions so it will not be included.

Next we will use the ```sum()``` function to do the same thing :

```python
# with sum()
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_height() is not None)
tree_heights_sum = trees.map(lambda tree: tree.get_height()).sum()
average_tree_height = tree_heights_sum / trees.count()
average_tree_height
```

Finally, with the ```mean()``` function :

```python
# variant with mean()
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_height() is not None)
tree_heights = trees.map(lambda tree: tree.get_height())
average_tree_height = tree_heights.mean()
average_tree_height
```

2.4 We will create a series of queries.

```python
# displays the list of districts containing trees
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_district() is not None)
trees_count_per_district = trees.map(lambda tree: (tree.get_district(), 1)).reduceByKey(lambda res, occ: res + occ)
trees_count_per_district.filter(lambda district_tuple: district_tuple[1] > 0).collect()
```

Output :
```
Out[134]: [('8', 5),
 ('9', 1),
 ('12', 29),
 ('14', 3),
 ('16', 36),
 ('19', 6),
 ('20', 3),
 ('4', 1),
 ('17', 1),
 ('7', 3),
 ('15', 1),
 ('5', 2),
 ('13', 2),
 ('11', 1),
 ('18', 1),
 ('3', 1),
 ('6', 1)]
```

```python
# displays the list of different species trees
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_kind() is not None)
distinct_tree_species = trees.map(lambda tree: tree.get_kind()).distinct().sortBy(lambda kind: kind, ascending=True)
distinct_tree_species.collect()
```

Output :
```Out[137]: ['araucana',
 'atlantica',
 'australis',
 'baccata',
 'bignonioides',
 'biloba',
 'bungeana',
 'cappadocicum',
 'carpinifolia',
 'colurna',
 'coulteri',
 'decurrens',
 'dioicus',
 'distichum',
 'excelsior',
 'fraxinifolia',
 'giganteum',
 'giraldii',
 'glutinosa',
 'grandiflora',
 'hippocastanum',
 'ilex',
 'involucrata',
 'japonicum',
 'kaki',
 'libanii',
 'monspessulanum',
 'nigra',
 'nigra laricio',
 'opalus',
 'orientalis',
 'papyrifera',
 'petraea',
 'pomifera',
 'pseudoacacia',
 'sempervirens',
 'serrata',
 'stenoptera',
 'suber',
 'sylvatica',
 'tomentosa',
 'tulipifera',
 'ulmoides',
 'virginiana',
 'x acerifolia']
```

```python
# the number of trees of each kind
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_kind() is not None)
trees_by_kind_count = trees.map(lambda tree: (tree.get_kind(), 1)).reduceByKey(lambda res, occ: res + occ).sortBy(lambda tree_tuple: tree_tuple[0], ascending=True)
trees_by_kind_count.collect()
```

Output :
```
Out[139]: [('araucana', 1),
 ('atlantica', 2),
 ('australis', 1),
 ('baccata', 2),
 ('bignonioides', 1),
 ('biloba', 5),
 ('bungeana', 1),
 ('cappadocicum', 1),
 ('carpinifolia', 4),
 ('colurna', 3),
 ('coulteri', 1),
 ('decurrens', 1),
 ('dioicus', 1),
 ('distichum', 3),
 ('excelsior', 1),
 ('fraxinifolia', 2),
 ('giganteum', 5),
 ('giraldii', 1),
 ('glutinosa', 1),
 ('grandiflora', 1),
 ('hippocastanum', 3),
 ('ilex', 1),
 ('involucrata', 1),
 ('japonicum', 1),
 ('kaki', 2),
 ('libanii', 2),
 ('monspessulanum', 1),
 ('nigra', 3),
 ('nigra laricio', 1),
 ('opalus', 1),
 ('orientalis', 8),
 ('papyrifera', 1),
 ('petraea', 2),
 ('pomifera', 1),
 ('pseudoacacia', 1),
 ('sempervirens', 1),
 ('serrata', 1),
 ('stenoptera', 1),
 ('suber', 1),
 ('sylvatica', 8),
 ('tomentosa', 2),
 ('tulipifera', 2),
 ('ulmoides', 1),
 ('virginiana', 2),
 ('x acerifolia', 11)]
```

```python
# calculates the height of the tallest tree of each kind
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_kind() is not None and tree.get_height() is not None)
tallest_heights_by_kind = trees.map(lambda tree: (tree.get_kind(), tree.get_height())).reduceByKey(lambda res, height: max(res, height)).sortBy(lambda tree_tuple: tree_tuple[0], ascending=True)
tallest_heights_by_kind.collect()
```

Output :
```
Out[140]: [('araucana', 9.0),
 ('atlantica', 25.0),
 ('australis', 16.0),
 ('baccata', 13.0),
 ('bignonioides', 15.0),
 ('biloba', 33.0),
 ('bungeana', 10.0),
 ('cappadocicum', 16.0),
 ('carpinifolia', 30.0),
 ('colurna', 20.0),
 ('coulteri', 14.0),
 ('decurrens', 20.0),
 ('dioicus', 10.0),
 ('distichum', 35.0),
 ('excelsior', 30.0),
 ('fraxinifolia', 27.0),
 ('giganteum', 35.0),
 ('giraldii', 35.0),
 ('glutinosa', 16.0),
 ('grandiflora', 12.0),
 ('hippocastanum', 30.0),
 ('ilex', 15.0),
 ('involucrata', 12.0),
 ('japonicum', 10.0),
 ('kaki', 14.0),
 ('libanii', 30.0),
 ('monspessulanum', 12.0),
 ('nigra', 30.0),
 ('nigra laricio', 30.0),
 ('opalus', 15.0),
 ('orientalis', 34.0),
 ('papyrifera', 12.0),
 ('petraea', 31.0),
 ('pomifera', 13.0),
 ('pseudoacacia', 11.0),
 ('sempervirens', 30.0),
 ('serrata', 18.0),
 ('stenoptera', 30.0),
 ('suber', 10.0),
 ('sylvatica', 30.0),
 ('tomentosa', 20.0),
 ('tulipifera', 35.0),
 ('ulmoides', 12.0),
 ('virginiana', 14.0),
 ('x acerifolia', 45.0)]
```

```python
# sort the trees height from smallest to largest
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_height() is not None)
asc_sorted_tree_heights = trees.map(lambda tree: (tree.get_height(), tree.get_name())).sortBy(lambda tree_tuple: tree_tuple[0], ascending=True)
asc_sorted_tree_heights.collect()
```

Output :
```
Out[141]: [(2.0, 'Faux de Verzy'),
 (5.0, 'If commun'),
 (6.0, "Cèdre bleu de l'Atlas ple"),
 (9.0, 'Désespoir du singe'),
 (10.0, 'Chicot du Canada'),
 (10.0, 'Hêtre pleureur'),
 (10.0, 'Pin Napoléon'),
 (10.0, 'Sophora du Japon'),
 (10.0, 'Chêne liège'),
 (11.0, 'Robinier faux-acacia'),
 (12.0, 'Kaki'),
 (12.0, 'Arbre à gutta-percha'),
 (12.0, 'Erable de Montpellier'),
 (12.0, 'Murier à papier'),
 (12.0, 'Arbre aux pochettes'),
 (12.0, 'Plaqueminier de Virginie'),
 (12.0, 'Faux orme de Sibérie'),
 (12.0, 'Magnolia à grandes fleurs'),
 (13.0, 'Oranger des Osages'),
 (13.0, 'If commun'),
 (14.0, 'Kaki'),
 (14.0, 'Plaqueminier de Virginie'),
 (14.0, 'Pin aux grands cônes'),
 (15.0, 'Chêne vert'),
 (15.0, 'Orme champêtre'),
 (15.0, 'Hêtre pleureur'),
 (15.0, 'Catalpa commun'),
 (15.0, "Erable d'Italie"),
 (16.0, 'Micocoulier de Provence'),
 (16.0, 'Aulne glutineux'),
 (16.0, 'Erable de Cappadoce'),
 (16.0, 'Faux orme de Sibérie'),
 (18.0, 'Zelkova du Japon'),
 (18.0, "Marronnier d'Inde"),
 (18.0, 'Hêtre pourpre'),
 (18.0, 'Arbre aux quarante écus'),
 (20.0, 'Cèdre à encens'),
 (20.0, 'Cyprés chauve'),
 (20.0, 'Séquoia géant'),
 (20.0, 'Noisetier de Byzance'),
 (20.0, 'Tilleul argenté'),
 (20.0, 'Platane commun'),
 (20.0, "Platane d'Orient"),
 (20.0, 'Noisetier de Byzance'),
 (20.0, 'Noisetier de Byzance'),
 (20.0, "Platane d'Orient"),
 (20.0, 'Hêtre pleureur'),
 (20.0, 'Paulownia'),
 (22.0, 'Pérocarya du Caucase'),
 (22.0, 'Arbre aux quarante écus'),
 (22.0, 'Tulipier de Virginie'),
 (22.0, "Marronnier d'Inde"),
 (22.0, "Platane d'Orient"),
 (23.0, 'Hêtre pourpre'),
 (25.0, 'Pin noir'),
 (25.0, 'Platane commun'),
 (25.0, 'Arbre aux quarante écus'),
 (25.0, 'Arbre aux quarante écus'),
 (25.0, "Cèdre bleu de l'Atlas"),
 (25.0, "Platane d'Orient"),
 (26.0, "Platane d'Orient"),
 (27.0, 'Pérocarya du Caucase'),
 (27.0, "Platane d'Orient"),
 (28.0, 'Noyer noir'),
 (30.0, 'Chêne rouvre'),
 (30.0, "Marronnier d'Inde"),
 (30.0, 'Frêne commun'),
 (30.0, 'Séquoia géant'),
 (30.0, 'Pin noir'),
 (30.0, 'Hêtre pourpre'),
 (30.0, 'Séquoia sempervirent'),
 (30.0, 'Séquoia géant'),
 (30.0, 'Pin de Corse'),
 (30.0, 'Cyprés chauve'),
 (30.0, 'Cèdre du Liban'),
 (30.0, 'Cèdre du Liban'),
 (30.0, 'Ptérocarya de Chine'),
 (30.0, 'Hêtre pourpre'),
 (30.0, 'Platane commun'),
 (30.0, 'Faux orme de Sibérie'),
 (30.0, 'Platane commun'),
 (31.0, 'Chêne rouve'),
 (31.0, "Platane d'Orient"),
 (32.0, 'Platane commun'),
 (33.0, 'Arbre aux quarante écus'),
 (34.0, "Platane d'Orient"),
 (35.0, 'Ailanthe'),
 (35.0, 'Cyprés chauve'),
 (35.0, 'Platane commun'),
 (35.0, 'Séquoia géant'),
 (35.0, 'Tulipier de Virginie'),
 (40.0, 'Platane commun'),
 (40.0, 'Platane commun'),
 (40.0, 'Platane commun'),
 (42.0, 'Platane commun'),
 (45.0, 'Platane commun')]
```

```python
# displays the district where the oldest tree is
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_year() is not None and tree.get_district() is not None)
min_year = trees.map(lambda tree: tree.get_year()).min()
oldest_tree_district = trees.filter(lambda tree: tree.get_year() == min_year).map(lambda tree: tree.get_district())
oldest_tree_district.collect()
```

Output :
```
Out[142]: ['5']
```

```python
# displays the district that contains the most trees
trees_csv = sc.textFile('/FileStore/tables/trees.csv')
header = trees_csv.first()
trees = trees_csv.filter(lambda line: line != header).map(lambda line: Tree(line)).filter(lambda tree: tree.get_district() is not None)
trees_count_per_district = trees.map(lambda tree: (tree.get_district(), 1)).reduceByKey(lambda res, occ: res + occ)
trees_count_per_district.max(lambda district_tuple: district_tuple[1])
```

Output :
```
Out[143]: ('16', 36)
```
