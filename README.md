Projet API, 

Python comme langage,
Fastapi pour la creation de l'API,
MySQL comme base de données,

Pour connecter à MySQL, je vais utiliser SqlAlchemy,
mais je ferais la conexion en core, sans utiliser orm


Ques'que je besoins pour tester le code? 
- Dans le module 'requirements.txt' on a tout a installer

Où je puis voir la documentation?
- Sur l'API, dans le path on ecris '/docs'


Le module principal c'est 'main.py' je l'ai appart, pour demarrer le server
Je separé les modules en diferents dossiers, pour milleur estructurer le projet (j'ai utilisé une estructure standard):
- config (conexion a la base de donnés)
- models (definition de model/style de tables)
- routers (demandes http)
- crud (les fonctions/métodes) 
- schemas (gerer le tipus de donnés)
