test:
	@poetry run dmypy run -- ghs tests --strict --namespace-packages --allow-untyped-decorators --follow-imports=skip  # dont typecheck 3rd party libs
	@poetry run pytest --timeout=3

dev_server:
	@uvicorn ghs.view.web.endpoints:app --host 127.0.0.1 --port 8008 --http httptools --interface asgi3 --log-level info --reload
