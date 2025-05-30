# Configuration des Clés API - Brad ou Bad

## 🔐 Variables d'Environnement Requises

Ce projet nécessite des clés API pour fonctionner. Pour des raisons de sécurité, les clés API ne sont **plus** stockées directement dans le code.

### Variables requises :

1. **OPENAI_API_KEY** : Clé API OpenAI pour les fonctionnalités IA principales
2. **MISTRAL_API_KEY** : Clé API Mistral (optionnelle, pour la version Mistral)

## 🚀 Configuration sur différents systèmes

### Windows (PowerShell)
```powershell
# Temporaire (session actuelle)
$env:OPENAI_API_KEY="votre_clé_openai_ici"
$env:MISTRAL_API_KEY="votre_clé_mistral_ici"

# Permanent (profil PowerShell)
echo '$env:OPENAI_API_KEY="votre_clé_openai_ici"' >> $PROFILE
echo '$env:MISTRAL_API_KEY="votre_clé_mistral_ici"' >> $PROFILE
```

### Windows (Command Prompt)
```cmd
set OPENAI_API_KEY=votre_clé_openai_ici
set MISTRAL_API_KEY=votre_clé_mistral_ici
```

### Linux/macOS (Bash/Zsh)
```bash
# Temporaire (session actuelle)
export OPENAI_API_KEY="votre_clé_openai_ici"
export MISTRAL_API_KEY="votre_clé_mistral_ici"

# Permanent (.bashrc ou .zshrc)
echo 'export OPENAI_API_KEY="votre_clé_openai_ici"' >> ~/.bashrc
echo 'export MISTRAL_API_KEY="votre_clé_mistral_ici"' >> ~/.bashrc
source ~/.bashrc
```

### Fichier .env (recommandé)
1. Créez un fichier `.env` à la racine du projet :
```bash
# .env
OPENAI_API_KEY=sk-proj-votre_clé_openai_complète_ici
MISTRAL_API_KEY=votre_clé_mistral_ici
```

2. Le fichier `.env` est automatiquement ignoré par Git (.gitignore)

## 🔑 Obtenir les clés API

### OpenAI
1. Visitez [platform.openai.com](https://platform.openai.com/)
2. Connectez-vous ou créez un compte
3. Allez dans "API Keys" dans le menu
4. Cliquez sur "Create new secret key"
5. Copiez la clé (commence par `sk-`)

### Mistral AI
1. Visitez [console.mistral.ai](https://console.mistral.ai/)
2. Connectez-vous ou créez un compte
3. Allez dans "API Keys"
4. Créez une nouvelle clé
5. Copiez la clé

## ⚠️ Sécurité

- **JAMAIS** de clé API dans le code source
- **JAMAIS** de commit avec des clés API
- Utilisez des variables d'environnement ou fichiers .env
- Régénérez vos clés si elles sont compromises

## 🧪 Test de Configuration

Après configuration, testez avec :
```bash
python check_openai_key.py
python test_api_debug.py
```

## 🔧 Dépannage

Si vous obtenez l'erreur "Clé API manquante" :
1. Vérifiez que la variable d'environnement est définie
2. Redémarrez votre terminal/IDE
3. Vérifiez l'orthographe de la variable
4. Assurez-vous qu'il n'y a pas d'espaces dans la clé

### Vérifier les variables d'environnement :
```bash
# Windows (PowerShell)
echo $env:OPENAI_API_KEY

# Linux/macOS
echo $OPENAI_API_KEY
```

## 📞 Support

Si vous continuez à avoir des problèmes :
1. Consultez la documentation OpenAI/Mistral
2. Vérifiez les quotas et la facturation
3. Contactez le support technique des providers 