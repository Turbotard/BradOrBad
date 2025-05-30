#!/usr/bin/env python3
"""
Script de debug pour tester la connexion OpenAI et diagnostiquer les problèmes
"""

from openai import OpenAI
import os

def test_openai_connection():
    """Test la connexion OpenAI avec différents diagnostics"""
    
    print("🔍 Diagnostic de l'API OpenAI")
    print("=" * 50)
    
    # Récupération de la clé API depuis les variables d'environnement
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Erreur: Variable d'environnement OPENAI_API_KEY non définie")
        print("💡 Définissez votre clé API avec: export OPENAI_API_KEY='votre_clé'")
        return False
    
    print(f"🔑 Clé API trouvée (longueur: {len(api_key)} caractères)")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test 1: Modèles disponibles
        print("\n🤖 Test 1: Vérification des modèles disponibles...")
        try:
            models = client.models.list()
            print(f"✅ {len(models.data)} modèles disponibles")
            
            # Affichage des modèles GPT
            gpt_models = [m.id for m in models.data if 'gpt' in m.id.lower()]
            if gpt_models:
                print(f"📋 Modèles GPT détectés: {gpt_models[:3]}...")
            
        except Exception as e:
            print(f"❌ Erreur modèles: {e}")
            return False
        
        # Test 2: Chat completion simple
        print("\n💬 Test 2: Chat completion...")
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Bonjour, répondez juste 'Test OK'"}],
                max_tokens=10
            )
            
            message = response.choices[0].message.content
            print(f"✅ Réponse reçue: '{message}'")
            
        except Exception as e:
            print(f"❌ Erreur chat: {e}")
            
            # Diagnostics d'erreurs courantes
            if "insufficient_quota" in str(e):
                print("💰 Problème: Quota insuffisant ou crédit épuisé")
                print("1. Vérifiez votre solde sur platform.openai.com")
                print("2. Ajoutez un mode de paiement")
            elif "invalid_api_key" in str(e):
                print("🔑 Problème: Clé API invalide")
                print("1. Vérifiez votre clé sur platform.openai.com/api-keys")
                print("2. Générez une nouvelle clé si nécessaire")
            elif "rate_limit" in str(e):
                print("⏱️ Problème: Limite de taux dépassée")
                print("1. Attendez quelques minutes")
                print("2. Réessayez plus tard")
            
            return False
        
        print("\n🎉 Tous les tests sont passés avec succès !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur de connexion: {e}")
        return False

def test_with_fallback():
    """Test avec modèle de secours"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Clé API non définie")
        return False
        
    client = OpenAI(api_key=api_key)
    
    models_to_try = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4"]
    
    for model in models_to_try:
        try:
            print(f"\n🧪 Test avec {model}...")
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Dis juste 'OK'"}],
                max_tokens=5
            )
            print(f"✅ {model} fonctionne !")
            return True
        except Exception as e:
            print(f"❌ {model} échoué: {e}")
    
    return False

if __name__ == "__main__":
    print("🔬 Script de diagnostic OpenAI")
    print("🔑 Assurez-vous d'avoir défini OPENAI_API_KEY dans vos variables d'environnement")
    print()
    
    success = test_openai_connection()
    
    if success:
        print("✅ API OpenAI fonctionnelle")
        test_with_fallback()
    else:
        print("⚠️ API OpenAI indisponible")
        print("🔧 Suivez les instructions ci-dessus pour résoudre le problème")
        print("💡 Contactez le support OpenAI si vous avez du crédit") 