test:
	@poetry run dmypy run -- ghs tests --strict
	@poetry run pytest --timeout=3

dev_server:
	@uvicorn ghs.view.web.endpoints:app --host 127.0.0.1 --port 8008 --loop uvloop --http httptools --interface asgi3 --log-level info --reload
