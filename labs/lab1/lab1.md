**Wiem CHOUCHANE**

**M2 APP LS1**

&nbsp;

# Lab 1 - Hbase

## 1. Hbase CLI

&nbsp;

(Voir doc : https://hbase.apache.org/book.html)

1.1.1 Commandes de base :

- Connexion SSH au cluster Hadoop :

```shell
ssh wiem.chouchane@hadoop-edge01.efrei.online
```

- Initialisation ticket Kerberos :

```shell
kinit wiem.chouchane
```

- Lancement de l'outil shell de HBase :

```shell
hbase shell
```

- Commandes et output :

    - Commande permettant d'afficher les infos sur le cluster HBase :

    ```shell
    status
    ```

    Output :

    ```
    1 active master, 1 backup masters, 3 servers, 0 dead, 22.6667 average load
    Took 0.3812 seconds
    ```

    - Commande permettant d'afficher la version de Hbase utilisée :

    ```shell
    version
    ```

    Output :

    ```
    2.2.4.1.0.3.0-223, rUnknown, Wed Jul 28 00:29:09 CEST 2021
    Took 0.0003 seconds
    ```

    - Commande permettant d'afficher les infos sur l'utilisateur courant :

    ```shell
    whoami
    ```

    Output :

    ```
    wiem.chouchane@EFREI.ONLINE (auth:KERBEROS)
    groups: wiem.chouchane
    Took 0.0155 seconds
    ```

    - Liste des tables du cluster Hbase :

    ```shell
    list
    ```

    Output :

    ```
    TABLE
    ns_dany_sonethavy:mytable
    ns_lucas_bakalian:table_example
    2 row(s)
    Took 0.0593 seconds
    => ["ns_dany_sonethavy:my_table", "ns_lucas_bakalian:table_example"]
    ```

    - Déconexion du HBase shell :

    ```shell
    exit
    ```

    Cette commande permet de se déconnecter du shell hbase et de revenir sur la machine.

1.1.2 Création du namespace

```shell
create_namespace "ns_wiem_chouchane"
```

1.1.3 Création de table

  - Création table :

    ```shell
    create "ns_wiem_chouchane:library" , {NAME => "author", VERSIONS => 2},  {NAME => "book", VERSIONS => 3}
    ```

    Output :

    ```
    Created table ns_wiem_chouchane:library
    Took 1.3087 seconds
    => Hbase::Table - ns_wiem_chouchane:library
    ```

    - Description table :

    ```shell
    describe "ns_wiem_chouchane:library"
    ```

    Output :

    ```
    Table ns_wiem_chouchane:library is ENABLED
    ns_wiem_chouchane:library
    COLUMN FAMILIES DESCRIPTION
    {NAME => 'author', VERSIONS => '2', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => '
    false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false',
    IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'
    }

    {NAME => 'book', VERSIONS => '3', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE => 'fa
    lse', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false', I
    N_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536'}

    2 row(s)

    QUOTAS
    0 row(s)
    Took 0.6151 seconds
    ```

1.1.4 Ajout de valeurs

En output, le temps d'exécution de la commande s'affiche à chaque PUT.

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:lastname", "Hugo"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:firstname", "Victor"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "book:title", "La légende des siècles"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "book:category", "Poemes"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "book:year", "1855"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "book:year", "1877"
```

```shell
put "ns_wiem_chouchane:library", "vhugo", "book:year", "1883"
```

```shell
put "ns_wiem_chouchane:library", "jverne", "author:lastname", "Jules"
```

```shell
put "ns_wiem_chouchane:library", "jverne", "author:firstname", "Verne"
```

```shell
put "ns_wiem_chouchane:library", "jverne", "book:publisher", "Hetzel"
```

```shell
put "ns_wiem_chouchane:library", "jverne", "book:title", "Face au drapeau"
```

```shell
put "ns_wiem_chouchane:library", "jverne", "book:year", "1896"
```

1.1.5 Comptage des tuples de la table library :

```shell
count "ns_wiem_chouchane:library"
```

Output :

```
2 row(s)
Took 0.0128 seconds
=> 2
```

Ici, il n'y a que 2 tuples donc pas besoin de configurer de cache.

1.1.6 Récupération des valeurs

- Récupération des valeurs de toutes les colonnes identifiées par la clé "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo"
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636532933966, value=Victor
 author:lastname                         timestamp=1636532894847, value=Hugo
 book:category                           timestamp=1636532944548, value=Poemes
 book:title                              timestamp=1636532939908, value=La l\xC3\xA9gende des si\xC3\xA8cles
 book:year                               timestamp=1636533078582, value=1883
1 row(s)
Took 0.0176 seconds
```

- Récupération des valeurs des colonnes appartenant à la column family "author" et identifiées par la clé "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo", "author"
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636532933966, value=Victor
 author:lastname                         timestamp=1636532894847, value=Hugo
1 row(s)
Took 0.0089 seconds
```

- Récupération des valeurs de la colonne "firstname" appartenant à la column family "author" et identifiée par la clé "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo", "author:firstname"
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636532933966, value=Victor
1 row(s)
Took 0.0067 seconds
```

- Récupération des valeurs des colonnes appartenant à la column family "book" et identifiées par la clé "jverne" :

```shell
get "ns_wiem_chouchane:library", "jverne", COLUMN => "book"
```

Output :

```
COLUMN                                   CELL
 book:publisher                          timestamp=1636533094047, value=Hetzel
 book:title                              timestamp=1636533099857, value=Face au drapeau
 book:year                               timestamp=1636533106562, value=1896
1 row(s)
Took 0.0274 seconds
```

- Récupération des valeurs des colonnes "title", "year" et "publisher" appartenant à la column family "book" et identifiées par la clé "jverne" :

```shell
get "ns_wiem_chouchane:library", "jverne", COLUMN => ["book:title", "book:year", "book:publisher"]
```

Output :

```
COLUMN                                   CELL
 book:publisher                          timestamp=1636533094047, value=Hetzel
 book:title                              timestamp=1636533099857, value=Face au drapeau
 book:year                               timestamp=1636533106562, value=1896
1 row(s)
Took 0.0100 seconds
```

- Récupération des valeurs correspondant au filtre par valeur appliqué (c'est-à-dire valant ici "Jules") et identifiées par la clé "jverne" :

```shell
get "ns_wiem_chouchane:library", "jverne", FILTER => "ValueFilter(=, 'binary:Jules')"
```

Output :

```
COLUMN                                   CELL
 author:lastname                         timestamp=1636533084251, value=Jules
1 row(s)
Took 0.0147 seconds
```

1.1.7 Navigation dans les tuples :

- Scan de toutes les données de la table "library" :

```shell
scan "ns_wiem_chouchane:library"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 jverne                                  column=author:lastname, timestamp=1636533084251, value=Jules
 jverne                                  column=book:publisher, timestamp=1636533094047, value=Hetzel
 jverne                                  column=book:title, timestamp=1636533099857, value=Face au drapeau
 jverne                                  column=book:year, timestamp=1636533106562, value=1896
 vhugo                                   column=author:firstname, timestamp=1636532933966, value=Victor
 vhugo                                   column=author:lastname, timestamp=1636532894847, value=Hugo
 vhugo                                   column=book:category, timestamp=1636532944548, value=Poemes
 vhugo                                   column=book:title, timestamp=1636532939908, value=La l\xC3\xA9gende des si\xC3\xA8cles
 vhugo                                   column=book:year, timestamp=1636533078582, value=1883
2 row(s)
Took 0.0359 seconds
```

- Scan des données de la column family "book" :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "book"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=book:publisher, timestamp=1636533094047, value=Hetzel
 jverne                                  column=book:title, timestamp=1636533099857, value=Face au drapeau
 jverne                                  column=book:year, timestamp=1636533106562, value=1896
 vhugo                                   column=book:category, timestamp=1636532944548, value=Poemes
 vhugo                                   column=book:title, timestamp=1636532939908, value=La l\xC3\xA9gende des si\xC3\xA8cles
 vhugo                                   column=book:year, timestamp=1636533078582, value=1883
2 row(s)
Took 0.0083 seconds
```

- Scan des données de la colonne "year" appartenant à la column family "book" :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "book:year"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=book:year, timestamp=1636533106562, value=1896
 vhugo                                   column=book:year, timestamp=1636533078582, value=1883
2 row(s)
Took 0.0058 seconds
```

- Scan des données des colonnes appartenant à la column family "author" et identifiées par une clé commençant par une lettre comprise entre a et n (sans filtre) :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "author", STARTROW => "a", STOPROW => "n"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 jverne                                  column=author:lastname, timestamp=1636533084251, value=Jules
1 row(s)
Took 0.0115 seconds
```

- Scan des données des colonnes appartenant à la column family "author" et identifiées par une clé commençant par une lettre comprise entre a et n (avec filtre) :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "author", FILTER => "RowFilter(>=, 'binary:a') AND RowFilter(<=, 'binary:n')"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 jverne                                  column=author:lastname, timestamp=1636533084251, value=Jules
1 row(s)
Took 0.0074 seconds
```

- Scan des données de la colonne "firstname" appartenant à la column family "author" :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "author:firstname"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 vhugo                                   column=author:firstname, timestamp=1636532933966, value=Victor
2 row(s)
Took 0.0119 seconds
```

- Scan des données dont la valeur de "title" correspond à la valeur paramétrée :

```shell
scan "ns_wiem_chouchane:library", COLUMN => "book:title", FILTER => "ValueFilter(=, 'binary:Face au drapeau')"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=book:title, timestamp=1636533099857, value=Face au drapeau
1 row(s)
Took 0.0062 seconds
```

- Scan des données (de version la plus récente) appartenant à la column family "book" dont la valeur de colonne "year" est inférieure ou égale à 1890 :

```shell
scan "ns_wiem_chouchane:library", {COLUMN => "book:year", FILTER => "ValueFilter(<=, 'binary:1890')", VERSIONS => 1}
```

Output :

```
ROW                                      COLUMN+CELL
 vhugo                                   column=book:year, timestamp=1636533078582, value=1883
1 row(s)
Took 0.0079 seconds
```

- Scan des données des colonnes identifiées par une clé commençant par "jv" et correspondant à la regex "[A-Z]([a-z]+){2,}" :

```shell
scan "ns_wiem_chouchane:library", FILTER => "RowFilter(>=, 'binary:jv') AND RowFilter(<, 'binary:jw') AND ValueFilter(=, 'regexstring:[A-Z]([a-z]+){2,}')"
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 jverne                                  column=author:lastname, timestamp=1636533084251, value=Jules
 jverne                                  column=book:publisher, timestamp=1636533094047, value=Hetzel
 jverne                                  column=book:title, timestamp=1636533099857, value=Face au drapeau
1 row(s)
Took 0.0069 seconds
```

1.1.8 Mise à jours de valeurs

- Modification de la valeur de la colonne "lastname" appartenant à la column family "author" et identifiée par "vhugo" en "HAGO" :

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:lastname", "HAGO"
```

- Modification de la valeur de la colonne "lastname" appartenant à la column family "author" et identifiée par "vhugo" en "HUGO" :

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:lastname", "HUGO"
```

- Modification de la valeur de la colonne "firstname" appartenant à la column family "author" et identifiée par "vhugo" en "Victor Marie" :

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:firstname", "Victor Marie"
```

- Modification de la valeur de la colonne "lastname" appartenant à la column family "author" et identifiée par "vhugo" en "Hugo" :

```shell
put "ns_wiem_chouchane:library", "vhugo", "author:lastname", "Hugo"
```

- Récupération des colonnes appartenant à la column family "author" et identifiées par "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo", "author"
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636533784159, value=Victor Marie
 author:lastname                         timestamp=1636533789621, value=Hugo
1 row(s)
Took 0.0221 seconds
```

- Récupération des colonnes appartenant à la column family "author" et identifiées par "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo", COLUMNS => "author"
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636533784159, value=Victor Marie
 author:lastname                         timestamp=1636533789621, value=Hugo
1 row(s)
Took 0.0062 seconds
```

- Récupération des 10 dernières versions des colonnes appartenant à la column family "author" et identifiées par "vhugo" :

```shell
get "ns_wiem_chouchane:library", "vhugo", COLUMNS => "author", VERSIONS => 10
```

Output :

```
COLUMN                                   CELL
 author:firstname                        timestamp=1636533784159, value=Victor Marie
 author:firstname                        timestamp=1636532933966, value=Victor
 author:lastname                         timestamp=1636533789621, value=Hugo
 author:lastname                         timestamp=1636533775184, value=HUGO
1 row(s)
Took 0.0098 seconds
```

1.1.9 Suppression de valeurs / colonnes

Le timestamp de "HUGO" dans le dernier get est 1636533775184.

- Suppression de la valeur author:name=HUGO correspondant au timestamp paramétré :

```shell
deleteall "ns_wiem_chouchane:library", "vhugo", "author:lastname", 1636533775184
```

- Suppression de toutes les valeurs de la colonne "firstname" :

```shell
deleteall "ns_wiem_chouchane:library", "vhugo", "author:firstname"
```

- Suppression de tout le tuple identifié par "vhugo" :

```shell
deleteall "ns_wiem_chouchane:library", "vhugo"
```

- Scan de la version 10 du tuple :

```shell
scan "ns_wiem_chouchane:library", COLUMNS => "author", VERSIONS => 10
```

Output :

```
ROW                                      COLUMN+CELL
 jverne                                  column=author:firstname, timestamp=1636533089190, value=Verne
 jverne                                  column=author:lastname, timestamp=1636533084251, value=Jules
1 row(s)
Took 0.0074 seconds
```

1.1.10 Suppression de table

- Désactivation de la table :

```shell
disable "ns_wiem_chouchane:library"
```

- Suppression de la table :

```shell
drop "ns_wiem_chouchane:library"
```

1.2.1 Insertion d'une table dans Hbase à partir d'un fichier CSV

- Import du fichier CSV dans HBase :

```shell
hdfs dfs -copyFromLocal ~/trees.csv /user/wiem.chouchane/trees.csv
```

- Vérification de la présence du fichier importé dans HBase :

```shell
hdfs dfs -cat /user/wiem.chouchane/trees.csv
```

Output : affiche le contenu du fichier CSV.


- Création de la table "trees" (préfixée du namespace précédent) dans HBase à partir du CSV :

```python
import sys

ROW_KEY_COLUMN_NAME = 'objectid'
TABLE_NAME = 'ns_wiem_chouchane:trees'
GENDER_COLUMN_FAMILY = 'gender'
INFORMATION_COLUMN_FAMILY = 'information'
ADDRESS_COLUMN_FAMILY = 'address'


def main():
    columns = get_all_column_names()
    entry = sys.stdin
    command = get_table_creation_command()
    command = fill_command(command, entry, columns)
    sys.stdout.write(command)


def fill_command(command, entry, columns):
    row_key_column_index = columns.index(ROW_KEY_COLUMN_NAME)
    for line in entry:
        data = line.replace('\n', '').split(';')
        row_key = str(data[row_key_column_index])
        for index, element in enumerate(data):
            if index != row_key_column_index:
                command = add_new_command_line(command, index, row_key, element, columns)
    return command


def get_all_column_names():
    columns = sys.stdin.readline().replace('\n', '').split(';')
    return list(map(lambda column: column.lower(), columns))


def get_table_creation_command():
    return 'create "' + TABLE_NAME + '" , ' \
          '{NAME => "' + GENDER_COLUMN_FAMILY + '", VERSIONS => 10},  ' \
          '{NAME => "' + INFORMATION_COLUMN_FAMILY + '", VERSIONS => 10}, ' \
          '{NAME => "' + ADDRESS_COLUMN_FAMILY + '", VERSIONS => 10};'


def add_new_command_line(command, index, row_key, element, columns):
    meta_data = get_meta_data(index, row_key, columns)
    command += get_new_command_line(meta_data, element)
    return command


def get_meta_data(index, row_key, columns):
    return {
        'row_key': row_key,
        'column_family': get_column_family(index),
        'column': get_column(index, columns)
    }


def get_new_command_line(meta_data, element):
    return 'put "' + \
           TABLE_NAME + '", "' + \
           meta_data['row_key'] + '", "' + \
           meta_data['column_family'] + ':' + \
           meta_data['column'] + '", "' + \
           element + '";'


def get_column_family(index):
    if is_gender_column_family_index(index):
        return GENDER_COLUMN_FAMILY
    elif is_information_column_family_index(index):
        return INFORMATION_COLUMN_FAMILY
    else:
        return ADDRESS_COLUMN_FAMILY


def is_gender_column_family_index(index):
    return 2 <= index <= 4 \
           or 9 <= index <= 10


def is_information_column_family_index(index):
    return 5 <= index <= 7


def get_column(index, columns):
    return columns[index]


if __name__ == "__main__":
    main()
```

- Lancement de la commande de création de la table :

```shell
hdfs dfs -cat /user/wiem.chouchane/trees.csv | python app.py | hbase shell
```

- Description de la table créée :

```shell
describe "ns_wiem_chouchane:trees"
```

Output :

```
Table ns_wiem_chouchane:trees is ENABLED
ns_wiem_chouchane:trees
COLUMN FAMILIES DESCRIPTION
{NAME => 'address', VERSIONS => '10', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE =>
 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false
', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '6553
6'}

{NAME => 'gender', VERSIONS => '10', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRITE =>
'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'false'
, IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '65536
'}

{NAME => 'information', VERSIONS => '10', EVICT_BLOCKS_ON_CLOSE => 'false', NEW_VERSION_BEHAVIOR => 'false', KEEP_DELETED_CELLS => 'FALSE', CACHE_DATA_ON_WRIT
E => 'false', DATA_BLOCK_ENCODING => 'NONE', TTL => 'FOREVER', MIN_VERSIONS => '0', REPLICATION_SCOPE => '0', BLOOMFILTER => 'ROW', CACHE_INDEX_ON_WRITE => 'f
alse', IN_MEMORY => 'false', CACHE_BLOOMS_ON_WRITE => 'false', PREFETCH_BLOCKS_ON_OPEN => 'false', COMPRESSION => 'NONE', BLOCKCACHE => 'true', BLOCKSIZE => '
65536'}

3 row(s)

QUOTAS
0 row(s)
Took 0.6067 seconds
```

- Comptage des tuples créés :

```shell
count "ns_wiem_chouchane:trees"
```

Output :

```
97 row(s)
Took 0.0649 seconds
=> 97
```

Idem ici, il n'y a pas énormément de tuples donc il n'y a pas besoin de configurer le cache. On a bien 97 tuples correspondant aux 97 lignes insérées depuis le CSV, en effet chacune avait un "OBJECTID" différent qu'on a pu constater dans une exploration préalable (réalisé ici en externe sous Google Colaboratory) :

```python
import pandas as pd

df = pd.read_csv('trees.csv', sep=';')
df.shape
```

Output :

```
(97,13)
```

```python
len(df['OBJECTID].unique())
```

Output :

```
97
```

- Pour l'exemple, récupération des valeurs de toutes les colonnes identifiées par la clé "6" :

```shell
get "ns_wiem_chouchane:trees", "6"
```

Output :

```
COLUMN                                   CELL
 address:adresse                         timestamp=1636534121542, value=Quai Branly, avenue de La Motte-Piquet, avenue de la Bourdonnais, avenue de Suffren
 address:arrondissement                  timestamp=1636534121514, value=7
 address:geopoint                        timestamp=1636534121505, value=(48.857140829, 2.29533455314)
 address:nom_ev                          timestamp=1636534121553, value=Parc du Champs de Mars
 gender:espece                           timestamp=1636534121522, value=pomifera
 gender:famille                          timestamp=1636534121526, value=Moraceae
 gender:genre                            timestamp=1636534121518, value=Maclura
 gender:nom commun                       timestamp=1636534121545, value=Oranger des Osages
 gender:variete                          timestamp=1636534121549, value=
 information:annee plantation            timestamp=1636534121530, value=1935
 information:circonference               timestamp=1636534121538, value=
 information:hauteur                     timestamp=1636534121534, value=13.0
1 row(s)
Took 0.0524 seconds
```