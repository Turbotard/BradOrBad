#!/usr/bin/env python3
"""
Script de démarrage rapide pour Brad ou Bad
Installe les dépendances et lance l'application Streamlit
"""

import subprocess
import sys
import os

def install_requirements():
    """Installe les dépendances depuis requirements.txt"""
    print("🔧 Installation des dépendances...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dépendances installées avec succès !")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'installation : {e}")
        return False

def launch_streamlit():
    """Lance l'application Streamlit"""
    print("🚀 Lancement de Brad ou Bad...")
    try:
        # Essayer d'abord avec python -m streamlit (recommandé pour Windows)
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main.py"])
    except KeyboardInterrupt:
        print("\n👋 Application fermée par l'utilisateur")
    except FileNotFoundError:
        # Si streamlit n'est pas trouvé, essayer la commande directe
        try:
            print("⚡ Tentative avec la commande streamlit directe...")
            subprocess.run(["streamlit", "run", "main.py"])
        except FileNotFoundError:
            print("❌ Streamlit non trouvé. Veuillez vérifier l'installation.")
            print("💡 Essayez : pip install streamlit")
    except Exception as e:
        print(f"❌ Erreur lors du lancement : {e}")

def main():
    """Fonction principale"""
    print("🎭 Brad ou Bad ? - Le Coach IA anti-brouteur")
    print("=" * 50)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists("main.py"):
        print("❌ Fichier main.py introuvable. Assurez-vous d'être dans le bon répertoire.")
        sys.exit(1)
    
    # Installer les dépendances
    if install_requirements():
        print("\n🎯 Prêt à démarrer !")
        print("📖 L'application va s'ouvrir automatiquement sur http://localhost:8501")
        print("⚡ Appuyez sur Ctrl+C pour arrêter l'application")
        print("🤖 Mode IA : Utilise l'intelligence artificielle pour s'adapter à vos réponses")
        print("🛡️ Mode secours : Fonctionne même sans connexion API\n")
        
        # Lancer Streamlit
        launch_streamlit()
    else:
        print("❌ Impossible de démarrer l'application.")
        sys.exit(1)

if __name__ == "__main__":
    main() 