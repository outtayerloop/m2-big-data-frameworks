#!/ usr/bin/env python
from pyspark import SparkConf , SparkContext

class Tree(object):

    """
    GEOPOINT;ARRONDISSEMENT;GENRE;
    ESPECE;FAMILLE;ANNEE PLANTATION;HAUTEUR;CIRCONFERENCE;
    ADRESSE;NOM COMMUN;VARIETE;OBJECTID;NOM_EV
    """
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

appName = "avaerageTreeHeight"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)
file = sc.textFile("hdfs://efrei/user/wiem.chouchane/trees.csv")
number = file.

def parseFromJson(lines:Iterator[String]):Iterator[Tweet] = {
    val gson = new Gson
    lines.map(line => gson.fromJson(line, classOf[Tweet]))
}