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
### Règles de base

1. **Créer une branche** pour chaque nouvelle fonctionnalité
2. **Écrire des tests** pour le nouveau code
3. **Documenter** les fonctions et modules
4. **Faire des commits atomiques** avec des messages clairs
5. **Créer une Pull Request** pour review


---
