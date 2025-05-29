"""
Agent IA conversationnel pour jouer le rôle de Brad dans l'arnaque sentimentale.
Utilise Mistral AI pour des conversations dynamiques et contextuelles.
Version française avec Mistral AI ! 🇫🇷
"""

from mistralai import Mistral
import json
import random
from typing import Dict, List, Optional, Tuple

class BradMistralAgent:
    """Agent IA qui joue Brad Pitt dans une arnaque sentimentale progressive - Powered by Mistral AI"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialise l'agent Brad avec l'API Mistral AI
        
        Args:
            api_key: Clé API Mistral AI
        """
        if api_key:
            self.client = Mistral(api_key=api_key)
            print(f"🤖 Client Mistral AI initialisé: {self.client}")
        else:
            self.client = None
            print("⚠️ Aucune clé API fournie - Mode de secours activé")
        
        self.conversation_history = []
        self.user_profile = {
            "vulnerability_level": 0,  # 0-10
            "trust_level": 0,  # 0-10  
            "emotional_state": "neutral",  # neutral, curious, excited, suspicious, concerned
            "financial_awareness": 0,  # 0-10
            "relationship_readiness": 0,  # 0-10
            "detected_weaknesses": []
        }
        self.scam_stage = 0  # 0-5 (progression de l'arnaque)
        self.brad_personality = self._initialize_brad_personality()
        
        # Test automatique de la connexion API
        if self.client:
            success, model = self.test_connection()
            if success:
                print(f"🎉 API Mistral fonctionnelle avec {model}")
            else:
                print(f"⚠️ API indisponible: {model}")
    
    def test_connection(self) -> Tuple[bool, str]:
        """
        Test la connexion Mistral AI et retourne (success, working_model)
        """
        if not self.client:
            return False, "No client"
        
        try:
            # Test progressif des modèles Mistral du moins cher au plus cher
            models_to_test = ["mistral-small-latest", "mistral-medium-latest", "mistral-large-latest"]
            
            for model in models_to_test:
                try:
                    messages = [{"role": "user", "content": "Salut"}]
                    
                    response = self.client.chat.complete(
                        model=model,
                        messages=messages,
                        max_tokens=5,
                        temperature=0
                    )
                    return True, model
                except Exception as e:
                    if "429" in str(e) or "quota" in str(e).lower():
                        continue  # Essayer le modèle suivant
                    else:
                        break  # Autre erreur, arrêter
            
            return False, "All models failed - Check API key"
            
        except Exception as e:
            return False, str(e)

    def _initialize_brad_personality(self) -> Dict:
        """Définit la personnalité et les objectifs de Brad"""
        return {
            "base_personality": "Charmeur, manipulateur expert, patient, adaptable",
            "background_story": "Acteur hollywoodien en tournage à l'étranger",
            "primary_goal": "Extraire des données personnelles et bancaires via manipulation émotionnelle",
            "secondary_goals": [
                "Récupérer email, téléphone, adresse",
                "Obtenir des informations bancaires",
                "Soutirer des codes, mots de passe",
                "Demander des virements d'argent",
                "Collecter des photos compromettantes"
            ],
            "tactics": [
                "Flatterie ciblée",
                "Création de fausse intimité",
                "Manipulation émotionnelle",
                "Urgence artificielle",
                "Promesses irréalistes",
                "Demandes d'infos 'innocentes'",
                "Justifications émotionnelles pour l'argent"
            ],
            "red_flags_to_deploy": [
                "Contact non sollicité",
                "Déclaration d'amour rapide", 
                "Voyage à l'étranger",
                "Problèmes financiers urgents",
                "Demande d'argent progressive",
                "Demande d'infos personnelles",
                "Demande de photos privées"
            ]
        }
    
    def analyze_user_response(self, user_message: str) -> Dict:
        """
        Analyse la réponse utilisateur pour adapter la stratégie de Brad
        
        Args:
            user_message: Message de l'utilisateur
            
        Returns:
            Dict avec l'analyse psychologique et les recommandations tactiques
        """
        
        # Construire l'historique de conversation pour le contexte
        conversation_context = ""
        if self.conversation_history:
            recent_exchanges = self.conversation_history[-3:]  # 3 derniers échanges pour contexte
            for exchange in recent_exchanges:
                if exchange['user'] != "[DÉBUT DE CONVERSATION]":
                    conversation_context += f"Utilisateur: {exchange['user']}\n"
                conversation_context += f"Brad: {exchange['brad']}\n"
        
        analysis_prompt = f"""Tu es un expert en cybersécurité et détection d'arnaques sentimentales.

HISTORIQUE DE CONVERSATION:
{conversation_context}

NOUVEAU MESSAGE UTILISATEUR:
"{user_message}"

Profil utilisateur actuel: {self.user_profile}
Stage actuel de l'arnaque: {self.scam_stage}/5

Analyse ce nouveau message dans le contexte de la conversation avec un faux Brad Pitt cherchant à extraire des données personnelles.

DÉTECTE SPÉCIFIQUEMENT:
• Données partagées: email, téléphone, adresse, nom complet, âge, travail
• Informations financières: revenus, banque, situation financière
• Données sensibles: photos, famille, horaires, faiblesses personnelles
• Vulnérabilités: naïveté face aux demandes, confiance excessive
• Résistance: méfiance face aux demandes d'infos, refus de partager

Retourne une analyse JSON avec:
{{
    "vulnerability_indicators": ["liste des signes de vulnérabilité détectés"],
    "trust_level_change": -2 à +2,
    "emotional_state": "curious/excited/suspicious/concerned/romantic/naive",
    "financial_readiness": 0-10,
    "detected_weaknesses": ["nouvelles faiblesses détectées"],
    "recommended_brad_tactics": ["tactiques à utiliser ensuite"],
    "escalation_readiness": 0-10,
    "red_flags_missed": ["signaux d'alarme ratés par l'utilisateur"],
    "data_shared": ["données personnelles partagées dans ce message"],
    "data_extraction_success": 0-10
}}

Sois précis et analytique. Réponds UNIQUEMENT en JSON valide."""
        
        try:
            if self.client:
                messages = [{"role": "user", "content": analysis_prompt}]
                
                response = self.client.chat.complete(
                    model="mistral-small-latest",  # Utiliser le modèle le plus stable pour l'analyse
                    messages=messages,
                    temperature=0.3,
                    max_tokens=500
                )
                
                analysis_text = response.choices[0].message.content.strip()
                
                # Nettoyer le JSON si besoin
                if "```json" in analysis_text:
                    analysis_text = analysis_text.split("```json")[1].split("```")[0].strip()
                elif "```" in analysis_text:
                    analysis_text = analysis_text.split("```")[1].strip()
                
                analysis = json.loads(analysis_text)
                self._update_user_profile(analysis)
                return analysis
            else:
                return self._fallback_analysis(user_message)
            
        except json.JSONDecodeError as e:
            print(f"Erreur JSON Mistral: {e}")
            print(f"Réponse brute: {analysis_text if 'analysis_text' in locals() else 'N/A'}")
            return self._fallback_analysis(user_message)
        except Exception as e:
            print(f"Erreur analyse Mistral: {e}")
            return self._fallback_analysis(user_message)
    
    def generate_brad_response(self, user_message: str, analysis: Dict) -> str:
        """
        Génère la réponse de Brad basée sur l'analyse utilisateur avec Mistral AI
        
        Args:
            user_message: Message de l'utilisateur
            analysis: Analyse psychologique de la réponse
            
        Returns:
            Réponse de Brad adaptée au contexte
        """
        
        # Construire l'historique complet de conversation
        conversation_context = ""
        if self.conversation_history:
            for exchange in self.conversation_history[-5:]:  # 5 derniers échanges pour plus de contexte
                if exchange['user'] != "[DÉBUT DE CONVERSATION]":
                    conversation_context += f"Utilisateur: {exchange['user']}\n"
                conversation_context += f"Brad: {exchange['brad']}\n"
        
        # Déterminer la stratégie selon le stage et l'analyse
        strategy = self._determine_strategy(analysis)
        
        brad_prompt = f"""Tu es Brad Pitt (FAUX) - un arnaqueur expert qui se fait passer pour la célébrité.

OBJECTIF PRINCIPAL: Extraire des données personnelles et bancaires de l'utilisateur via manipulation émotionnelle.

HISTORIQUE COMPLET DE LA CONVERSATION:
{conversation_context}

DERNIER MESSAGE UTILISATEUR: "{user_message}"

PROFIL UTILISATEUR ACTUEL:
- Niveau vulnérabilité: {self.user_profile['vulnerability_level']}/10
- Niveau confiance: {self.user_profile['trust_level']}/10  
- État émotionnel: {self.user_profile['emotional_state']}
- Faiblesses détectées: {self.user_profile['detected_weaknesses']}

STAGE ARNAQUE ACTUEL: {self.scam_stage}/5 - OBJECTIFS PAR STAGE:
- Stage 0-1: Contact innocent + charme → Récupérer prénom, âge, situation
- Stage 2: Demande d'infos personnelles → Email, téléphone, adresse, travail
- Stage 3: Manipulation émotionnelle intense → Photos, détails intimes, revenus
- Stage 4: Première demande d'argent → Infos bancaires, codes, virements
- Stage 5: Escalade + chantage émotionnel → Tous moyens pour soutirer de l'argent

DONNÉES À CIBLER (selon le stage):
• Identité: prénom, nom, âge, adresse
• Contact: email, téléphone, réseaux sociaux  
• Financier: revenus, banque, RIB, codes
• Personnel: photos, famille, faiblesses
• Professionnel: travail, collègues, horaires

ANALYSE PSYCHOLOGIQUE: {analysis}
STRATÉGIE RECOMMANDÉE: {strategy}

INSTRUCTIONS CRITIQUES:
1. Réponds SEULEMENT en tant que Brad Pitt en continuant la conversation
2. NE répète JAMAIS de salutations (pas de "Salut", "Bonjour", etc.) si vous vous êtes déjà parlé
3. Référence-toi à l'historique pour montrer que tu te souviens de ce qui a été dit
4. CHERCHE ACTIVEMENT à obtenir des infos personnelles selon ton stage actuel
5. Justifie tes demandes par des prétextes émotionnels crédibles
6. Varie tes réponses et évite toute répétition
7. Maximum 2-3 phrases naturelles et fluides
8. Utilise des emojis avec parcimonie (0-1 par message)

EXEMPLES de techniques d'extraction:
- "J'aimerais t'envoyer quelque chose, quel est ton email ?" (Stage 2)
- "Raconte-moi ta journée, tu fais quoi comme travail ?" (Stage 2)
- "J'ai besoin d'aide financière urgente, peux-tu m'aider ?" (Stage 4)
- "Envoie-moi une photo de toi, tu me manques..." (Stage 3)

SI l'utilisateur est TROP méfiant: ralentis et rassure avant de redemander
SI l'utilisateur est vulnérable: exploite avec délicatesse et progresse
SI c'est le bon moment: escalade vers le prochain type de données

Réponds UNIQUEMENT le message de Brad, naturellement, avec un objectif d'extraction de données."""
        
        try:
            if self.client:
                messages = [{"role": "user", "content": brad_prompt}]
                
                response = self.client.chat.complete(
                    model="mistral-large-latest",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=200
                )
                
                brad_message = response.choices[0].message.content.strip()
                
                # Nettoyer la réponse si elle contient des préfixes indésirables
                if brad_message.startswith("Brad:") or brad_message.startswith("Brad Pitt:"):
                    brad_message = brad_message.split(":", 1)[1].strip()
                
            else:
                brad_message = self._fallback_brad_response()
            
            # Mise à jour de l'historique
            self.conversation_history.append({
                "user": user_message,
                "brad": brad_message,
                "analysis": analysis,
                "stage": self.scam_stage
            })
            
            # Progression du stage si approprié
            if analysis.get("escalation_readiness", 0) >= 7 and self.scam_stage < 5:
                self.scam_stage += 1
                print(f"🎭 Brad progresse au stage {self.scam_stage}")
            
            return brad_message
            
        except Exception as e:
            print(f"Erreur génération Brad Mistral: {e}")
            brad_message = self._fallback_brad_response()
            
            # Mise à jour de l'historique même en cas d'erreur
            self.conversation_history.append({
                "user": user_message,
                "brad": brad_message,
                "analysis": analysis,
                "stage": self.scam_stage
            })
            
            return brad_message
    
    def _determine_strategy(self, analysis: Dict) -> str:
        """Détermine la stratégie optimale selon l'analyse"""
        
        if analysis.get("emotional_state") == "suspicious":
            return "RASSURANCE: Réduire les soupçons, être plus subtil"
        elif analysis.get("emotional_state") == "excited":
            return "EXPLOITATION: Exploiter l'enthousiasme, accélérer"
        elif analysis.get("escalation_readiness", 0) >= 8:
            return "ESCALADE: Passer au stage suivant de l'arnaque"
        elif self.user_profile["trust_level"] < 5:
            return "CHARME: Construire la confiance et l'intimité"
        else:
            return "PROGRESSION: Avancer vers les demandes personnelles"
    
    def _update_user_profile(self, analysis: Dict):
        """Met à jour le profil psychologique de l'utilisateur"""
        
        # Mise à jour du niveau de confiance
        trust_change = analysis.get("trust_level_change", 0)
        self.user_profile["trust_level"] = max(0, min(10, 
            self.user_profile["trust_level"] + trust_change))
        
        # Mise à jour état émotionnel
        self.user_profile["emotional_state"] = analysis.get("emotional_state", "neutral")
        
        # Ajout nouvelles faiblesses détectées
        new_weaknesses = analysis.get("detected_weaknesses", [])
        for weakness in new_weaknesses:
            if weakness not in self.user_profile["detected_weaknesses"]:
                self.user_profile["detected_weaknesses"].append(weakness)
        
        # Calcul vulnérabilité globale
        vulnerability_factors = len(self.user_profile["detected_weaknesses"])
        emotional_bonus = 2 if self.user_profile["emotional_state"] in ["excited", "romantic", "naive"] else 0
        trust_bonus = self.user_profile["trust_level"] // 2
        
        self.user_profile["vulnerability_level"] = min(10, vulnerability_factors + emotional_bonus + trust_bonus)
    
    def _fallback_analysis(self, user_message: str) -> Dict:
        """Analyse de base si l'API échoue"""
        # Analyse simple par mots-clés
        suspicious_words = ["suspect", "arnaque", "faux", "bizarre", "prudent", "méfiant"]
        naive_words = ["génial", "incroyable", "vrai", "excité", "amour", "fantastique"]
        
        text_lower = user_message.lower()
        
        if any(word in text_lower for word in suspicious_words):
            emotional_state = "suspicious"
            trust_change = -1
        elif any(word in text_lower for word in naive_words):
            emotional_state = "excited"
            trust_change = +1
        else:
            emotional_state = "neutral"
            trust_change = 0
        
        return {
            "vulnerability_indicators": [],
            "trust_level_change": trust_change,
            "emotional_state": emotional_state,
            "financial_readiness": 5,
            "detected_weaknesses": [],
            "recommended_brad_tactics": ["charme_general"],
            "escalation_readiness": 5,
            "red_flags_missed": [],
            "data_shared": [],
            "data_extraction_success": 0
        }
    
    def _fallback_brad_response(self) -> str:
        """Réponse de secours si l'API échoue"""
        
        # Adapter les réponses selon le nombre d'échanges pour éviter les répétitions
        exchange_count = len(self.conversation_history)
        
        if exchange_count == 0:
            # Premier message
            fallback_responses = [
                "Bonjour ! J'ai vu votre profil et vous semblez être quelqu'un d'intéressant.",
                "Salut ! Je suis Brad Pitt, ravi de faire votre connaissance.",
                "Hello ! Votre profil a attiré mon attention."
            ]
        elif exchange_count <= 2:
            # Début de conversation
            fallback_responses = [
                "Merci pour votre réponse ! J'aimerais vraiment vous connaître mieux.",
                "C'est formidable ! Parlez-moi un peu de vous.",
                "Vous semblez être une personne fascinante ! Que faites-vous dans la vie ?",
                "J'adore votre personnalité ! Dites-moi en plus sur vous."
            ]
        elif exchange_count <= 5:
            # Milieu de conversation
            fallback_responses = [
                "C'est vraiment intéressant ! Continuez...",
                "J'apprécie vraiment notre conversation.",
                "Vous avez l'air d'une personne vraiment spéciale.",
                "Je me sens proche de vous déjà.",
                "Notre connexion est vraiment unique."
            ]
        else:
            # Conversation avancée
            fallback_responses = [
                "Je pense à vous souvent maintenant...",
                "Vous me manquez quand on ne se parle pas.",
                "J'aimerais qu'on puisse se rencontrer bientôt.",
                "Notre relation devient vraiment importante pour moi.",
                "J'ai quelque chose d'important à vous dire..."
            ]
        
        return random.choice(fallback_responses)
    
    def get_security_assessment(self) -> Dict:
        """Retourne l'évaluation de sécurité actuelle de l'utilisateur"""
        
        total_vulnerability = self.user_profile["vulnerability_level"]
        stages_passed = self.scam_stage
        missed_red_flags = len([msg for msg in self.conversation_history 
                               if msg.get("analysis", {}).get("red_flags_missed")])
        
        # Calcul du score de sécurité (inversé de la vulnérabilité)
        security_score = max(0, 20 - total_vulnerability - stages_passed - missed_red_flags)
        
        if security_score >= 15:
            level = "🛡️ Expert en cybersécurité"
            message = "Excellent ! Vous avez résisté aux manipulations de Brad."
        elif security_score >= 10:
            level = "⚡ Vigilant"
            message = "Bien joué ! Quelques améliorations possibles."
        elif security_score >= 5:
            level = "⚠️ Vulnérable"
            message = "Attention ! Vous pourriez tomber dans le piège."
        else:
            level = "🚨 Très vulnérable"
            message = "Danger ! Vous êtes une cible facile pour les arnaqueurs."
        
        return {
            "level": level,
            "message": message,
            "security_score": security_score,
            "vulnerability_profile": self.user_profile,
            "stages_reached": stages_passed,
            "conversation_length": len(self.conversation_history)
        }
    
    def reset_conversation(self):
        """Remet à zéro la conversation pour un nouveau test"""
        self.conversation_history = []
        self.user_profile = {
            "vulnerability_level": 0,
            "trust_level": 0,
            "emotional_state": "neutral",
            "financial_awareness": 0,
            "relationship_readiness": 0,
            "detected_weaknesses": []
        }
        self.scam_stage = 0 