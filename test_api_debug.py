#!/usr/bin/env python3
"""
Script de debug pour tester la connexion OpenAI et diagnostiquer les problèmes
"""

from openai import OpenAI
import os

def test_openai_connection():
    """Test la connexion OpenAI avec différents diagnostics"""
    
    print("🔍 Diagnostic de l'API OpenAI")
    print("=" * 40)
    
    # Test avec la clé fournie
    api_key = "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"
    
    print(f"🔑 Clé API (masquée): {api_key[:20]}...{api_key[-10:]}")
    print(f"📏 Longueur clé: {len(api_key)} caractères")
    
    try:
        client = OpenAI(api_key=api_key)
        
        # Test simple avec très peu de tokens
        print("\n🧪 Test 1: Requête minimale...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modèle moins cher
            messages=[
                {"role": "user", "content": "Hi"}
            ],
            max_tokens=5,  # Très peu de tokens
            temperature=0
        )
        
        print("✅ Test 1 réussi !")
        print(f"Réponse: {response.choices[0].message.content}")
        
        # Test avec gpt-4
        print("\n🧪 Test 2: GPT-4...")
        response2 = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "Say 'OK'"}
            ],
            max_tokens=3,
            temperature=0
        )
        
        print("✅ Test 2 réussi !")
        print(f"Réponse GPT-4: {response2.choices[0].message.content}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur API: {str(e)}")
        
        # Analyse détaillée de l'erreur
        if "429" in str(e):
            print("\n🔍 Erreur 429 détectée:")
            print("• Quota insuffisant OU")
            print("• Limite de taux dépassée OU") 
            print("• Problème de facturation")
            
        elif "401" in str(e):
            print("\n🔍 Erreur 401 détectée:")
            print("• Clé API invalide")
            print("• Clé expirée")
            
        elif "403" in str(e):
            print("\n🔍 Erreur 403 détectée:")
            print("• Accès refusé")
            print("• Compte suspendu")
            
        print(f"\n💡 Solutions possibles:")
        print("1. Vérifiez votre solde sur platform.openai.com")
        print("2. Vérifiez les limites de dépenses dans 'Usage limits'")
        print("3. Essayez de régénérer votre clé API")
        print("4. Vérifiez que le bon compte/organisation est sélectionné")
        
        return False

def test_models_availability():
    """Test quels modèles sont disponibles"""
    api_key = "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"
    
    try:
        client = OpenAI(api_key=api_key)
        print("\n📋 Modèles disponibles:")
        
        models_to_test = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o-mini"]
        
        for model in models_to_test:
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": "Hi"}],
                    max_tokens=1
                )
                print(f"✅ {model}: Disponible")
            except Exception as e:
                print(f"❌ {model}: {str(e)[:50]}...")
                
    except Exception as e:
        print(f"❌ Impossible de lister les modèles: {e}")

if __name__ == "__main__":
    # Test principal
    success = test_openai_connection()
    
    if not success:
        print("\n🔧 Test des modèles individuels...")
        test_models_availability()
    
    print(f"\n🎯 Résumé:")
    if success:
        print("✅ API OpenAI fonctionnelle")
        print("🚀 Problème résolu ! Brad va utiliser l'IA")
    else:
        print("⚠️ API OpenAI indisponible") 
        print("🛡️ Brad utilisera le mode de secours")
        print("💡 Contactez le support OpenAI si vous avez du crédit")
    
    input("\nAppuyez sur Entrée pour continuer...") 