# 🎭 Brad ou Bad ? - Le Coach IA anti-brouteur

Une application éducative interactive pour sensibiliser aux arnaques sentimentales en ligne.

## 🎯 Objectif

"Brad ou Bad ?" est un simulateur ludique qui vous met face à un faux Brad Pitt tentant de vous manipuler par des messages de plus en plus suspects. L'objectif est d'apprendre à détecter les signaux d'alarme des arnaques sentimentales (romance scams) dans un environnement sécurisé.

## 🛠️ Technologies utilisées

- **Python 3.8+**
- **Streamlit** pour l'interface web interactive
- **Analyse de sentiment** basée sur des mots-clés
- **Système de scoring** pour évaluer la vigilance

## 📦 Installation

1. **Cloner le repository :**
   ```bash
   git clone [votre-repo]
   cd BradOrBad
   ```

2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application :**
   ```bash
   streamlit run main.py
   ```

4. **Ouvrir votre navigateur :** L'application se lance automatiquement sur `http://localhost:8501`

## 🎮 Comment jouer

1. **Lisez le message de "Brad"** qui apparaît dans l'interface
2. **Répondez** comme vous le feriez naturellement dans une vraie conversation
3. **Recevez un feedback** de notre Coach IA sur votre niveau de vigilance
4. **Progressez** à travers 5 étapes de difficulté croissante
5. **Découvrez votre score final** et vos recommandations personnalisées

## 🚩 Les 5 étapes du piège

1. **Contact initial** - Brad se présente comme acteur
2. **Demande d'infos** - Il veut votre numéro de téléphone
3. **Manipulation émotionnelle** - Déclaration d'amour rapide
4. **Première demande d'argent** - "Problème bancaire" urgent
5. **Escalade** - Chantage émotionnel et montants élevés

## 🧠 Système de scoring

- **Réponses vigilantes** : +3 à +7 points
- **Pose de limites** : +3 à +6 points  
- **Réponses naïves** : -1 à -5 points
- **Bonus questions** : +1 point (curiosité = bon réflexe)
- **Bonus détection argent** : +2 points (étapes 4-5)

## 📊 Évaluation finale

- **20+ points** : Expert en cybersécurité 🏆
- **15-19 points** : Très vigilant 🛡️
- **8-14 points** : Vigilance correcte ⚡
- **3-7 points** : Vigilance insuffisante ⚠️
- **0-2 points** : Forte vulnérabilité 🚨

## 🛡️ Conseils de cybersécurité intégrés

L'application fournit des conseils pratiques :
- Vérification d'identité des contacts non sollicités
- Protection des données personnelles
- Reconnaissance des techniques de manipulation
- Signalement des tentatives d'arnaque

## 📁 Structure du projet

```
BradOrBad/
├── main.py              # Interface Streamlit principale
├── scenarios.py         # Scénarios de Brad et conseils sécurité
├── evaluator.py         # Analyse des réponses et scoring
├── requirements.txt     # Dépendances Python
└── README.md           # Documentation
```

## 🎨 Fonctionnalités

### Interface utilisateur
- Chat en temps réel avec messages stylés
- Barre de progression visuelle
- Métriques en temps réel (score, étape, niveau de danger)
- Design responsive et moderne

### Analyse intelligente
- Détection de mots-clés suspects/vigilants
- Analyse de la longueur des réponses
- Bonus pour les questions (signe de réflexion)
- Scoring adaptatif selon l'étape

### Contenu éducatif
- 10 conseils de cybersécurité essentiels
- Statistiques réelles sur les arnaques sentimentales
- Signaux d'alarme organisés par catégorie
- Ressources pour aller plus loin

## 🔧 Personnalisation

### Ajouter de nouveaux scénarios
Modifiez le fichier `scenarios.py` pour ajouter des étapes :

```python
{
    "step": 5,
    "category": "nouvelle_categorie",
    "suspicion_level": 6,
    "message": "Votre nouveau message de Brad...",
    "red_flags": ["Nouveau signal d'alarme"],
    "expected_response_types": ["type1", "type2"]
}
```

### Modifier le système de scoring
Ajustez les scores dans `evaluator.py` :

```python
base_scores = {
    0: {"suspicious": 5, "boundary": 3, "naive": -1, "neutral": 1},
    # Modifiez selon vos besoins
}
```

## 🎓 Utilisation éducative

Cette application est parfaite pour :
- **Formations en cybersécurité** dans les entreprises
- **Ateliers de sensibilisation** pour le grand public
- **Cours d'éducation numérique** dans les établissements scolaires
- **Campagnes de prévention** des services publics

## ⚠️ Avertissements

- Cette application est **purement éducative**
- Aucune vraie demande d'argent ou d'informations personnelles
- Les scénarios sont **fictifs** et exagérés pour l'apprentissage
- **Respectueux** des vraies victimes d'arnaques

## 🤝 Contribution

Les contributions sont bienvenues ! Vous pouvez :
- Ajouter de nouveaux scénarios
- Améliorer l'analyse de sentiment
- Traduire l'interface
- Ajouter des statistiques réelles
- Créer des tests automatisés

## 📞 Ressources utiles

- **cybermalveillance.gouv.fr** - Signalement officiel
- **Info Escroqueries** : 0 805 805 817
- **Guide ANSSI** sur les arnaques en ligne

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

**⚡ Prêt à tester votre vigilance ? Lancez l'application et découvrez si vous êtes "Brad-proof" !** 