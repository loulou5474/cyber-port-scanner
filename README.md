# Simple TCP Port Scanner

Un scanner de ports TCP basique écrit en Python, développé dans un but éducatif pour comprendre le fonctionnement des connexions réseau et de la reconnaissance (Recon) en cybersécurité.

## Fonctionnalités
- Scan une liste de ports standards (HTTP, HTTPS, SSH, FTP, etc.).
- Utilise la bibliothèque native `socket` de Python (aucune dépendance externe requise).
- Gestion des interruptions utilisateur (Ctrl+C).

## Utilisation
1. Assurez-vous d'avoir Python 3 installé.
2. Clonez le dépôt.
3. Modifiez la variable `TARGET` dans le script avec l'adresse IP souhaitée.
4. Lancez le script :
   ```bash
   python port_scanner.py
