#!/usr/bin/env python3
"""
Script de diagnostic complet OpenAI selon l'analyse de Benjamin
Teste organisation, type de clé, accès API, etc.
"""

import sys
import openai
from openai import OpenAI
import os

def analyze_api_key_format(api_key):
    """Analyse le format de la clé API"""
    print(f"\n🔍 Analyse du format de clé")
    print(f"🔑 Clé: {api_key[:20]}...{api_key[-10:]}")
    print(f"📏 Longueur: {len(api_key)} caractères")
    
    if api_key.startswith("sk-"):
        if "proj-" in api_key:
            print("✅ Format: Clé projet (sk-proj-...)")
            return "project"
        else:
            print("✅ Format: Clé standard (sk-...)")
            return "standard"
    elif api_key.startswith("sess-"):
        print("⚠️ Format: Clé session (temporaire)")
        return "session"
    else:
        print("❌ Format: Clé invalide ou inconnue")
        return "invalid"

def test_new_syntax():
    """Test avec la nouvelle syntaxe OpenAI v1.x"""
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Variable d'environnement OPENAI_API_KEY non définie")
        return False
        
    print("\n🧪 Test avec OpenAI v1.x (nouvelle syntaxe)")
    
    try:
        analyze_api_key_format(api_key)
        
        client = OpenAI(api_key=api_key)
        
        print("\n💬 Test chat completion...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Bonjour, répondez juste 'Test réussi'"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ Réponse: {result}")
        print("🎉 Nouvelle syntaxe: FONCTIONNELLE")
        return True
        
    except Exception as e:
        print(f"❌ Erreur nouvelle syntaxe: {e}")
        return False

def test_old_syntax():
    """Test avec l'ancienne syntaxe OpenAI v0.x"""
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Variable d'environnement OPENAI_API_KEY non définie")
        return False
        
    print("\n🧪 Test avec OpenAI v0.x (ancienne syntaxe)")
    
    try:
        # Configuration globale (ancienne méthode)
        openai.api_key = api_key
        
        # Ancienne méthode de chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Dites juste 'Test OK'"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ Réponse: {result}")
        print("🎉 Ancienne syntaxe: FONCTIONNELLE")
        return True
        
    except Exception as e:
        print(f"❌ Erreur ancienne syntaxe: {e}")
        return False

def test_models_and_limits():
    """Test des modèles disponibles et limites"""
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Variable d'environnement OPENAI_API_KEY non définie")
        return False
        
    print("\n🤖 Test des modèles disponibles")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test avec différents modèles
        models_to_test = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4"]
        
        for model in models_to_test:
            try:
                print(f"\n🧪 Test {model}...")
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": "Hi"}],
                    max_tokens=5
                )
                print(f"✅ {model}: Disponible")
                
            except Exception as e:
                if "model" in str(e).lower():
                    print(f"❌ {model}: Non disponible dans votre plan")
                else:
                    print(f"❌ {model}: Erreur - {str(e)[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur test modèles: {e}")
        return False

def diagnose_errors(api_key):
    """Diagnostic avancé des erreurs"""
    print("\n🔧 Diagnostic avancé")
    
    if not api_key:
        print("❌ Clé API manquante")
        print("1. 📍 Va sur https://platform.openai.com/account/api-keys")
        print("2. 🔑 Génère une nouvelle clé")
        print("3. 💾 Sauvegarde-la dans tes variables d'environnement")
        return
    
    # Vérifications de format
    key_type = analyze_api_key_format(api_key)
    
    if key_type == "invalid":
        print("2. 🔑 Crée une vraie clé API sur platform.openai.com")
        return
    
    print("\n🏢 Vérifications organisationnelles")
    if key_type == "project":
        print("1. 🏢 Vérifie ton organisation sur platform.openai.com/account/org-settings")
        print("2. 💳 Vérifie le mode de paiement de l'organisation")
        print("3. 📊 Vérifie les quotas sur platform.openai.com/account/usage")
    
    print("\n💰 Si tu as des erreurs de quota:")
    print("• Vérifie ton solde")
    print("• Ajoute un mode de paiement")
    print("• Vérifie les limites de dépenses")
    print("• Attends le renouvellement mensuel")
    
    print("\n🆘 Si rien ne fonctionne:")
    print("• Contacte le support OpenAI")
    print("• Vérifie les status sur status.openai.com")

def main():
    """Fonction principale du diagnostic"""
    print("🔬 DIAGNOSTIC COMPLET OPENAI - Style Benjamin")
    print("=" * 60)
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Variable d'environnement OPENAI_API_KEY non définie")
        print("💡 Définissez votre clé API avec: export OPENAI_API_KEY='votre_clé'")
        diagnose_errors(None)
        return
    
    key_type = analyze_api_key_format(api_key)
    
    # Tests selon les recommandations de Benjamin
    print(f"\n🎯 Tests adaptés pour clé {key_type}")
    
    success_new = test_new_syntax()
    success_old = test_old_syntax() if not success_new else True
    success_models = test_models_and_limits()
    
    print(f"\n📊 RÉSULTATS FINAUX")
    print("=" * 30)
    print(f"✅ Nouvelle syntaxe: {'✅' if success_new else '❌'}")
    print(f"✅ Ancienne syntaxe: {'✅' if success_old else '❌'}")
    print(f"✅ Modèles testés: {'✅' if success_models else '❌'}")
    
    if success_new:
        print("\n🎉 SUCCESS! API fonctionnelle")
        print("🚀 Brad peut utiliser l'IA complète")
    else:
        print("\n⚠️ Problèmes détectés")
        diagnose_errors(api_key)

if __name__ == "__main__":
    main() 