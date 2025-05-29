#!/usr/bin/env python3
"""
Script de diagnostic complet OpenAI selon l'analyse de Benjamin
Teste organisation, type de clé, accès API, etc.
"""

import openai
from openai import OpenAI
import json

def analyze_api_key_format(api_key):
    """Analyse le format de la clé API"""
    print("🔍 Analyse du format de clé API:")
    print(f"🔑 Clé: {api_key[:20]}...{api_key[-10:]}")
    print(f"📏 Longueur: {len(api_key)} caractères")
    
    if api_key.startswith("sk-"):
        if "proj-" in api_key:
            print("⚠️ Type: Clé PROJECT (sk-proj-...)")
            print("💡 Peut ne pas marcher avec tous les endpoints")
            return "project"
        else:
            print("✅ Type: Clé API standard (sk-...)")
            return "standard"
    elif api_key.startswith("sess-"):
        print("❌ Type: Clé SESSION (sess-...)")
        print("🚫 Ne fonctionne PAS avec l'API - seulement ChatGPT web")
        return "session"
    else:
        print("❓ Type: Format inconnu")
        return "unknown"

def test_with_new_client():
    """Test avec la nouvelle syntaxe OpenAI v1.x"""
    api_key = "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"
    
    print("\n🧪 Test avec OpenAI v1.x (nouvelle syntaxe)")
    print("=" * 50)
    
    try:
        client = OpenAI(api_key=api_key)
        print(f"✅ Client créé: {type(client)}")
        
        # Vérifier l'organisation
        print(f"🏢 Organisation: {getattr(client, 'organization', 'Non spécifiée')}")
        
        # Test minimal
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Salut, qui es-tu ?"}],
            max_tokens=10
        )
        
        print("🎉 SUCCESS avec nouvelle syntaxe !")
        print(f"💬 Réponse: {response.choices[0].message.content}")
        return True, "new_syntax"
        
    except Exception as e:
        print(f"❌ Erreur nouvelle syntaxe: {str(e)[:100]}...")
        return False, str(e)

def test_with_old_client():
    """Test avec l'ancienne syntaxe OpenAI v0.x"""
    api_key = "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"
    
    print("\n🧪 Test avec OpenAI v0.x (ancienne syntaxe)")
    print("=" * 50)
    
    try:
        openai.api_key = api_key
        
        # Test avec ancienne syntaxe
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Salut, qui es-tu ?"}],
            max_tokens=10
        )
        
        print("🎉 SUCCESS avec ancienne syntaxe !")
        print(f"💬 Réponse: {response.choices[0].message.content}")
        return True, "old_syntax"
        
    except Exception as e:
        print(f"❌ Erreur ancienne syntaxe: {str(e)[:100]}...")
        return False, str(e)

def test_organizations():
    """Test avec différentes organisations"""
    api_key = "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"
    
    print("\n🏢 Test des organisations")
    print("=" * 30)
    
    # Test sans organisation spécifique
    try:
        client = OpenAI(api_key=api_key)
        
        # Essayer de lister les modèles pour voir l'org
        models = client.models.list()
        print(f"✅ Connexion réussie à l'organisation par défaut")
        print(f"📋 {len(models.data)} modèles disponibles")
        
        return True
        
    except Exception as e:
        print(f"❌ Problème organisation: {str(e)[:100]}...")
        return False

def diagnostic_solutions(key_type, errors):
    """Propose des solutions selon le diagnostic"""
    print("\n🛠️ DIAGNOSTIC ET SOLUTIONS")
    print("=" * 40)
    
    if key_type == "project":
        print("🔸 Problème probable: Clé PROJECT mal configurée")
        print("✅ Solutions:")
        print("1. 📍 Va sur https://platform.openai.com/account/api-keys")
        print("2. 🔑 Crée une nouvelle clé 'User' (pas Project)")
        print("3. 🗑️ Supprime l'ancienne clé project")
        
    elif key_type == "session":
        print("🔸 Problème: Clé SESSION invalide pour l'API")
        print("✅ Solutions:")
        print("1. 🚫 Cette clé ne marche QUE pour ChatGPT web")
        print("2. 🔑 Crée une vraie clé API sur platform.openai.com")
        
    elif "429" in str(errors):
        print("🔸 Problème: Quota/Organisation")
        print("✅ Solutions:")
        print("1. 🏢 Vérifie ton organisation sur platform.openai.com/account/org-settings")
        print("2. 💳 Va sur Billing → vérifie que l'API est activée")
        print("3. 💰 Assure-toi que tes 15$ sont dans la BONNE organisation")
        print("4. 🔄 Change le budget mensuel de $0 à $5-10")
        
    elif "401" in str(errors):
        print("🔸 Problème: Authentification")
        print("✅ Solutions:")
        print("1. 🔑 Clé API invalide - regénère-la")
        print("2. ⏰ Clé expirée")
        print("3. 🏢 Mauvaise organisation")
        
    print(f"\n📞 Si rien ne marche:")
    print("• Contacte le support OpenAI")
    print("• Ou utilise le mode de secours (qui fonctionne très bien !)")

def main():
    """Diagnostic complet"""
    print("🔬 DIAGNOSTIC COMPLET OPENAI - Style Benjamin")
    print("=" * 60)
    
    api_key = "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"
    
    # 1. Analyse du format
    key_type = analyze_api_key_format(api_key)
    
    errors = []
    
    # 2. Test nouvelle syntaxe
    success_new, error_new = test_with_new_client()
    if not success_new:
        errors.append(error_new)
    
    # 3. Test ancienne syntaxe  
    success_old, error_old = test_with_old_client()
    if not success_old:
        errors.append(error_old)
    
    # 4. Test organisations
    org_success = test_organizations()
    
    # 5. Résultats et solutions
    print(f"\n🎯 RÉSULTATS FINAUX")
    print("=" * 25)
    
    if success_new or success_old:
        print("🎉 API FONCTIONNELLE !")
        syntax = "nouvelle" if success_new else "ancienne"
        print(f"✅ Marche avec syntaxe {syntax}")
        print("🚀 Brad peut utiliser l'IA complète !")
    else:
        print("⚠️ API NON FONCTIONNELLE")
        print("🛡️ Brad utilisera le mode de secours")
        diagnostic_solutions(key_type, errors)
    
    print(f"\n💻 Ton app Brad ou Bad fonctionne parfaitement quoi qu'il arrive !")

if __name__ == "__main__":
    main()
    input("\nAppuyez sur Entrée pour continuer...") 