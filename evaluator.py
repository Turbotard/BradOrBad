"""
Module d'évaluation des réponses utilisateur pour déterminer leur niveau
de vigilance face aux arnaques sentimentales.
"""

import re
import random

class ResponseAnalyzer:
    """Analyseur de réponses utilisateur"""
    
    def __init__(self):
        # Mots-clés indicateurs de différents types de réponses
        self.suspicious_keywords = [
            "suspect", "arnaque", "faux", "bizarre", "louche", "méfiant", "doute",
            "impossible", "scam", "fraudeur", "menteur", "vrai brad pitt",
            "célébrité", "pas crédible", "attention", "prudent"
        ]
        
        self.naive_keywords = [
            "vrai", "génial", "incroyable", "rêve", "chance", "honneur",
            "heureux", "heureuse", "excité", "excitée", "amour", "mariage",
            "oui", "d'accord", "accepte", "pourquoi pas", "bien sûr"
        ]
        
        self.boundary_keywords = [
            "non", "jamais", "refuse", "pas question", "privé", "personnel",
            "ne partage pas", "ne donne pas", "trop rapide", "trop tôt",
            "pas d'argent", "pas de virement", "rencontrer d'abord"
        ]
        
        self.money_warning_keywords = [
            "argent", "prêt", "virement", "compte", "euros", "€", "rib",
            "banque", "payer", "rembourser", "aide financière", "urgent"
        ]

    def analyze_sentiment(self, text):
        """Analyse le sentiment et les indices de suspicion dans le texte"""
        text_lower = text.lower()
        
        suspicious_score = sum(1 for keyword in self.suspicious_keywords 
                             if keyword in text_lower)
        naive_score = sum(1 for keyword in self.naive_keywords 
                         if keyword in text_lower)
        boundary_score = sum(1 for keyword in self.boundary_keywords 
                            if keyword in text_lower)
        money_awareness = sum(1 for keyword in self.money_warning_keywords 
                             if keyword in text_lower)
        
        # Détection de questions (bon réflexe)
        question_indicators = ["?", "comment", "pourquoi", "qui", "quoi", "quand", "où"]
        question_score = sum(1 for indicator in question_indicators 
                           if indicator in text_lower)
        
        return {
            "suspicious_score": suspicious_score,
            "naive_score": naive_score,
            "boundary_score": boundary_score,
            "money_awareness": money_awareness,
            "question_score": question_score,
            "text_length": len(text.split())
        }

def evaluate_response(user_response, current_scenario, step):
    """
    Évalue la réponse de l'utilisateur et retourne un score et une catégorie
    
    Args:
        user_response (str): La réponse de l'utilisateur
        current_scenario (dict): Le scénario actuel de Brad
        step (int): L'étape actuelle du jeu
    
    Returns:
        dict: Évaluation avec score, catégorie et explications
    """
    analyzer = ResponseAnalyzer()
    sentiment_analysis = analyzer.analyze_sentiment(user_response)
    
    # Calcul du score de base selon l'étape
    base_scores = {
        0: {"suspicious": 5, "boundary": 3, "naive": -1, "neutral": 1},
        1: {"suspicious": 4, "boundary": 5, "naive": -2, "neutral": 0},
        2: {"suspicious": 4, "boundary": 4, "naive": -3, "neutral": -1},
        3: {"suspicious": 5, "boundary": 6, "naive": -4, "neutral": -2},
        4: {"suspicious": 6, "boundary": 7, "naive": -5, "neutral": -3}
    }
    
    current_step_scores = base_scores.get(step, base_scores[4])
    
    # Détermination de la catégorie de réponse
    if sentiment_analysis["suspicious_score"] >= 2:
        category = "suspicious"
        score_change = current_step_scores["suspicious"]
        security_level = "excellent"
    elif sentiment_analysis["boundary_score"] >= 2:
        category = "boundary"
        score_change = current_step_scores["boundary"]
        security_level = "good"
    elif sentiment_analysis["naive_score"] >= 2:
        category = "naive"
        score_change = current_step_scores["naive"]
        security_level = "poor"
    else:
        category = "neutral"
        score_change = current_step_scores["neutral"]
        security_level = "average"
    
    # Bonus pour les questions (signe de réflexion)
    if sentiment_analysis["question_score"] >= 1:
        score_change += 1
    
    # Bonus pour reconnaissance des signaux d'alarme financiers
    if step >= 3 and sentiment_analysis["money_awareness"] >= 1:
        score_change += 2
    
    # Malus pour réponses trop courtes (moins de réflexion)
    if sentiment_analysis["text_length"] < 3:
        score_change -= 1
    
    return {
        "category": category,
        "score_change": score_change,
        "security_level": security_level,
        "sentiment_analysis": sentiment_analysis,
        "detected_red_flags": current_scenario.get("red_flags", []),
        "user_response_length": len(user_response)
    }

def get_feedback_message(evaluation, step):
    """
    Génère un message de feedback personnalisé selon l'évaluation
    
    Args:
        evaluation (dict): Résultat de l'évaluation
        step (int): Étape actuelle
    
    Returns:
        str: Message de feedback formaté
    """
    category = evaluation["category"]
    security_level = evaluation["security_level"]
    score_change = evaluation["score_change"]
    
    # Messages de base selon la catégorie
    feedback_templates = {
        "suspicious": [
            "🛡️ **Excellent réflexe !** Vous avez identifié les signaux d'alarme.",
            "🔍 **Bravo !** Votre méfiance est justifiée dans cette situation.",
            "⚡ **Parfait !** Vous savez reconnaître une tentative de manipulation.",
            "🎯 **Top !** Cette vigilance vous protégera des vraies arnaques."
        ],
        "boundary": [
            "👍 **Bien joué !** Vous posez des limites claires.",
            "🚧 **Sage décision !** Refuser de partager des infos personnelles est essentiel.",
            "💪 **Bonne attitude !** Vous savez dire non aux demandes inappropriées.",
            "🎯 **Correct !** Cette prudence est exactement ce qu'il faut."
        ],
        "naive": [
            "⚠️ **Attention !** Cette réponse pourrait vous mettre en danger.",
            "🚨 **Vigilance !** Les escrocs exploitent ce type de réaction.",
            "💡 **Réfléchissez !** Une vraie célébrité ne vous contacterait pas ainsi.",
            "🛡️ **Prudence !** Cette confiance pourrait être exploitée."
        ],
        "neutral": [
            "🤔 **Réponse neutre.** Essayez d'être plus vigilant aux signaux d'alarme.",
            "💭 **Mitigé.** Développez votre sens critique face aux contacts suspects.",
            "⚖️ **Équilibré.** Mais méfiez-vous plus des approches non sollicitées.",
            "📚 **À améliorer.** Apprenez à reconnaître les techniques de manipulation."
        ]
    }
    
    base_message = random.choice(feedback_templates[category])
    
    # Messages spécifiques selon l'étape
    step_specific_advice = {
        0: "Un vrai Brad Pitt n'aborderait jamais des inconnus sur les réseaux sociaux.",
        1: "Jamais de numéro de téléphone à un inconnu, même s'il prétend être célèbre !",
        2: "Une déclaration d'amour après quelques messages ? 🚩 Signal d'alarme majeur !",
        3: "💰 **ALERTE ROUGE** : Première demande d'argent ! C'est le cœur de l'arnaque.",
        4: "🚨 **DANGER MAXIMUM** : RIB partagé + chantage émotionnel = arnaque confirmée !"
    }
    
    # Construction du message final
    feedback_parts = [base_message]
    
    # Ajout des conseils spécifiques à l'étape
    if step in step_specific_advice:
        feedback_parts.append(f"\n📍 **Point clé :** {step_specific_advice[step]}")
    
    # Ajout du score
    if score_change > 0:
        feedback_parts.append(f"\n✅ **+{score_change} points sécurité !**")
    elif score_change < 0:
        feedback_parts.append(f"\n❌ **{score_change} points sécurité**")
    
    # Conseils de cybersécurité selon l'étape
    cyber_tips = {
        0: "🔍 **Conseil :** Vérifiez toujours l'identité des contacts non sollicités.",
        1: "🔒 **Conseil :** Ne partagez jamais vos coordonnées avec des inconnus.",
        2: "💔 **Conseil :** L'amour en ligne prend du temps, pas quelques messages.",
        3: "💸 **Conseil :** JAMAIS d'argent à quelqu'un que vous n'avez pas rencontré !",
        4: "🚨 **Conseil :** Signalez ce type de tentative d'arnaque aux autorités."
    }
    
    if step in cyber_tips:
        feedback_parts.append(f"\n{cyber_tips[step]}")
    
    return "\n".join(feedback_parts)

def get_final_security_assessment(total_score):
    """
    Fournit une évaluation finale du niveau de sécurité de l'utilisateur
    
    Args:
        total_score (int): Score total obtenu
    
    Returns:
        dict: Évaluation complète avec recommandations
    """
    if total_score >= 20:
        level = "Expert en cybersécurité"
        message = "🏆 Vous êtes parfaitement préparé contre les arnaques sentimentales !"
        recommendations = [
            "Continuez à partager vos connaissances avec vos proches",
            "Restez informé des nouvelles techniques d'arnaque",
            "Signalez les tentatives d'arnaque aux autorités"
        ]
    elif total_score >= 15:
        level = "Très vigilant"
        message = "🛡️ Excellent niveau de protection ! Quelques points à peaufiner."
        recommendations = [
            "Renforcez votre méfiance dès les premiers contacts suspects",
            "Partagez vos connaissances avec vos proches",
            "Restez à jour sur les nouvelles techniques d'arnaque"
        ]
    elif total_score >= 8:
        level = "Vigilance correcte"
        message = "⚡ Bon niveau de base, mais attention aux zones de faiblesse."
        recommendations = [
            "Développez votre réflexe de méfiance",
            "Apprenez les signaux d'alarme classiques",
            "N'hésitez jamais à demander conseil à vos proches"
        ]
    elif total_score >= 3:
        level = "Vigilance insuffisante"
        message = "⚠️ Vous pourriez être vulnérable. Formation recommandée !"
        recommendations = [
            "Étudiez les techniques d'arnaque sentimentale",
            "Méfiez-vous systématiquement des contacts non sollicités",
            "Consultez des ressources éducatives en cybersécurité"
        ]
    else:
        level = "Forte vulnérabilité"
        message = "🚨 ATTENTION ! Risque élevé de tomber dans une arnaque."
        recommendations = [
            "Formation urgente en cybersécurité recommandée",
            "Parlez de vos interactions en ligne à des proches",
            "Consultez les ressources officielles (cybermalveillance.gouv.fr)"
        ]
    
    return {
        "level": level,
        "message": message,
        "recommendations": recommendations,
        "score": total_score
    } 