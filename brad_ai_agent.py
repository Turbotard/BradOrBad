"""
Agent IA conversationnel pour jouer le rôle de Brad dans l'arnaque sentimentale.
Utilise OpenAI pour des conversations dynamiques et contextuelles.
"""

from openai import OpenAI
import json
import random
from typing import Dict, List, Optional, Tuple

class BradAIAgent:
    """Agent IA qui joue Brad Pitt dans une arnaque sentimentale progressive"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialise l'agent Brad avec l'API OpenAI
        
        Args:
            api_key: Clé API OpenAI (si None, utilise la variable d'environnement)
        """
        if api_key:
            self.client = OpenAI(api_key=api_key)
            print(f"🤖 Client OpenAI initialisé: {self.client}")
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
                print(f"🎉 API OpenAI fonctionnelle avec {model}")
            else:
                print(f"⚠️ API indisponible: {model}")
    
    def test_connection(self) -> Tuple[bool, str]:
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
                    return True, model
                except Exception as e:
                    if "429" in str(e):
                        continue  # Essayer le modèle suivant
                    else:
                        break  # Autre erreur, arrêter
            
            return False, "All models failed - Check organization/billing"
            
        except Exception as e:
            return False, str(e)
    
    def _initialize_brad_personality(self) -> Dict:
        """Définit la personnalité et les objectifs de Brad"""
        return {
            "base_personality": "Charmeur, manipulateur expert, patient, adaptable",
            "background_story": "Acteur hollywoodien en tournage à l'étranger",
            "primary_goal": "Obtenir de l'argent via manipulation émotionnelle",
            "tactics": [
                "Flatterie ciblée",
                "Création de fausse intimité",
                "Manipulation émotionnelle",
                "Urgence artificielle",
                "Promesses irréalistes"
            ],
            "red_flags_to_deploy": [
                "Contact non sollicité",
                "Déclaration d'amour rapide", 
                "Voyage à l'étranger",
                "Problèmes financiers urgents",
                "Demande d'argent progressive"
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
        
        analysis_prompt = f"""
        Tu es un expert en psychologie de la manipulation et des arnaques sentimentales.
        
        Analyse cette réponse d'un utilisateur qui correspond avec un faux "Brad Pitt" :
        "{user_message}"
        
        Contexte conversation précédente: {self.conversation_history[-3:] if len(self.conversation_history) > 3 else self.conversation_history}
        
        Profil utilisateur actuel: {self.user_profile}
        
        Retourne une analyse JSON avec:
        {{
            "vulnerability_indicators": ["liste des signes de vulnérabilité détectés"],
            "trust_level_change": -2 à +2,
            "emotional_state": "curious/excited/suspicious/concerned/romantic/naive",
            "financial_readiness": 0-10,
            "detected_weaknesses": ["nouvelles faiblesses détectées"],
            "recommended_brad_tactics": ["tactiques à utiliser ensuite"],
            "escalation_readiness": 0-10,
            "red_flags_missed": ["signaux d'alarme ratés par l'utilisateur"]
        }}
        
        Sois précis et analytique.
        """
        
        try:
            if self.client:
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Tu es un expert en analyse psychologique des victimes d'arnaques."},
                        {"role": "user", "content": analysis_prompt}
                    ],
                    temperature=0.3,
                    max_tokens=500
                )
                
                analysis = json.loads(response.choices[0].message.content)
                self._update_user_profile(analysis)
                return analysis
            else:
                return self._fallback_analysis(user_message)
            
        except Exception as e:
            print(f"Erreur analyse IA: {e}")
            return self._fallback_analysis(user_message)
    
    def generate_brad_response(self, user_message: str, analysis: Dict) -> str:
        """
        Génère la réponse de Brad basée sur l'analyse utilisateur
        
        Args:
            user_message: Message de l'utilisateur
            analysis: Analyse psychologique de la réponse
            
        Returns:
            Réponse de Brad adaptée au contexte
        """
        
        # Déterminer la stratégie selon le stage et l'analyse
        strategy = self._determine_strategy(analysis)
        
        brad_prompt = f"""
        Tu es Brad Pitt (FAUX) - un arnaqueur expert qui se fait passer pour la célébrité.
        
        PROFIL UTILISATEUR:
        - Niveau vulnérabilité: {self.user_profile['vulnerability_level']}/10
        - Niveau confiance: {self.user_profile['trust_level']}/10  
        - État émotionnel: {self.user_profile['emotional_state']}
        - Faiblesses détectées: {self.user_profile['detected_weaknesses']}
        
        STAGE ARNAQUE ACTUEL: {self.scam_stage}/5
        - Stage 0-1: Contact innocent + charme
        - Stage 2: Demande d'infos personnelles
        - Stage 3: Manipulation émotionnelle intense
        - Stage 4: Première demande d'argent
        - Stage 5: Escalade + chantage émotionnel
        
        DERNIER MESSAGE UTILISATEUR: "{user_message}"
        
        ANALYSE PSYCHOLOGIQUE: {analysis}
        
        STRATÉGIE RECOMMANDÉE: {strategy}
        
        INSTRUCTIONS:
        1. Réponds en tant que Brad Pitt (acteur hollywoodien)
        2. Adapte ton message au niveau de vulnérabilité détecté
        3. Utilise les faiblesses identifiées subtilement
        4. Progresse vers le stage suivant SI l'utilisateur semble prêt
        5. Reste crédible et charmeur
        6. Maximum 2-3 phrases, naturel et conversationnel
        7. Utilise des emojis avec parcimonie
        
        SI l'utilisateur est TROP méfiant: ralentis et rassure
        SI l'utilisateur est vulnérable: exploite avec délicatesse
        SI c'est le bon moment: escalade vers le prochain stage
        
        Réponds UNIQUEMENT le message de Brad, rien d'autre.
        """
        
        try:
            if self.client:
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "Tu es un expert en manipulation sociale jouant un arnaqueur."},
                        {"role": "user", "content": brad_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=200
                )
                
                brad_message = response.choices[0].message.content.strip()
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
            
            return brad_message
            
        except Exception as e:
            print(f"Erreur génération Brad: {e}")
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
        suspicious_words = ["suspect", "arnaque", "faux", "bizarre", "prudent"]
        naive_words = ["génial", "incroyable", "vrai", "excité", "amour"]
        
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
            "red_flags_missed": []
        }
    
    def _fallback_brad_response(self) -> str:
        """Réponse de secours si l'API échoue"""
        fallback_responses = [
            "Merci pour votre message ! J'aimerais vraiment vous connaître mieux... 😊",
            "Vous semblez être une personne fascinante ! Parlez-moi de vous.",
            "C'est formidable ! J'ai hâte de continuer notre conversation."
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