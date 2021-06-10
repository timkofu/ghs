test:
	@poetry run dmypy run -- ghs --strict --allow-untyped-decorators
	@poetry run pytest --timeout=3

dev_server:
	@uvicorn ghs.view.web.endpoints:app --host 127.0.0.1 --port 8008 --loop uvloop --http httptools --interface asgi3 --log-level info --reload

.PHONY: doc
doc:
	@poetry run pdoc --force --html --output-dir doc --config show_source_code=False ghs > /dev/null

deploy: test doc
