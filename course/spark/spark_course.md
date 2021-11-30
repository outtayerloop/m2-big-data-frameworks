# Spark course

- Populaire, supporte Python, Java, Scala, R...
- Utile aux traitements distribués
- SQL, streaming (micro-batch quasi temps réel), ML, prototypage sur PC, lancement à l'échelle sur un cluster de serveurs possible
- Data engineer : ne fait pas de ML, fait du SQL, fait de la transfo de données, ETL

## Applications

- Structured streaming : quasi temps réel, on se branche sur un channel et on écoute au fur et à mesure ce qui se passe

- Analyse

- Librairies de calcul : ETL, réseau, etc.

## Contexte Spark

- Construit sur des RDDs : tableaux de lignes (row lists) qui peuvent être divisés en parties aléatoires et peuvent être répartis pour distribuer les calculs

- Dataframes et datasets : dataframe fonctionne avec des RDDs par-dessous, ce qui est bien c'est qu'on peut interroger des dataframes (tableaux SQL) qui peuvent être requêtés avec du SQL, simplifie l'utilisation des dataframes et autres dans Spark, pour manipuler la donnée + facilement

- Big Data : 3V : volume, variété et vélocité

- Tâches analytiques, ETL simple, SQL, temps réel : possible avec Spark

- Stockage : HDFS

- Compute : YARN

- Hive : ??

- Kafka : ??

- Spark : process de données, ETL, streaming, analytique, ML, etc.

- Peut se brancher avec Jupyter Notebook

- Applications faciles à écrire, APIs composables cad qu'on peut utiliser ttes les APIs de Spark pour écrire des applis avancées, on peut écrire ses propres librairies avec Spark => grande flexibilité

- Si on utilise du SQL pour charger des données, on peut utiliser la Spark ML pour combiner et processer ces données chargées en SQL par ex => peu de lignes de code pour bcp d'étapes => puissance de Spark

- But Spark : plate-forme unifiée pour tout faire, ajd on a aussi unifié niveau infra => cloud, etc.

- On limite Spark au moteur de calcul distribué en général => recouvre déjà pas mal de besoins. Distribution des calculs sur le réseau, peut lire depuis HDFS, depuis providers cloud (S3, Azure, Databricks etc.). On peut même faire tourner des jobs Spark direct sur le cloud au lieu d'installer sur la machine Spark, on peut envoyer direct le code sur le cloud (attention à l'utilisation qu'ils font du code envoyé xD)

- Spark streaming : pour faire du quasi temps réel

- Kafka : messaging par ex

- Spark : PAS un outil de stockage donc ne stocke pas sur le long terme, il est un outil de traitement de données comme MapReduce de Hadoop (sauf que MapReduce dispo uniquement en Java)

- HDFS et MapReduce = moteur de calcul dans Apache Hadoop, MapReduce a été fait pour faire calculs sur blocs HDFS direct

- Spark : fonctionnait sur Hadoop à la base mais s'adapte au mieux pour différentes sources de données en optimisant lui-même les lectures => **data locality** : qd on a des blocs sur différents workers, on fait tourner des containers YARN sur les mêmes noeuds qui contiennent les blocs

- Spark ne tourne pas que sur Hadoop !

- Apache Hadoop : données stockées sur HDFS ou Hive, process avec Spark (MapReduce quasi plus du tout utilisé), schedule avec Oozie (ajd remplacé par un autre truc ?)

- Spark : librairies open source avec différents besoins couverts => ~demie-douzaine de librairies => Spark SQL, MLLib, Graphics (BD graph, processing graph, stockage de données sous forme de graphes avec noeuds et lignes, données physiques, gains sur les requêtes mais difficilement distribuable parce que graphes pas trop divisibles)

## Architecture de Spark

- Data scientist prototypent sur le PC, installent les librairies etc mais on va vouloir passer à l'échelle parce que le PC ne peut plus processer toute la donnée, on n'a plus assez de place sur le PC, plus assez de puissance => passage sur le calcul distribué

- Cluster : plusieurs PCs branchés ensemble, Spark utilise ressources cumulées des machines, passage à l'échelle simplifié

- Spark fonctionne en mode standalone, YARN, Mesos

- Spark sait répartir les tâches selon puissance dispo (CPU, RAM), il sait diviser, mais il faut que physiquement les jobs soient exécutés sur machines branchées sur le cluster et Spark fait ça bien mais il a besoin d'aide en termes de distribution => YARN et Mesos interviennent là

- YARN, Mesos : génération du paquet à partir du code et YARN va exécuter et distribuer le travail sur le cluster, on submit l'appli Spark au cluster manager qui s'occupe de distribuer les ressources

- 2 grosses parties dans Spark :
  - Application driver / process driver : gère l'appli Spark,contient la main function, le driver tourne sur l'edge en mode client par ex, va répondre aux entrées des users, analyse et distribue la charge sur les executors, des fois du code est fait dans le driver alors que ça devrait être fait sur le worker etc. Il maintient infos importantes durant cycle de vie de l'appli. Il possède la session Spark et le code utilisateur
  - 1 ou plusieurs executors : exécutent les tâches physiquement sur les machines qui ont été distribuées par le driver, retournent leur statut au driver et donnent en retour le résultat du calcul, ils processent la donné
- Tout ça tourne sous YARN, Mesos ou autre, on a juste à écrire le code et submit l'appli Spark, c'est par la façon dont le code est écrit que le driver va distribuer le code ou pas (attention aux fonctions qui rapatrient le code vers le driver)

- Bare Metal : cluster, on doit nous-même packager l'appli comme en MapReduce (sbt, maven, compiler l'appli puis soumettre au job) => https://www.ibm.com/fr-fr/cloud/bare-metal-servers?utm_content=SRCWW&p1=Search&p4=43700066871174338&p5=p&gclsrc=ds

- Executor : exécute calcul pur sur Spark, si on veut faire du calcul sur un dataset, on va le diviser dans le master (driver) mais chaque morceau du dataset sera distribué sur les executors pour appliquer la fonction de calcul en parallèle sur les executors

- Spark language API : run Spark en différents langages => Scala (1er langage supporté par Spark, Spark écrit en Scala)

- Databricks : facilite les choses, pratique parce que ça permet de prototyper

- Apache Kafka écrit en Scala (l'un des 1ers langages fonctionnels, devient vite illisible mais cool qd même)

- Spark session tourne dans une JVM, process sur les executors dans le langage de prog choisi

- Code Spark transposable d'un langage à un autre parce que les APIs Spark ont été travaillées pour que ce soit facile de passer d'un langage à un autre, assez unifié peu importe le langage

- Spark divisé en 2 APIs:
  - Bas niveau : données non structurées
  - Haut niveau : données structurées

- Spark session : on démarre un Spark Shell (on lance la console Scala ou PySpark) => shell interactif et on va pouvoir écrire du code direct dessus => bien pour prototyper, si on veut soumettre une appli standalone (batch) on utilise spark submit => on met un JAR et il s'occupe du reste

- Process du driver : Spark Session, permet d'exécuter fonctions pré-définies sur le cluster, Spark Session configure si c'est du Spark streaming, si c'est du SQL etc

- Dataframe : tableau dsitribué et structuré à colonnes t à lignes => structure la + utilisée et la + commune, on peut définir colonnes et types grâce au schema => spreadsheet avec colonnes nommées => ressemble aux tableaux en SQL (donner le nom et le type pour chaque colonne du Dataframe). On distribue chaque ensemble de lignes sur un executor

- YARN : master et node manager qui fait tourner containers.

- Executor Spark tourne sur YARN

- Parallélisation possible des calculs sur un même executor, on divise les données par partitions (ensemble de lignes sur lesquels on exécute du code à travers une machine sur le worker).

- **Partition** de dataframe : détermine comment paralléliser, si on n'a qu'1 partition on va avoir un parallélisme de 1 seulement même si on a 1000 executors !

- Généralement on ne manipule pas les partitions, on le fait à travers les RDDs, Spark s'occupe des partitions

- Structures internes de Spark immutables : on ne peut pas modifier les données, on va plutôt les transformer parce qu'on ne peut pas les manipuler, on est capable de revenir à une étape bien précise de transfo grâce à ça

- Pour avoir une sortie en affichage il faut utiliser une **action** au lieu d'une **transformation**

- **Lazy evaluation** : qd l'executor exécute le code, tant qu'il n'y a pas d'action (afficher, écrire/lire dans HDFS/AWS etc) alors il ne se passera rien physiquement en termes de CPU/RAM. Ce n'est pas parce qu'on a écrit du code qu'il va se passer qqe chose, **si on fait full transfo alors il ne se passera RIEN** ! => permet l'optimisation, avec utilisation de prédicats etc (payant sous Databricks)

- 2 types d'opérations dans Spark : **transformation** (evalué mais pas exécuté) et **action** (exécuté physiquement parlant avec CPU/RAM) => permet d'optimiser les différentes tâches

- Spark UI : permet de monitorer les opérations (accessible sous Databricks)

- Spark Session un peu comme Configurator de MapReduce

- C'est YARN qui exécute l'appli Spark




