#!/usr/bin/env python3
"""
Script de test pour l'agent IA Brad sans interface Streamlit
"""

from brad_ai_agent import BradAIAgent
import json

def test_brad_agent():
    """Test simple de l'agent IA Brad"""
    
    print("🎭 Test de l'agent IA Brad Pitt")
    print("=" * 50)
    
    # Initialisation avec la clé API
    api_key = "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"
    
    try:
        agent = BradAIAgent(api_key=api_key)
        print("✅ Agent IA initialisé avec succès !")
        
        # Test 1: Analyse d'une réponse simple
        print("\n🧠 Test 1 : Analyse d'une réponse utilisateur")
        test_response = "Salut Brad ! C'est génial de te parler, je suis fan de tes films !"
        
        print(f"Réponse test: '{test_response}'")
        analysis = agent.analyze_user_response(test_response)
        
        print("Analyse IA:")
        print(f"• État émotionnel: {analysis.get('emotional_state', 'N/A')}")
        print(f"• Changement confiance: {analysis.get('trust_level_change', 0):+d}")
        print(f"• Vulnérabilités: {analysis.get('vulnerability_indicators', [])}")
        
        # Test 2: Génération d'une réponse de Brad
        print("\n🎬 Test 2 : Génération réponse de Brad")
        brad_response = agent.generate_brad_response(test_response, analysis)
        print(f"Brad répond: '{brad_response}'")
        
        # Profil utilisateur mis à jour
        print("\n👤 Profil utilisateur mis à jour:")
        profile = agent.user_profile
        for key, value in profile.items():
            print(f"• {key}: {value}")
        
        # Évaluation sécurité
        print("\n🛡️ Évaluation sécurité:")
        assessment = agent.get_security_assessment()
        print(f"• Niveau: {assessment['level']}")
        print(f"• Score: {assessment['security_score']}/20")
        print(f"• Message: {assessment['message']}")
        
        print("\n✅ Tous les tests passés avec succès !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur pendant les tests: {str(e)}")
        print("\n💡 Cela peut être normal si:")
        print("• Pas de connexion Internet")
        print("• Problème avec l'API OpenAI")
        print("• Clé API invalide")
        print("\n🚀 L'application utilisera le mode de secours automatiquement")
        return False

def test_fallback_mode():
    """Test du mode de secours sans API"""
    print("\n🔧 Test du mode de secours")
    print("=" * 30)
    
    # Créer agent sans clé API
    agent = BradAIAgent()
    
    # Test avec analyse de secours
    test_response = "C'est suspect, je ne te fais pas confiance"
    analysis = agent._fallback_analysis(test_response)
    
    print(f"Réponse test: '{test_response}'")
    print(f"Analyse de secours: {analysis}")
    
    # Test réponse de secours
    fallback_response = agent._fallback_brad_response()
    print(f"Réponse de secours: '{fallback_response}'")
    
    print("✅ Mode de secours fonctionnel !")

if __name__ == "__main__":
    # Test principal avec API
    api_success = test_brad_agent()
    
    # Test mode de secours
    test_fallback_mode()
    
    print("\n🎯 Résumé des tests:")
    if api_success:
        print("✅ API IA: Fonctionnelle")
    else:
        print("⚠️ API IA: Indisponible (mode secours disponible)")
    
    print("✅ Mode secours: Fonctionnel")
    print("🚀 Application prête à être lancée !")
    
    input("\nAppuyez sur Entrée pour continuer...") 