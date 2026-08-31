"""pilotage — l'API interne de l'équipe.

La base de données est atteinte par les variables d'environnement
PG* fournies par le shell du projet (flake.nix) : psycopg.connect()
sans argument les lit directement.
"""

from fastapi import FastAPI
import psycopg

app = FastAPI(title="pilotage")


@app.get("/")
def racine():
    return {"service": "pilotage"}


@app.get("/sante")
def sante():
    with psycopg.connect() as conn:
        base, serveur = conn.execute(
            "SELECT current_database(), version()"
        ).fetchone()
    return {"statut": "ok", "base": base, "serveur": serveur}
