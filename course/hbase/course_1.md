# Big Data Frameworks - Apache HBase (HDFS - Hadoop File System)

## Rappels composants HDFS

- **Langage principal Hadoop** : Java

- **3 V du Big Data** : volumétrie, variété, vélocité

- **Open Source** : pour enrichir les composants par la commu

- **HDFS** : clusters (grappes de serveurs connectés les uns avec les autres), on va installer sur chacun des serveurs une partie du composant => HDFS. HDFS = partie stockage distribué. Ex : fichiers volumineux stockés de façon pérenne, fichiers divisés en blocs et distribués sur un ensemble de noeuds par HDFS (**data nodes**). Sécurisé car on ne perd pas les données, les blocs sont répliqués 3 fois au minimum, on peut perdre jusqu'à 2 noeds max donc donnée tjrs dispo => tolérance à la panne. Si on perd un noeud ou un rack on ne perd pas la donnée.

- **HDFS HA (high availability)** : 2 machines name node dans une archi de prod comme ça si on perd un name node alors reprise d'activité. Si on perd les 2 name nodes (panne réseau par ex) ils ne sont pas perdus physiquement (ils n'ont pas brûlé), on peut les récup, on fait des sauvegardes des file systems (données essentielles niveau OS) des name nodes (volumes de données usqu'au peta octet), facilité d'export

- **Name node** : master daemon, meta-données, annuaire (infos de distribution des fichiers). Page d'administration avec infos du name node (ex : cluster de l'EFREI) => noms des machines, capacité totale et utilisée, nb data nodes, vue des data nodes, nb de blocs par data node (en théorie même nb de blocs par data node), adresse des data nodes, état du cluster HDFS de façon générale et état de fonctionnement. Si 2 name nodes et 1 tombe en panne, alors le 2eme passe de stand by à actif. Stocke info, blocs de données, répartition dans les data nodes.

- **Data node** : slave daemon, contient données

- **Journal node** : propose haute disponibilité (HA) des name nodes pour qu'ils fonctionnent de façon synchronisée car on a besoin de bcp de réactivité en cas de dysfonctionnement d'un des name nodes, en terme de détection de panne de name node et de synchro des opérations, le name node passif sait où en est le name node actif

- **ZKFC (Zoo Keeper Failover Controller)** : détecte si un name node est down

- Couches les plus importantes de Hadoop : cluster **HDFS** (stockage, contient name node / secondary name node qui sont 2 daemons) et cluster **YARN**

- **Cluster YARN** : alloue et orchestre ressources dans cluster Hadoop aux différentes applis. 2 daemon principaux :
  - **Resource manager** : master daemon => alloue CPU et RAM sur chaque node manager, gère l'ensemble des node managers
  - **Node manager** : slave daemon, gère ressource sur seulement ce noeud-là

## Apache HBase

- Pas comme HDFS car c'est un autre composant Hadoop

- Utilisé par Facebook

- **Stockage efficace de données volumineuses** : lecture / écriture données rapidement malgré volume

- **Stockage colonne clé/valeur orienté document** : "objet json" / "dictionnaire de données" (pas physiquement). Chaque doc est identifié de façon unique par une clé. Chaque document a des "propriétés" et chaque propriété aura la clé associée à son document (donc plusieurs propriétés peuvent avoir la même clé si elles appartiennent au même document)

- **Accessibilité rapide**

- **Fonctionnement à la façon d'une BD** : stockage sous forme de ligne mais pas de SGBD/table physique.

- **Séparation en régions** : nb contigu (clé successives) de tuples (documents). Ex : clés 7000 à 8000 sur une région, 9000 à 10 000 sur une autre région. Document / table sur une seule région à la base et plus on fait grossir la table et plus la région grossit et se divise en d'autres régions pour garder la même efficacité.

- **Region server** : stocke la donnée brute, distribution au sein du cluster, 1 region server par machine. Sert plusieurs régions, peut stocker plusieurs régions / tables, et toutes ces régions sont stockées par HDFS. HBase ré-alloue les régions à des region servers. Des machines contiennnent les region servers.

- **Différence avec HDFS** : dans HDFS on divise les fichiers en blocs et on les répartit. Dans HBase on répartit les données direct et c'est le fonctionnement du region server qui fait l'efficacité de HBase. Dans HBase ça fonctionne avec la RAM, il y a un syst de cache qui permet lect/écrit rapide pour le client, le region server fonctionne par region (RAM allouée/dédiée), le fait d'avoir plsrs régions augmente l'efficacité car qd on augmente le nb de données, on attribue + de régions avec autant de RAM donc on ne perd pas en perfs. Si on ajoute trop de données on aura une région de + et comme elle a les mêmes ressources qu'une autre région on perd pas en perfs.

- **Pre-split niveau HBase** : on dit dés le départ cb de régions on a sur la table et la répartition sur les region servers. Tout ça dépend de comment on interroge la donnée. On peut déterminer le nb de regions optimal. Ex : si les clé commencent par la 1ère lettre de l'alphabet alors 26 régions car 26 lettres si on suppose qu'on a la même qté de données dans chaque région (répartition équitable). On veut éviter que des régions travaillent plus que d'autres. Qd on sait pas comment répartir les données entre régions on ne fait pas de pre-split on laisse juste HBase le faire automatiquement.

- **Stockage de la donnée HBase dans HDFS** : dans un répertoire dédié de HDFS. On ne perd jms la donnée HBase si on ne perd pas la donnée HDFS. Si le region server tombe, mécanisme de **WAL (Write Ahead Lock)** cad log avant d'écrire, lorsqu'on fait une opération sur HBase, il stocke l'opération faite dans HDFS puis la rend effective dans les region servers, donc si jms un region server tombe, toutes les opérations seront effectuées sur une autre région nouvellement effectuée grâce aux **HFiles**. Dans HBase on ne fait que de l'écriture, une update est une nouvelle écriture avec un update de timestamp => gagne en efficacité. Suppression de ligne = écriture dans HBase avec marqueur de suppression. On fait la ré-organisation des fichiers**HFiles** la nuit car ça prend bcp de temps.

- **Stockage par ordre alphabétique de clé dans HBase** : construction des clés en fonction de la donnée.

- **Colonne Hbase** : c'est une **ligne** dans l'ex du cours. Appartiennent à des **column family**.

- **Pas de schema d'avance dans Hbase** : répartition de la données dans des documents clé/valeur, on aura des **column family** (familles de colonnes => famille de lignes), on devra spécifier juste ça à la création de la table (mais pas les colonnes elles-mêmes). Dans clé on peut mettre par ex : email client. On aura par ex une column family adresse de facturation et une autre pour les transactions, on pourra ajouter colonnes pour l'adresse de facturation en fonction de l'adresse (USA, France) car Hbase accepte le fait qu'on puisse ajouter colonnes au fur et à mesure.

- **Formats de stockage des valeurs Hbase** : texte, binaire, PDF. Chaque colonne (ligne) **entre 0 et 10 Mo** donc **PAS DE STOCKAGE VIDEO DANS HBASE** (trop volumineux).

- **Requêtes HBase** : sur la clé uniquement, c'est pour ça que HBase est rapide car filtre niveau clé rangées par ordre alphabétique, et par région. On split les lignes dans la région jusqu'à obtenir la bonne ligne => **re-filter**. Interrogation sur l'accès et non pas sur la valeur, on aura la clé puis la valeur correspondante => **différent de SQL / BD classique** car l'interrogation se fait sur la clé et non pas la valeur. Il existe des requêtes complexes ("JOIN") mais pas bonne archi HBase (pb archi, HBAse pas pertinent pour ce use case).

- **Choix HBase dans archi** : en fonction du requêtage de données car organisation clé importante. Coûte cher en termes d'admin et de conception (archi complexe), coûte cher en termes de performances (bcp de machines nécess). Dépend des besoins, accès à la milliseconde dans HBase.

- **Comme un dictionnaire** : ensemble de docs clé/valeur trié par clé. Une famille = un ensemble de clé/valeur. Classé aussi selon nom des colonnes. Valeur = document (contient un ensemble de **column family** qui contient ensemble de colonnes avec pour chaque colonne une valeur).

- **Qualifier** : colonne

- **Cellule** : valeur de la colonne + timestamp.

- **Timestamp** : versioning des lignes. Update/suppression = écriture d'une nouvelle ligne avec nouveau timestamp et nvx marqueurs => versioning de la donnée dans HBase.

- **Column family** : un ensemble de column families constitue un **document**. on peut mettre des **column filters** pour requêter sur une colonne. Par contre si on veut par ex tous les livres qui ont été vendus à 10 euros alors filtre sur la valeur et pas sur la clé donc HBase pas efficace du tout (car il indexe par clé). On va sur 1 ou 2 column family max dans une table HBase sinon perte en efficacité !

- **Normalisation HBase** : réplication de la donnée à l'avance car on s'interroge sur la façon dont la donnée est interrogée.

- **Standardisation des diagrammes** : redondance des données

- **Clé HBase** : byte array (par ex pour Java)

- **Classement des tuples** : ordre alphabétique des clés. On a donc pas l'ordre d'arrivée des tuples par ex. On indexe donc plutôt par nom de domaine pour retrouver + vite la donnée.

- **Tuple HBase** : ensemble de propriétés (ex : colonne et valeur). Le tuple HBase est l'ensemble des column families avec leurs valeurs.

- **Eviter hotspotting** : toutes les régions doivent fonctionner de la même manière => contiennent même nb de données. Répartition données dans les régions dépend directement de la clé donc bien choisir les clés des documents, il faut éviter les régions inégales.

- **Outils HBase** : Hbase shell, Hbase API (Java), Python API (HappyBase), page web dynamique qui affiche infos (voir screens de page d'admin HBase)

- **HBase master**

- **Hbase slave**

- **Disable table** : désactivation table, car comme les tables sont réparties sur les régions, on n'a pas de garantie que qd on suppr une table il n'y ait pas encore d'opération dessus

- **Ligne** : composée de différentes colonnes. Insertion de clé/valeur colonne par colonne, on indique la column family et la table

- **Table** : ensemble de régions et de lignes. Peuvent être réparties en namespaces. Si on utilise namespace, il faut préfixer nom de la table par le namespace dans les requêtes HBase

-**Données HBase** : récupérées sous forme de bytes au départ (à convertir au format souhaité : string, double, etc.). Des fois il faudra utiliser des offsets pour découper la sortie de données en ce qui nous intéresse uniquement

- **Scan** : efficace que si on délimite la qté de données (début/fin) sinon trop consommateur

- **Etats regions** : ouverte, fermée, etc. On a jamais un état exact sur toutes les régions de la même manière, le HBase Master gère chaque région pour que les opérations sur chaque région soit équivalente mais 1 lifecycle par région car par ex certaines régions ont besoin d'être splittées, compressées, etc. 









