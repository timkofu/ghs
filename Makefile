test:
	@poetry run dmypy run -- ghs tests --strict --namespace-packages --allow-untyped-decorators --follow-imports=skip  # type-check only my code
	@poetry run pytest
