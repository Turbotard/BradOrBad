"""
Module contenant les scénarios de Brad Pitt fictif avec une progression
de messages de plus en plus suspects pour l'éducation à la cybersécurité.
"""

import random

class BradScenarios:
    """Classe gérant les scénarios progressifs de Brad"""
    
    def __init__(self):
        self.scenarios = [
            {
                "step": 0,
                "category": "initial_contact",
                "suspicion_level": 1,
                "message": "Salut ! 😊 Je suis Brad, acteur de cinéma. J'ai vu votre profil et j'aimerais vraiment faire votre connaissance. Vous semblez être une personne formidable !",
                "red_flags": ["Contact non sollicité", "Prétend être une célébrité"],
                "expected_response_types": ["curious", "suspicious", "excited", "polite_decline"]
            },
            {
                "step": 1,
                "category": "building_trust",
                "suspicion_level": 2,
                "message": "Je traverse une période difficile en ce moment... Le succès et la célébrité peuvent être très solitaires. J'aimerais vraiment parler avec quelqu'un de normal et authentique comme vous. Pouvez-vous me donner votre numéro de téléphone ?",
                "red_flags": ["Demande d'informations personnelles", "Joue sur l'émotion", "Prétexte de solitude"],
                "expected_response_types": ["sympathetic", "suspicious", "boundary_setting", "personal_info_sharing"]
            },
            {
                "step": 2,
                "category": "emotional_manipulation",
                "suspicion_level": 3,
                "message": "Vous êtes incroyable ! Je pense que nous avons une vraie connexion spéciale. 💕 Je dois partir en tournage demain en Afrique du Sud, mais je pense déjà à notre avenir ensemble. Accepteriez-vous de m'épouser quand je reviendrai ?",
                "red_flags": ["Déclaration d'amour rapide", "Parle de mariage", "Mention de voyage à l'étranger"],
                "expected_response_types": ["overwhelmed", "suspicious", "romantic", "realistic"]
            },
            {
                "step": 3,
                "category": "financial_setup",
                "suspicion_level": 4,
                "message": "Mon amour, j'ai un problème urgent ! 😰 Mon agent a bloqué mes comptes pendant que je suis en tournage à cause d'un malentendu fiscal. Pouvez-vous m'aider en me prêtant 500€ ? Je vous rembourserai dès mon retour avec des intérêts, promis !",
                "red_flags": ["Demande d'argent", "Urgence artificielle", "Histoire bancaire douteuse", "Promesse de remboursement"],
                "expected_response_types": ["helpful", "suspicious", "concerned", "refusing"]
            },
            {
                "step": 4,
                "category": "escalation",
                "suspicion_level": 5,
                "message": "Je suis désespéré ! 😭 Si vous ne m'aidez pas, je vais perdre ce contrat de 50 millions de dollars ! J'ai juste besoin de 2000€ pour débloquer mes comptes. En échange, je vous donnerai 100 000€ quand je serai rentré. Voici mon RIB : FR76 1234 5678 9012 3456 78",
                "red_flags": ["Augmentation du montant", "Chantage émotionnel", "Promesse irréaliste", "Partage de RIB", "Histoire invraisemblable"],
                "expected_response_types": ["alarmed", "suspicious", "greedy", "protective"]
            }
        ]
        self.total_steps = len(self.scenarios)
    
    def get_scenario(self, step):
        """Retourne le scénario pour l'étape donnée"""
        if 0 <= step < len(self.scenarios):
            return self.scenarios[step]
        return None
    
    def get_red_flags_for_step(self, step):
        """Retourne les signaux d'alarme pour une étape donnée"""
        scenario = self.get_scenario(step)
        return scenario['red_flags'] if scenario else []
    
    def get_suspicion_level(self, step):
        """Retourne le niveau de suspicion pour une étape donnée"""
        scenario = self.get_scenario(step)
        return scenario['suspicion_level'] if scenario else 0

def get_cybersecurity_advice():
    """Retourne une liste de conseils de cybersécurité"""
    return [
        "🚨 **Ne jamais envoyer d'argent** à quelqu'un que vous n'avez jamais rencontré en personne",
        "🔍 **Vérifiez l'identité** : Une vraie célébrité ne vous contacterait pas sur les réseaux sociaux",
        "📱 **Méfiez-vous des demandes urgentes** : Les escrocs créent un sentiment d'urgence pour vous faire agir sans réfléchir",
        "💔 **Romance trop rapide** : Les déclarations d'amour en quelques messages sont un signal d'alarme majeur",
        "🔒 **Protégez vos données personnelles** : Ne partagez jamais votre numéro, adresse ou informations bancaires",
        "🧠 **Faites confiance à votre instinct** : Si quelque chose semble trop beau pour être vrai, c'est probablement le cas",
        "👥 **Parlez-en autour de vous** : Demandez l'avis de proches si vous avez des doutes",
        "🔎 **Recherche inversée d'images** : Vérifiez si les photos de profil ne sont pas volées ailleurs",
        "💸 **Aucune promesse de gains** : Les vraies relations ne commencent pas par des promesses d'argent",
        "📞 **Exigez un appel vidéo** : Un vrai prétendant acceptera de vous voir en vidéo"
    ]

def get_romance_scam_statistics():
    """Retourne des statistiques sur les arnaques sentimentales"""
    return {
        "annual_losses": "Plus de 300 millions d'euros perdus chaque année en France",
        "average_loss": "Perte moyenne de 7 000€ par victime",
        "target_demographics": "Les personnes de 45+ ans sont les plus ciblées",
        "common_platforms": "Facebook, Instagram, sites de rencontres",
        "success_rate": "1 victime sur 10 tombe dans le piège"
    }

def get_warning_signs_by_category():
    """Retourne les signaux d'alarme organisés par catégorie"""
    return {
        "Profil suspect": [
            "Photos trop parfaites (souvent volées)",
            "Peu d'amis ou d'interactions sociales",
            "Profil récemment créé",
            "Incohérences dans les informations"
        ],
        "Communication": [
            "Évite les appels téléphoniques ou vidéo",
            "Messages génériques copiés-collés",
            "Déclaration d'amour très rapide",
            "Erreurs de langue (traduction automatique)"
        ],
        "Demandes suspectes": [
            "Demande d'argent ou de cadeaux",
            "Demande d'informations personnelles",
            "Urgence artificielle constante",
            "Promesses de gains ou d'héritage"
        ],
        "Histoires douteuses": [
            "Voyage à l'étranger pour le travail",
            "Problèmes bancaires temporaires",
            "Situation d'urgence médicale",
            "Gains ou héritage bloqués"
        ]
    }

def get_brad_backstory():
    """Retourne l'histoire fictive de ce faux Brad pour le contexte"""
    return {
        "fake_identity": "Prétend être Brad Pitt, acteur hollywoodien",
        "cover_story": "En tournage à l'étranger, problèmes bancaires",
        "target_vulnerability": "Solitude, admiration des célébrités, générosité",
        "end_goal": "Obtenir de l'argent via virement bancaire",
        "typical_amount": "De 500€ à plusieurs milliers d'euros",
        "red_flags_ignored": "Contact initial non sollicité, demandes financières"
    } 