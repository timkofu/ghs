test:
	@poetry run dmypy run -- ghs tests --strict --namespace-packages --allow-untyped-decorators --follow-imports=skip  # dont typecheck 3rd party libs
	@poetry run pytest
