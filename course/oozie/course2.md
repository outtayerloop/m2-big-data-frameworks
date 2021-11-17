# Course 2 - Apache Oozie

- **YARN** : partie compute, contient MapReduce pour le processing

- **Apache Oozie** : outil de scheduling CronTab, permet de planifier des tâches à run, pour des heures et des jours précis et des jobs / processings précis, il faut orchestrer les exécutions => Oozie schedule les actions Hive, MapReduce etc.

- **Utilité** : boîte à outil d'orchestration, pour planifier ttes les actions Hadoop

- **Langage de programmation simple**

- **Troubleshoot possible**

- **Peut supporter de nvx types de jobs**

- **Peut se scaler** : pr supporter plusieurs workflows en même temps

- **Peut être multi-tenant**

- **Multi-stage** : peut commencer par action Hive, puis faire un truc différent comme MapReduce, se synchro sur de nvlles entrées ds Hive, exécuter des scripts de création de table, etc.

- **Workflow** : job qui tourne sur demande sur Oozie => workflow

- **Coordinator job** : tourne de façon régulière, ts les mercredi par ex, s'exécute sur base pré-définie avec séquence pré-définie et démarre workflow sous-jacent qd données sont présentes (selon le DAG). Attention à la reprise des données (incident BDD etc.)

- **Bundle job** : liste de coordinator jobs

- **DAG (Directed Acyclic Graph)** : possibilité de définir avec conditions cmnt actions des workflows vont s'exécuter, selon ordre des noeuds du DAG par ex, ajouter gardes (ex : si script Hive n'a pas marché, envoyer mail, etc.)

- **Daily log workflow possible**

- **MapReduce** : à partir de HDFS

- **Actions Spark possibles** : pas que MapReduce Hadoop

- **Tracking en mémoire** : des données manquantes à l'exécution d'un job, car Oozie ne déclenche les workflows que qd ttes les données sont dispos

- **Différence entre Oozie et script shell** : il faut client lourd et un scheduler à la main pour script shell alors qu'Oozie sait communqiuer avec HDFS, Hive etc. et sait faire du YARN au lieu de taper à la main ttes les commandes, on peut simplement utiliser les APIs Oozie au lieu de scripter au shell, mais possible de faire du shell sous Oozie mais ça reste Oozie qui schedule et s'occupe du flow

- **Format XML** : arborescence et validation avec XSD => permet de rester carré sur Oozie

- **Variables possibles** : .properties => adresse name node, job tracker, workflow app path etc.

- **MapReduce** : input / output directories pour entrées et sorties, il faut d'abord suppr l'output path avant de le re-créer sinon job MR plante dans le workflow. Les données sont stockées dans HDFS, si le dossier en sortie existe déjà pas possible de re-générer données dedans, pour éviter d'écraser données sans faire exprès

- **Application Deployment model** : décrit comment on déploie workflow Oozie pour pvr l'utiliser. Application Oozie (workflow, coordinator ou bundle) => définit un fichier de config, un fichier de description et un ens de JAR / scripts opérationnels. Workflow = fichier XML, job.properties et ens de scripts opérationnels. Config : dans le XML, définit ordre actions. job.properties = ens des variables. Scripts / JAR : pas tt le tps obligatoires car dépend du moment de la soumission du job, si action Java oui obligatoire d'un JAR mais pour MapReduce. Path = path HDFS souvent. Un dossier HDFS contient un workflow et on y met les JARs pour Oozie par ex.

## Architecture Oozie

- **Pas de master / slave** : pas un outil distribué comme YARN, HDFS, on peut cependant en avoir plsrs pour redondance.

- **OozieClient** : client lourd ou HTTP pour communiquer avec Oozie qui communique ensuite avec cluster Hadoop.

- **job.properties** : permet de soumettre un job à Oozie

- **Oozie Server** : applet java, Tomcat, java API possible donc client lourd sinon HTTP

- **Garde les états des différents jobs** : Oozie sait s'ils sont en train de run par ex etc.

- **Purge des jobs** : après période courte

- **Serveur web** : qui récup requête et schedule les workflows au 1er arrivé 1er servi au niveau des requêtes de jobs

- **Mise à l'échelle** : se fait dans YARN direct si on fait un MapReduce, c'est pas Oozie qui fait du scaling lui-même mais on peut indiquer dans job.properties les ressources qui pourront être utilisées pour run les jobs (RAM allouée par ex), mais c'est YARN qui gère le runtime

- **Hadoop DistCP** : copie des trucs de AWS S3

- **Hive** : queries sur données

- **Pipeline** : workflow.xml, on met paramétrage DistCP, on met la sortie, on peut mettre actions Hive pr créer table sur données en entrée et faire reqs pour avoir résultats, si on veut le faire de façon répétitive et quotidienne on fera un coordinator Oozie

- **Action nodes** : dans le XML, actions unitaires d'un workflow chaînées ensemble, c'est ce qui exécute une action java, Spark, MapReduce etc. On peut aussi avoir actions généralistes qui sont pas du Hadoop pr exécuter code arbitraire (ex : entre des actions Hadoop). on peut pas pré-définir à l'avance l'usage que les utilisateurs vont faire

- **Run commande Oozie client** : sur l'edge node => **gateway** (node où on run la commande oozie client). C'est oozie qui appelle les api java pr soumettre les actions. On fait pas hdfs dfs, on fait oozie client submit.

- **Launchers** : permettent de lancer workflow et le scheduler

**job.xml** : config

- **Lancer job MapReduce** : syntaxe

- **Sub-workflow** : embeddeed-workflow (workflow intégré), permet de lancer un workflow enfant depuis workflow parent

- **UDF (User Defined Function)** : fonctions custom possible sur Hive notamment

-**Application path** : dossier HDFS contenant tout ce dont un workflow a besoin

- **Shell Action** : exécute un script .sh

- **Asynchrone** : sont pas run directement, ont besoin du Oozie launcher

- **Synchrone** : exécuté au moment de la lecture de l'action dans le workflow.xml (voir à partir de diapo ~120)

- **Action kill** : permet d'arrêter un job

- **Noeud erreur** : permet de dire ce qu'on fait en cas d'erreur

- **job.properties** : paramétrage des actions. Pas nécessairement dans HDFS, utilisé pour soumettre le workflow. Il est important d'y définir les variables du workflow.xml : {jobType} par ex

- **job.xml** : ??
