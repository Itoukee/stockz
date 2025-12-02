.PHONY: test test-unit test-int test-ci up-test-db

# Lancer la DB de test
up-test-db:
	docker compose -f docker-compose.test.yml up -d

# Tests unitaires
test-unit:
	pytest tests/unit -q

# Tests d’intégration
test-int:
	pytest tests/integration -q

# Tous les tests
test:
	pytest -q

# Utilisé en CI (lance la DB, puis les tests)
test-ci: up-test-db
	pytest -q