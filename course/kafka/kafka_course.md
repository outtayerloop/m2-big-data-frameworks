# Kafka course

- **Yarn** : computing / scheduling Big data => CPU/RAM, composant Hadoop, pour gérer les différents noeuds sous forme de CPU/RAM qui existent sous forme d'archi distribuée sur cluster Hadoop, on a un serveur YARN. Un client demande de scheduler un traitement, et le resource manager prend les requêtes et les distribue sur des noeuds qui travaillent conjointement. C'est un scheduler de ressources car il permet de gérer les tâches exécutées sur noeuds. Par ex si on a un job Spark avec algo de tri random forest, on peut faire tourner Spark dans YARN qui va prendre le code et l'envoyer sur les noeuds. Le driver Spark pourra paralléliser les traitements sur les différents noeuds. YARN est comme un taxi, c'est la partie synchroniseur de ressources/resources scheduling

- **Map/Reduce et Spark** : traitement distribué sur cluster Hadoop et autre (Spark)

- **Hive** : vue / BD relationnelle pour requêter données sous Hadoop avec HDFS et Yarn

- **Oozie** : schedule / organise des workflows d'actions Apache Hadoop

- **Kafka** : système de messaging Big Data.

- **Donnée** : stockée puis analysée soit pour santé infra soit business, logs de sécurité, mais aussi logs business (chaque action d'un client potentiel ou non est trackée).

- **Publish/subscribe (Pub/sub)** : pattern de messaging caractérisé par un **sender** qui envoie à un **publisher** une info, le **receiver** se branche et va recevoir l'info par la suite. Garantit l'ordre d'arrivée des messages.

- **Apache Avro** : format de données utilisé par Kafka (pas XML, pas JSON)

- **Message** : plus petite unité de Kafka, consommés dans l'ordre chronologique.

- **Topics** : comme JMS, ou dossier dans file system, parce que plusrs consommateurs et plusieurs publishers. Peut $etre divisé en partitions.

- **Partitions** : organisation physique des messages à l'intérieur d'un même topic sur les différents serveurs pour leur répartition.

- **Advanced Kafka clients** : **producers/publishers/writers** et **consumers**. Les **producers** écrivent des messages dans Kafka. Qd on écrit un message ds Kafka on doit obligatoirement préciser le topic mais en général on ne choisit pas la partition, il y a un **partitioner** (répartitionneur) qui le fait lui-même. Les **consumers** lisent les messages et savent où ils en étaient pour pouvoir reprendre grâce notamment à l'**offset**. On a la garantie que les messages sont consommés dans l'ordre.

- **Kafka Broker** : serveur Kafka, il reçoit les messages des producers, il les commit sur le fs local (pas HDFS, c'est un fs propre à Kafka en local sur les machines). Ils sont designés pour marcher sous système distribué, min 3 noeuds ds un cluster Kafka, tjrs nb impair.

- **Rétention** : cb de tps les messages écrits sont gardés (7 jours par défaut). On peut rejouer en cas de panne. Avec Kafka on fait du temps réel / streaming / micro-batching.

- **Producer** : se connecte à Kafka en utilisant du binaire et écrit un message (que ce soit un programme ou un utilisateur).

- **ProducerRecord** : objet qui représente le message, il contient key, message (value), topic, partition (choisie par Kafka).

- **Serializer** : pour key, value (message)

- **Fire-and-forget** : le sender envoie sans savoir si ça a été reçu

- **Synchronous send** : le sender attend que le message ait bien été reçu, bloque tant que le message n'a pas été reçu

- **Asynchronous send** : on a une callback qui nous dit qd le message a été reçu donc on peut faire autre chose en attendant (pas bloqué comme synchronous)