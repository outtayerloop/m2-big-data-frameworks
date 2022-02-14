# HDFS Course

- **File System distribué** : blocs physiques, disques durs, flash SSH, etc. Il y a besoin d'une interface entre disque physique et donnée qu'on a (fichier Word, PDF, etc.). Distribué : organise les fichiers et dossiers comme UNIX (arborescence), répartition d'un fichier sur un ensemble d'ordis (big data 3V : volume, vélocité, variété). On découpe chaque fichier et on les répartit. Système de réplication d'HDFS permet de pas perdre d'info en cas de panne.

- **OS** : on organise les données physiquement sur le disque dur / le flash. La donnée brute est stockée sur le système de fichiers, on peut avoir plusieurs formats selon les OS, selon la sécu qu'on veut avoir.

- **Environnement distribué** : dans Hadoop. Ordis / serveurs. Un morceau d'HDFS qui tourne sur un serveur du cluster.

- **HDFS pas fait pour les petits fichiers !** : HDFS divise les fichiers en blocs (64 Mo en général) et les distribue sur des workers. Donc un fichier de 1 Mo prendra un bloc à lui tout seul (gaspillage de bloc)

- **namenode** : contient nom et répartition blocs des fichiers sur les machines, c'est un annuaire

- **HA mode** : (high availability) mode haute disponibilité

- **Réplication** : chaque bloc est répliqué 3 fois

- **Stockage petits fichiers** : hbase par exemple mais pas HDFS