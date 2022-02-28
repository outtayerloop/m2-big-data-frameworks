# Hive course

- **SQL Semantic layer for Hadoop**

- **SQL** : uniforme peu importe BD derrière

- **Datawarehouse system for Hadoop** : metadata info about stored data on HDFS, data can be queried as tables, SQL-like operations using the **HiveQL** language

- **HiveServer2** : process java qui tourne sur un des masters du serveur, émission de requêtes SQL grâce à JDBC et DiveServer2 les transforme en HiveQL. Avec Hive on émet vue SQL. Décide du plan d'exécution

- **Hive metastore** : gestionnaire de données de Hive, stocke nom des tables, etc.

- **LLAP** : Hive analyse en temps réel les requêtes pour optimiser temps de traitement. Il monte dans la RAM du cluster YARN les requêtes les + faite. LLAP utilise le cache, plein de daemons LLAP qui utilisent containers YARN pour mettre en cache données les + utilisées.

- **CBO** : Hive Cost-Based optimization

- **ORC** : format de fichier préféré de Hive 3, **à retenir :** les formats de fichier différents. ORC = format par défaut dans une table managée.

- **SerDe** : sérialisation / dé-sérialisation des données