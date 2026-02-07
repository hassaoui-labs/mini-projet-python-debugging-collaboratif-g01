# Mini-projet-python-debugging-collaboratif-g01

📌 Contexte : 
Mini-projet collaboratif réalisé dans le cadre du Doctorat – Troisième Cycle, visant à approfondir les techniques de debugging Python et le travail collaboratif à l’aide des outils DevOps.

🎯 Objectifs pédagogiques : 
- Maîtriser le debugging avancé en Python
- Identifier, analyser et corriger des erreurs complexes
- Travailler efficacement en équipe via Git/GitHub
- Utiliser des outils collaboratifs (cloud, Live Share)

🧩 Description du projet : 
Développer une plateforme permettant aux utilisateurs de soumettre du code Python, de détecter automatiquement les erreurs, de visualiser les logs et de collaborer à la correction du code.

⚙️ Fonctionnalités attendues : 
+ Exécution sécurisée de scripts Python
+ Capture et analyse des exceptions
+ Génération de logs détaillés
+ Correction collaborative du code
+ Historique des erreurs et corrections

🛠️ Technologies à utiliser : 
    - Python
    - Git / GitHub
    - Google Colab
    - Visual Studio Live Share

👥 Répartition du travail (suggestion) : 
- Membre 1 : moteur d’exécution
- Membre 2 : module de debugging
- Membre 3 : collaboration temps réel
- Membre 4 : documentation & gestion GitHub

📦 Livrables attendus : 
         - Dépôt GitHub structuré (Code source versionné)
         - Wiki Documentation projet 
         - Rapport technique PDF
         - Journal de commits



## 📚 Documentation

- **[Module 1 - Moteur d'Exécution](docs/1-Documantation-Execution_engine.md)** ✅
- **[Module 2 - Debugger](docs/debugger_doc.md)** ⏳
- **[Module 3 - Collaboration](docs/collaboration_doc.md)** ⏳
- **[Guide de contribution](CONTRIBUTING.md)** ⏳


---

## 🔄 Workflow Git

### Pour commencer à travailler

```bash
# 1. Créer une branche pour votre fonctionnalité
git checkout -b feature/nom-fonctionnalite

# 2. Faire vos modifications
# ... coder ...

# 3. Ajouter les fichiers modifiés
git add .

# 4. Commit avec un message descriptif
git commit -m "feat: ajout de la fonctionnalité X"

# 5. Pousser vers GitHub
git push origin feature/nom-fonctionnalite

# 6. Créer une Pull Request sur GitHub
```

### Convention de nommage des commits

- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `test:` Ajout/modification de tests
- `refactor:` Refactorisation du code
- `style:` Formatage, indentation

---

## 🧪 Tests et qualité du code

```bash
# Lancer tous les tests
pytest tests/ -v

# Tests avec couverture
pytest tests/ --cov=src --cov-report=term-missing

# Générer un rapport HTML de couverture
pytest tests/ --cov=src --cov-report=html
# Puis ouvrir: htmlcov/index.html

# Vérifier le style de code (PEP 8)
flake8 src/ tests/
```

---

## 📦 Livrables attendus

- [x] ✅ **Dépôt GitHub structuré** (avec branches, commits réguliers)
- [x] ✅ **Code source versionné** (Module 1 complété)
- [ ] ⏳ **Wiki / Documentation projet**
- [ ] ⏳ **Rapport technique PDF**
- [ ] ⏳ **Journal de commits détaillé**

---
### Règles de base

1. **Créer une branche** pour chaque nouvelle fonctionnalité
2. **Écrire des tests** pour le nouveau code
3. **Documenter** les fonctions et modules
4. **Faire des commits atomiques** avec des messages clairs
5. **Créer une Pull Request** pour review

---

## 📊 Progression du projet

| Module | Progression | Dernière mise à jour |
|--------|------------|---------------------|
| Moteur d'exécution | ████████████ 100% | 28/01/2026 - Sofiane |
| Module debugging | ░░░░░░░░░░░░ 0% | - |
| Collaboration | ░░░░░░░░░░░░ 0% | - |
| Documentation | ████░░░░░░░░ 33% | 26/02/2026 |

---

## 📝 Changelog

### [Version 0.1.0] - 07/02/2026

#### Ajouté (par Sofiane)
- ✅ Moteur d'exécution sécurisé complet
- ✅ Gestion des exceptions et timeout
- ✅ Monitoring mémoire et temps d'exécution
- ✅ Historique et statistiques
- ✅ Tests unitaires (8 tests, 100% couverture)
- ✅ Documentation complète
- ✅ Exemples d'utilisation

---

## 👨‍🎓 Équipe

- **Sofiane** - Module 1: Moteur d'exécution ✅
- **Faiçal** - Module 2: Debugging ⏳
- **Ilyes** - Module 3: Collaboration ⏳
- **Abderrahmane** - Documentation & GitHub ⏳

---

**Dernière mise à jour:** 07/02/2026 par Abderrahmane  
**Projet:** Mini-projet Python Debugging Collaboratif - G01  
