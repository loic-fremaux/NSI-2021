from __future__ import annotations

import re


class User:
    def __init__(self, sexe: int, nom: str, prenom: str, mail: str):
        if not self.check_valid_email(mail):
            raise ValueError("Mail is not valid")
        self.sexe = sexe
        self.nom = nom
        self.prenom = prenom
        self.mail = mail

    def __repr__(self):
        return self.nom + " " + self.prenom + " [" + self.mail + "]"

    def check_valid_email(self, mail: str) -> bool:
        return bool(re.search("^[a-zA-Z0-9]{3,15}\\.[a-zA-Z0-9]{3,15}@(hmail\\.com|ac-amiens\\.fr|toto\\.org)$", mail))

    def __gt__(self, other: User) -> bool:
        return self.compare_names(other.nom, other.prenom) == 1

    def __ge__(self, other: User) -> bool:
        return self.compare_names(other.nom, other.prenom) > -1

    def __lt__(self, other: User) -> bool:
        return self.compare_names(other.nom, other.prenom) == -1

    def __len__(self, other: User) -> bool:
        return self.compare_names(other.nom, other.prenom) < 1

    def compare_names(self, nom, prenom) -> int:
        if self.nom > nom:
            return 1
        elif self.nom < nom:
            return -1
        else:
            if self.prenom > prenom:
                return 1
            elif self.prenom < prenom:
                return -1
            else:
                return 0


alan_turing = User(1, "Alan", "TURING", "alan.turing@ac-amiens.fr")
alan_turing2 = User(1, "Alan", "TURING", "alan.turing@ac-amiens.fr")
alane_turing = User(1, "Alane", "TURING", "alane.turing@ac-amiens.fr")
print(alan_turing)

print(alan_turing < alane_turing)
print(alane_turing == alane_turing)
