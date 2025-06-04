# -*- coding: utf-8 -*-
"""Simple CLI app for ELADEB-R inspired evaluation"""

from dataclasses import dataclass, field
from typing import List

@dataclass
class Domain:
    name: str
    difficulty: int = 0  # 0: none, 1: peu, 2: important, 3: tres important
    need: int = 0        # 0: none, 1: non urgent, 2: moyennement urgent, 3: urgent
    origin: str = ""     # P, F, E, ?

DOMAINS = [
    "Lieu de vie", "Finances", "Travail", "Droit & justice",
    "Temps libre", "Tâches administratives", "Entretien du ménage", "Déplacements",
    "Fréquentation des lieux publics", "Connaissances et amitiés", "Famille",
    "Enfants", "Relations sentimentales", "Alimentation", "Hygiène personnelle",
    "Santé physique", "Santé psychique", "Addiction", "Traitement",
    "Spiritualité & croyances", "Sexualité"  # optional
]

def ask_question(prompt: str) -> str:
    return input(prompt + "\n> ")


def yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (o/n)\n> ").strip().lower()
        if ans in {"o", "oui"}:
            return True
        if ans in {"n", "non"}:
            return False
        print("Merci de répondre par 'o' ou 'n'.")


def ask_scale(prompt: str, options: List[str]) -> int:
    while True:
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        ans = input(prompt + "\n> ")
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            return int(ans)
        print("Choix invalide, veuillez réessayer.")


def main():
    print("--- Evaluation ELADEB-R simplifiée ---")
    free_question = ask_question("Quel est pour vous le problème le plus important actuellement ?")
    print()
    domains = [Domain(name) for name in DOMAINS]

    # Difficultés
    print("Évaluation des difficultés")
    for d in domains:
        if yes_no(f"Le domaine '{d.name}' pose-t-il un problème actuellement ?"):
            d.difficulty = ask_scale(
                "Degré d'importance du problème :",
                ["Peu important", "Important", "Très important"]
            )
    print()

    # Besoins
    print("Évaluation des besoins d'aide")
    for d in domains:
        if yes_no(f"Avez-vous besoin d'aide supplémentaire pour le domaine '{d.name}' ?"):
            d.need = ask_scale(
                "Urgence de l'aide :",
                ["Non urgent (>3 mois)", "Moyennement urgent (1-3 mois)", "Urgent (<30 jours)"]
            )
            d.origin = ask_question("Origine de l'aide souhaitée (P: professionnels, F: famille, E: entourage, ?: non précisé)")
    print()

    priority = ask_question("Quel est votre besoin prioritaire si une seule chose pouvait être faite ?")
    print()

    # Résultats
    print("--- Résultats ---")
    print(f"Réponse initiale : {free_question}")
    for d in domains:
        print(f"{d.name} - Difficulté: {d.difficulty}, Besoin: {d.need}, Origine: {d.origin}")
    print(f"Besoin prioritaire : {priority}")

    # calculs simples
    total_diff = sum(d.difficulty for d in domains)
    total_need = sum(d.need for d in domains)
    print(f"Score total difficultés: {total_diff}")
    print(f"Score total besoins: {total_need}")

if __name__ == "__main__":
    main()
