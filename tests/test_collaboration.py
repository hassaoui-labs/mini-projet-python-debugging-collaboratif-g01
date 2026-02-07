import pytest
from src.collaboration import CollaborationManager

@pytest.fixture
def manager():
    return CollaborationManager()

def test_register_collaborator(manager):
    users = manager.register_collaborator("Sofiane")
    assert "Sofiane" in users
    assert len(users) == 1

def test_log_correction(manager):
    manager.register_collaborator("Ilyes")
    fix = manager.log_correction("Ilyes", "SyntaxError", "Ajout de deux-points")
    assert fix["user"] == "Ilyes"
    assert fix["error_fixed"] == "SyntaxError"
    assert len(manager.correction_history) == 1

def test_session_summary(manager):
    manager.register_collaborator("Faical")
    manager.log_correction("Faical", "NameError", "Variable définie")
    summary = manager.get_session_summary()
    assert summary["total_collaborators"] == 1
    assert summary["total_fixes"] == 1
    assert "Membre2" in manager.format_collab_report()
