#!/usr/bin/env python3
"""
Test avancé OpenAI basé sur les suggestions de Benjamin
Diagnostic complet : modèles, organisations, quotas
"""

from openai import OpenAI
import json

def test_connection_advanced():
    """Test de connexion avancé selon les suggestions de Benjamin"""
    
    print("🔬 Test OpenAI avancé - Style Benjamin")
    print("=" * 50)
    
    api_key = "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"
    
    print(f"🔑 API Key: {api_key[:20]}...{api_key[-10:]}")
    print(f"📏 Longueur: {len(api_key)} caractères")
    
    try:
        # 1. Instanciation du client
        print("\n🤖 Instanciation client OpenAI...")
        client = OpenAI(api_key=api_key)
        print(f"✅ Client créé: {client}")
        print(f"📋 Type client: {type(client)}")
        
        # 2. Test des modèles disponibles
        print("\n🎯 Récupération des modèles disponibles...")
        try:
            models = client.models.list()
            available_models = [m.id for m in models.data]
            print(f"✅ {len(available_models)} modèles trouvés")
            
            # Filtrer les modèles GPT
            gpt_models = [m for m in available_models if 'gpt' in m.lower()]
            print(f"🧠 Modèles GPT disponibles: {gpt_models[:5]}...")  # Premiers 5
            
        except Exception as e:
            print(f"❌ Erreur récupération modèles: {e}")
            return False
        
        # 3. Test des organisations
        print("\n🏢 Test des organisations...")
        try:
            # Note: organizations.list() n'existe plus dans la nouvelle API
            # On teste directement avec une requête simple
            print("ℹ️ Test indirect d'organisation via requête simple...")
            
        except Exception as e:
            print(f"⚠️ Info orga non accessible: {e}")
        
        # 4. Tests progressifs des modèles
        models_to_test = [
            ("gpt-3.5-turbo", "Modèle standard le moins cher"),
            ("gpt-4o-mini", "GPT-4 mini économique"),
            ("gpt-4", "GPT-4 complet"),
            ("gpt-4-turbo", "GPT-4 Turbo"),
        ]
        
        print(f"\n🧪 Test progressif des modèles...")
        
        for model, description in models_to_test:
            if model in available_models:
                try:
                    print(f"\n🔹 Test {model} ({description})...")
                    response = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": "Say just 'OK'"}],
                        max_tokens=3,
                        temperature=0
                    )
                    
                    print(f"✅ {model}: '{response.choices[0].message.content}'")
                    print(f"💰 Usage: {response.usage}")
                    
                    # Si on arrive ici, l'API fonctionne !
                    return True, model
                    
                except Exception as e:
                    print(f"❌ {model}: {str(e)[:80]}...")
                    
                    # Analyse spécifique de l'erreur
                    if "429" in str(e):
                        if "insufficient_quota" in str(e):
                            print("   🔍 Quota insuffisant dans cette organisation")
                        elif "rate_limit" in str(e):
                            print("   🔍 Limite de taux dépassée")
                    elif "401" in str(e):
                        print("   🔍 Problème d'authentification")
                    elif "403" in str(e):
                        print("   🔍 Accès refusé à ce modèle")
            else:
                print(f"⚠️ {model}: Non disponible dans votre plan")
        
        return False, None
        
    except Exception as e:
        print(f"💥 Erreur fatale: {e}")
        return False, None

def diagnostic_solutions():
    """Affiche les solutions selon le diagnostic"""
    print(f"\n🛠️ Solutions recommandées:")
    print("1. 🌐 Vérifiez platform.openai.com/account/usage")
    print("2. 💳 Vérifiez Settings → Billing → Usage limits")
    print("3. 🏢 Vérifiez Settings → Organization (bonne orga sélectionnée)")
    print("4. 🔑 Regénérez votre API key si nécessaire")
    print("5. ⏰ Attendez quelques minutes (limite de taux)")
    print("6. 📞 Contactez le support OpenAI si vous avez du crédit")

def create_test_connection_method():
    """Génère le code pour la méthode test_connection à ajouter dans BradAIAgent"""
    
    code = '''
def test_connection(self) -> tuple[bool, str]:
    """
    Test la connexion OpenAI et retourne (success, working_model)
    Méthode inspirée des suggestions de Benjamin
    """
    if not self.client:
        return False, "No client"
    
    try:
        # Test progressif des modèles du moins cher au plus cher
        models_to_test = ["gpt-3.5-turbo", "gpt-4o-mini", "gpt-4"]
        
        for model in models_to_test:
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": "OK"}],
                    max_tokens=1,
                    temperature=0
                )
                print(f"✅ API fonctionnelle avec {model}")
                return True, model
            except Exception as e:
                print(f"⚠️ {model}: {str(e)[:50]}...")
                continue
        
        return False, "All models failed"
        
    except Exception as e:
        print(f"❌ Test connexion échoué: {e}")
        return False, str(e)
'''
    return code

if __name__ == "__main__":
    print("🎭 Test Brad ou Bad - API OpenAI")
    
    # Test principal
    success, working_model = test_connection_advanced()
    
    print(f"\n🎯 Résultats:")
    if success:
        print(f"🎉 SUCCESS! API OpenAI fonctionnelle avec {working_model}")
        print(f"🚀 Brad peut utiliser l'IA pour des réponses ultra-réalistes!")
    else:
        print(f"⚠️ API OpenAI indisponible")
        print(f"🛡️ Brad utilisera le mode de secours (qui fonctionne très bien)")
        diagnostic_solutions()
    
    # Génération du code pour BradAIAgent
    print(f"\n💻 Code à ajouter dans BradAIAgent:")
    print("=" * 40)
    print(create_test_connection_method())
    
    input("\nAppuyez sur Entrée pour continuer...") 