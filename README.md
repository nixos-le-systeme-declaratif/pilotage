# pilotage

API interne de l'équipe de camille — projet compagnon du livre
« NixOS : Le système déclaratif » (Partie VI, chapitre
« Environnements de développement »).

Deux routes FastAPI (`/`, `/sante`) ; la base PostgreSQL `camille`
est celle du chapitre « Les services », atteinte par les variables
d'environnement `PG*` — `psycopg.connect()` sans argument les lit
directement. C'est le chapitre qui équipe ce dépôt de son
environnement (`flake.nix`, puis direnv).
