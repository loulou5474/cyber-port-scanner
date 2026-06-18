import socket
import sys
from datetime import datetime

# Définition de la cible (tu peux changer l'IP ou le domaine)
# 'localhost' ou '127.0.0.1' correspond à ta propre machine pour tester en toute sécurité
TARGET = "127.0.0.1"

print("-" * 50)
print(f"Scanning de la cible : {TARGET}")
print(f"Début du scan : {str(datetime.now())}")
print("-" * 50)

# Liste des ports les plus courants à tester
ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389]

try:
    for port in ports_to_scan:
        # Configuration du socket (AF_INET pour IPv4, SOCK_STREAM for TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # On définit un timeout court pour ne pas attendre indéfiniment
        s.settimeout(1.0)
        
        # Tentative de connexion au port
        result = s.connect_ex((TARGET, port))
        
        # connect_ex renvoie 0 si la connexion a réussi
        if result == 0:
            print(f"Port {port} : OUVERT")
        else:
            # Optionnel : décommenter la ligne ci-dessous si tu veux voir les ports fermés
            # print(f"Port {port} : Fermé")
            pass
            
        s.close()

except KeyboardInterrupt:
    print("\nScan interrompu par l'utilisateur.")
    sys.exit()

except socket.gaierror:
    print("\nLe nom d'hôte n'a pas pu être résolu.")
    sys.exit()

except socket.error:
    print("\nImpossible de se connecter au serveur.")
    sys.exit()

print("-" * 50)
print("Scan terminé avec succès !")
print("-" * 50)