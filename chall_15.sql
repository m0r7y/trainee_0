/*
PostgreSQL : SQL : « ORM can not beat me »

Et oui, postgreSQL est la base de données utiliser par Odoo. 
Ne vous étonnez pas, même si l’ORM de Odoo est magique, 
il y aura des parties de vos codes qui utilisera des requêtes SQL.

Donner les requêtes SQL pour créer la table « your_first_model » dont les champs sont les suivants :
- id de type numérique (clé primaire, auto-incrément)
- firstname de type string
- is_major de type booléen
- age de type numérique
- heigh de type float
- city_id de type numérique (clé étrangère)

Créer la table city dont les champs sont les suivants :
- id de type numérique (clé primaire, auto-incrément)
- city_name de type string

Relier la table your_first_model et city par une contraite de foreign key

Donnez l’instruction SQL pour avoir afficher : 
- nombre_de_personne et le nom de la ville
# OUTPUT
21 ‘asgard’ ;
13 ‘bisounours’ ;

*/
