test:
	@poetry run dmypy run -- ghs tests --strict --namespace-packages --allow-untyped-decorators
	@poetry run pytest
