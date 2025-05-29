import streamlit as st
import os
from dotenv import load_dotenv
from brad_mistral_agent import BradMistralAgent

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Brad ou Bad ? 🎭 - Agent Mistral IA 🇫🇷",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour améliorer l'apparence
st.markdown("""
<style>
.brad-message {
    background: linear-gradient(135deg, #ff6b6b, #ee5a52);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 15px 0;
    box-shadow: 0 4px 8px rgba(255, 107, 107, 0.3);
    position: relative;
}
.brad-message::before {
    content: "🎬";
    position: absolute;
    top: -5px;
    left: -5px;
    background: white;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}
.user-message {
    background: linear-gradient(135deg, #4dabf7, #339af0);
    color: white;
    padding: 20px;
    border-radius: 15px;
    margin: 15px 0;
    box-shadow: 0 4px 8px rgba(77, 171, 247, 0.3);
    position: relative;
}
.user-message::before {
    content: "👤";
    position: absolute;
    top: -5px;
    right: -5px;
    background: white;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}
.analysis-box {
    background: linear-gradient(135deg, #ffd43b, #fab005);
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    color: #495057;
    font-size: 14px;
    border-left: 4px solid #fd7e14;
}
.vulnerability-high {
    background: linear-gradient(135deg, #fa5252, #e03131);
    color: white;
}
.vulnerability-medium {
    background: linear-gradient(135deg, #fd7e14, #e8590c);
    color: white;
}
.vulnerability-low {
    background: linear-gradient(135deg, #51cf66, #37b24d);
    color: white;
}
.stage-indicator {
    background: linear-gradient(135deg, #845ef7, #7048e8);
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    text-align: center;
    font-weight: bold;
    margin: 10px 0;
}
.real-time-analysis {
    background: rgba(134, 94, 247, 0.1);
    border: 2px solid #845ef7;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
}
.mistral-badge {
    background: linear-gradient(135deg, #ff7f50, #ff6347);
    color: white;
    padding: 5px 15px;
    border-radius: 15px;
    font-size: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialise les variables de session Streamlit"""
    if 'brad_agent' not in st.session_state:
        # Récupération de la clé API Mistral depuis les variables d'environnement
        api_key = os.getenv('MISTRAL_API_KEY')
        
        if not api_key:
            st.error("⚠️ Clé API Mistral non trouvée ! Vérifiez votre fichier .env")
            st.stop()
        
        st.session_state.brad_agent = BradMistralAgent(api_key=api_key)
    
    if 'conversation_started' not in st.session_state:
        st.session_state.conversation_started = False
    
    if 'show_analysis' not in st.session_state:
        st.session_state.show_analysis = True
    
    if 'conversation_ended' not in st.session_state:
        st.session_state.conversation_ended = False

def display_header():
    """Affiche l'en-tête de l'application"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.title("🎭 Brad ou Bad ? - Agent Mistral IA")
        st.subheader("Coach IA anti-brouteur avec Intelligence Artificielle Française 🇫🇷")
    
    with col2:
        st.markdown('<div class="mistral-badge">🇫🇷 Powered by Mistral AI</div>', unsafe_allow_html=True)
    
    # Informations agent
    agent = st.session_state.brad_agent
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        vulnerability_level = agent.user_profile["vulnerability_level"]
        vulnerability_class = "vulnerability-high" if vulnerability_level >= 7 else "vulnerability-medium" if vulnerability_level >= 4 else "vulnerability-low"
        st.markdown(f"""
        <div class="{vulnerability_class}" style="padding: 10px; border-radius: 10px; text-align: center;">
            <strong>🎯 Vulnérabilité</strong><br>
            {vulnerability_level}/10
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        trust_level = agent.user_profile["trust_level"]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #20c997, #12b886); color: white; padding: 10px; border-radius: 10px; text-align: center;">
            <strong>🤝 Confiance</strong><br>
            {trust_level}/10
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        emotional_state = agent.user_profile["emotional_state"]
        emotion_emoji = {"neutral": "😐", "curious": "🤔", "excited": "😍", "suspicious": "🤨", "concerned": "😰", "romantic": "💕", "naive": "😊"}
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #a855f7, #9333ea); color: white; padding: 10px; border-radius: 10px; text-align: center;">
            <strong>{emotion_emoji.get(emotional_state, "😐")} État</strong><br>
            {emotional_state.title()}
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        scam_stage = agent.scam_stage
        st.markdown(f"""
        <div class="stage-indicator">
            <strong>🎭 Stage Arnaque</strong><br>
            {scam_stage}/5
        </div>
        """, unsafe_allow_html=True)

    # Description du stage actuel
    stage_descriptions = {
        0: "🟢 Contact Initial - Brad établit le premier contact",
        1: "🟡 Charme & Confiance - Brad développe la relation",
        2: "🟠 Collecte de Données - Brad demande email, téléphone, adresse",
        3: "🔴 Manipulation Émotionnelle - Brad cherche photos et infos intimes",
        4: "🚨 Demande d'Argent - Brad veut vos infos bancaires et codes",
        5: "💀 Chantage & Escalade - Brad utilise tous les moyens"
    }
    
    st.markdown(f"""
    <div style="background: rgba(255, 127, 80, 0.1); padding: 15px; border-radius: 10px; margin: 20px 0; border-left: 4px solid #ff7f50;">
        <strong>📍 Stage actuel :</strong> {stage_descriptions.get(scam_stage, "Inconnu")}
        <br><span style="font-size: 12px; color: #666;">🇫🇷 Analysé par Mistral AI en temps réel</span>
    </div>
    """, unsafe_allow_html=True)

    # Affichage des données collectées par Brad
    all_data_shared = []
    for exchange in agent.conversation_history:
        if 'analysis' in exchange and 'data_shared' in exchange['analysis']:
            all_data_shared.extend(exchange['analysis']['data_shared'])
    
    if all_data_shared:
        st.markdown(f"""
        <div style="background: rgba(220, 53, 69, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #dc3545;">
            <strong>⚠️ Données récupérées par Brad :</strong><br>
            {' • '.join(set(all_data_shared))}
            <br><span style="font-size: 12px; color: #dc3545;">🚨 Dans une vraie arnaque, ces infos seraient utilisées contre vous !</span>
        </div>
        """, unsafe_allow_html=True)

def display_conversation():
    """Affiche l'historique de conversation avec l'agent IA"""
    agent = st.session_state.brad_agent
    
    if not agent.conversation_history:
        st.markdown("""
        <div style="text-align: center; padding: 40px; background: rgba(255, 127, 80, 0.1); border-radius: 15px; margin: 20px 0;">
            <h3>🎬 Brad Pitt souhaite vous parler...</h3>
            <p>Un message de quelqu'un prétendant être Brad Pitt vient d'arriver. Êtes-vous prêt à tester votre vigilance ?</p>
            <div class="mistral-badge" style="margin-top: 10px;">🇫🇷 Intelligence Artificielle Française</div>
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.subheader("💬 Conversation en cours")
    
    for i, exchange in enumerate(agent.conversation_history):
        # D'abord afficher le message utilisateur (si ce n'est pas le premier message d'initialisation)
        if exchange['user'] != "[DÉBUT DE CONVERSATION]":
            st.markdown(f"""
            <div class="user-message">
                <strong>Vous :</strong><br>
                {exchange['user']}
            </div>
            """, unsafe_allow_html=True)
        
        # Puis afficher la réponse de Brad
        st.markdown(f"""
        <div class="brad-message">
            <strong>Brad Pitt :</strong><br>
            {exchange['brad']}
        </div>
        """, unsafe_allow_html=True)
        
        # Analyse en temps réel (si activée)
        if st.session_state.show_analysis and 'analysis' in exchange:
            analysis = exchange['analysis']
            
            with st.expander(f"🔍 Analyse Mistral IA - Échange #{i+1}", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**🧠 État psychologique détecté :**")
                    st.write(f"• État émotionnel: `{analysis.get('emotional_state', 'neutral')}`")
                    st.write(f"• Changement confiance: `{analysis.get('trust_level_change', 0):+d}`")
                    st.write(f"• Prêt pour escalade: `{analysis.get('escalation_readiness', 0)}/10`")
                
                with col2:
                    st.markdown("**⚠️ Signaux détectés :**")
                    vulnerabilities = analysis.get('vulnerability_indicators', [])
                    if vulnerabilities:
                        for vuln in vulnerabilities[:3]:  # Limite à 3
                            st.write(f"• {vuln}")
                    else:
                        st.write("• Aucune vulnérabilité majeure détectée")
                
                # Tactiques recommandées pour Brad
                if analysis.get('recommended_brad_tactics'):
                    st.markdown("**🎭 Tactiques IA de Brad :**")
                    tactics = analysis.get('recommended_brad_tactics', [])
                    st.write(f"• {', '.join(tactics[:2])}")  # Montre 2 tactiques max
                
                st.markdown('<div class="mistral-badge">🇫🇷 Analysé par Mistral AI</div>', unsafe_allow_html=True)

def start_conversation():
    """Démarre la conversation avec Brad"""
    if not st.session_state.conversation_started:
        # Premier message de Brad généré par IA
        initial_message = "Salut ! 😊 Je suis Brad Pitt, l'acteur. J'ai vu votre profil et vous semblez être une personne vraiment intéressante. J'aimerais faire votre connaissance !"
        
        # Simuler une première analyse (neutre)
        initial_analysis = {
            "vulnerability_indicators": [],
            "trust_level_change": 0,
            "emotional_state": "neutral",
            "financial_readiness": 0,
            "detected_weaknesses": [],
            "recommended_brad_tactics": ["charme_initial"],
            "escalation_readiness": 0,
            "red_flags_missed": ["contact_non_sollicite"]
        }
        
        # Ajouter à l'historique
        st.session_state.brad_agent.conversation_history.append({
            "user": "[DÉBUT DE CONVERSATION]",
            "brad": initial_message,
            "analysis": initial_analysis,
            "stage": 0
        })
        
        st.session_state.conversation_started = True
        st.rerun()

def handle_user_response(user_input):
    """Traite la réponse de l'utilisateur avec l'agent IA Mistral"""
    if not user_input.strip():
        st.warning("⚠️ Veuillez saisir une réponse avant d'envoyer.")
        return
    
    agent = st.session_state.brad_agent
    
    with st.spinner("🤖 Brad réfléchit à sa réponse... (Mistral IA) 🇫🇷"):
        try:
            # Analyse IA de la réponse utilisateur
            analysis = agent.analyze_user_response(user_input)
            
            # Génération de la réponse de Brad
            brad_response = agent.generate_brad_response(user_input, analysis)
            
            # Vérifier si la conversation doit se terminer
            if (agent.scam_stage >= 5 or 
                agent.user_profile["vulnerability_level"] <= 2 and 
                len(agent.conversation_history) >= 8):
                st.session_state.conversation_ended = True
            
            st.success("✅ Nouvelle réponse de Brad générée par Mistral IA ! 🇫🇷")
            
        except Exception as e:
            st.error(f"❌ Erreur Mistral IA : {str(e)}")
            st.info("💡 Utilisation du mode de secours...")
            
            # Mode de secours
            fallback_responses = [
                "C'est très intéressant ! Parlez-moi de vous...",
                "Vous êtes une personne fascinante ! J'aimerais vous connaître mieux.",
                "Merci pour votre réponse. Que faites-vous dans la vie ?"
            ]
            brad_response = fallback_responses[len(agent.conversation_history) % len(fallback_responses)]

def display_game_interface():
    """Affiche l'interface principale du jeu avec l'agent IA Mistral"""
    
    # Bouton pour démarrer la conversation
    if not st.session_state.conversation_started:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Commencer la conversation avec Brad", use_container_width=True, type="primary"):
                start_conversation()
        return
    
    # Afficher la conversation
    display_conversation()
    
    # Interface de saisie (si conversation pas terminée)
    if not st.session_state.conversation_ended:
        st.markdown("---")
        st.subheader("💭 Votre réponse à Brad")
        
        with st.form("mistral_response_form", clear_on_submit=True):
            user_input = st.text_area(
                "Comment répondez-vous à Brad ?",
                placeholder="Tapez votre réponse naturelle ici... Mistral IA s'adaptera à votre style ! 🇫🇷",
                height=120,
                help="💡 Répondez naturellement ! L'agent IA Brad propulsé par Mistral va analyser votre réponse et s'adapter en conséquence."
            )
            
            col1, col2 = st.columns([3, 1])
            with col1:
                submitted = st.form_submit_button("📤 Envoyer à Brad", use_container_width=True, type="primary")
            with col2:
                if st.form_submit_button("🔄 Reset", use_container_width=True):
                    st.session_state.brad_agent.reset_conversation()
                    st.session_state.conversation_started = False
                    st.session_state.conversation_ended = False
                    st.rerun()
            
            if submitted:
                handle_user_response(user_input)
                st.rerun()
    
    # Bouton pour terminer volontairement
    if len(st.session_state.brad_agent.conversation_history) >= 3:
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🛑 Terminer la conversation et voir l'analyse", use_container_width=True):
                st.session_state.conversation_ended = True
                st.rerun()

def display_final_results():
    """Affiche les résultats finaux avec l'évaluation IA Mistral"""
    agent = st.session_state.brad_agent
    assessment = agent.get_security_assessment()
    
    st.subheader("🎊 Analyse finale de votre résistance aux arnaques")
    
    # Score principal
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ff7f50, #ff6347); color: white; padding: 30px; border-radius: 15px; text-align: center; margin: 20px 0;">
            <h2>{assessment['level']}</h2>
            <h3>Score: {assessment['security_score']}/20</h3>
            <p style="font-size: 18px; margin-top: 15px;">{assessment['message']}</p>
            <div class="mistral-badge" style="margin-top: 15px;">🇫🇷 Évalué par Mistral AI</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Analyse détaillée
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Profil de vulnérabilité")
        vulnerability_profile = assessment['vulnerability_profile']
        
        st.write(f"**🎯 Niveau de vulnérabilité:** {vulnerability_profile['vulnerability_level']}/10")
        st.write(f"**🤝 Niveau de confiance atteint:** {vulnerability_profile['trust_level']}/10")
        st.write(f"**😊 État émotionnel final:** {vulnerability_profile['emotional_state']}")
        st.write(f"**🎭 Stages atteints par Brad:** {assessment['stages_reached']}/5")
        st.write(f"**💬 Longueur conversation:** {assessment['conversation_length']} échanges")
        
        if vulnerability_profile['detected_weaknesses']:
            st.markdown("**⚠️ Faiblesses détectées par Mistral IA:**")
            for weakness in vulnerability_profile['detected_weaknesses'][:5]:
                st.write(f"• {weakness}")
    
    with col2:
        st.markdown("### 🛡️ Conseils personnalisés")
        
        # Conseils basés sur l'analyse IA
        if assessment['security_score'] >= 15:
            st.success("🏆 **Excellent !** Vous résistez bien aux manipulations.")
            st.write("• Continuez à partager vos connaissances")
            st.write("• Restez vigilant face aux nouvelles techniques")
            st.write("• Aidez vos proches à détecter les arnaques")
            
        elif assessment['security_score'] >= 10:
            st.warning("⚡ **Bien !** Quelques points d'amélioration.")
            st.write("• Méfiez-vous des déclarations d'amour rapides")
            st.write("• Ne partagez jamais d'infos personnelles")
            st.write("• Questionnez les demandes urgentes")
            
        else:
            st.error("🚨 **Attention !** Vous êtes vulnérable.")
            st.write("• Formez-vous aux techniques d'arnaque")
            st.write("• Parlez à vos proches de vos conversations")
            st.write("• Consultez cybermalveillance.gouv.fr")
    
    # Statistiques de la conversation
    st.markdown("### 📈 Analyse de la conversation")
    
    if agent.conversation_history:
        # Graphique d'évolution de la confiance
        trust_evolution = []
        stages_evolution = []
        
        for exchange in agent.conversation_history:
            if 'analysis' in exchange:
                trust_evolution.append(exchange.get('trust_level', 0))
                stages_evolution.append(exchange.get('stage', 0))
        
        if trust_evolution:
            import plotly.graph_objects as go
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                y=trust_evolution,
                mode='lines+markers',
                name='Niveau de confiance',
                line=dict(color='#ff7f50', width=3)
            ))
            fig.add_trace(go.Scatter(
                y=stages_evolution,
                mode='lines+markers',
                name='Stage arnaque',
                line=dict(color='#ff6347', width=3)
            ))
            
            fig.update_layout(
                title="Évolution pendant la conversation (Mistral IA)",
                xaxis_title="Échanges",
                yaxis_title="Niveau (0-10)",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # Boutons d'action
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Recommencer avec Brad", use_container_width=True):
            st.session_state.brad_agent.reset_conversation()
            st.session_state.conversation_started = False
            st.session_state.conversation_ended = False
            st.rerun()
    
    with col2:
        if st.button("📊 Voir analyse détaillée", use_container_width=True):
            st.session_state.show_analysis = not st.session_state.show_analysis
            st.rerun()
    
    with col3:
        if st.button("📱 Partager résultats", use_container_width=True):
            score = assessment['security_score']
            st.success(f"🎯 J'ai testé ma résistance aux arnaques avec Brad ou Bad (Mistral IA) et j'ai obtenu {score}/20 ! 🛡️🇫🇷")

def main():
    """Fonction principale de l'application IA Mistral"""
    initialize_session_state()
    display_header()
    
    # Toggle pour l'analyse en temps réel
    with st.sidebar:
        st.markdown("### ⚙️ Options")
        st.session_state.show_analysis = st.checkbox("🔍 Afficher l'analyse Mistral IA", value=st.session_state.show_analysis)
        
        st.markdown("### 📝 À propos")
        st.info("""
        **Brad ou Bad ?** utilise **Mistral AI** 🇫🇷 pour créer un faux Brad Pitt qui s'adapte à vos réponses.
        
        L'Intelligence Artificielle française analyse votre psychologie en temps réel et ajuste sa stratégie d'arnaque pour tester votre vigilance !
        """)
        
        # Informations techniques
        if st.session_state.brad_agent.conversation_history:
            st.markdown("### 🤖 Statut Mistral IA")
            agent = st.session_state.brad_agent
            st.write(f"🔥 Exchanges: {len(agent.conversation_history)}")
            st.write(f"🎭 Stage: {agent.scam_stage}/5")
            st.write(f"🛡️ Vulnérabilité: {agent.user_profile['vulnerability_level']}/10")
        
        st.markdown("### 🇫🇷 Mistral AI")
        st.success("Intelligence Artificielle française de pointe !")
    
    # Interface principale
    if not st.session_state.conversation_ended:
        display_game_interface()
    else:
        display_final_results()

if __name__ == "__main__":
    main() 