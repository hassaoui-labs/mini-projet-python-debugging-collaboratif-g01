## 📁 Structure du projet

```
mini-projet-python-debugging-collaboratif-g01/
│
├── src/                          # Code source
│   ├── __init__.py
│   ├── execution_engine.py       # ✅ Module 1 - Moteur d'exécution (Sofiane)
│   ├── debugger.py               # ⏳ Module 2 - Debugging (Membre 2)
│   ├── collaboration.py          # ⏳ Module 3 - Collaboration (Membre 3)
│   └── utils.py                  # Utilitaires communs
│
├── tests/                        # Tests unitaires
│   ├── __init__.py
│   ├── test_execution_engine.py  # ✅ Tests module 1
│   ├── test_debugger.py          # ⏳ Tests module 2
│   └── test_collaboration.py     # ⏳ Tests module 3
│
├── docs/                         # Documentation
│   ├── execution_engine_doc.md   # ✅ Doc module 1
│   ├── debugger_doc.md           # ⏳ Doc module 2
│   └── collaboration_doc.md      # ⏳ Doc module 3
│
├── examples/                     # Exemples d'utilisation
│   └── example_usage.py          # ✅ Démonstrations
│
├── logs/                         # Fichiers de logs
│   └── .gitkeep
│
├── .gitignore                    # Fichiers à ignorer
├── requirements.txt              # Dépendances Python
├── README.md                     # Ce fichier
└── CONTRIBUTING.md               # Guide de contribution
```
### Étapes d'installation

```bash
# 1. Cloner le repository
git clone https://github.com/[superviseur]/mini-projet-python-debugging-collaboratif-g01.git
cd mini-projet-python-debugging-collaboratif-g01

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv

# 3. Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur Linux/Mac:
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Vérifier l'installation
python -c "from src.execution_engine import ExecutionEngine; print('✓ Installation réussie!')"
```

---

## 💻 Utilisation

### Exemple rapide - Module 1 (Moteur d'exécution)

```python
from src.execution_engine import ExecutionEngine

# Créer une instance
engine = ExecutionEngine(timeout=10, max_memory_mb=100)

# Exécuter du code
code = """
print("Hello World!")
x = 10 + 20
print(f"Résultat: {x}")
"""

result = engine.execute_code(code)

# Afficher le résultat
if result['success']:
    print("✓ Exécution réussie!")
    print(result['output'])
else:
    print("✗ Erreur:", result['error'])
```

### Lancer les tests

```bash
# Tous les tests
pytest tests/ -v

# Tests avec couverture de code
pytest tests/ --cov=src --cov-report=html

# Tests d'un module spécifique
pytest tests/test_execution_engine.py -v
```

### Lancer les exemples

```bash
# Démonstration du moteur d'exécution
python examples/example_usage.py

# Démonstration basique
python src/execution_engine.py
```

---
