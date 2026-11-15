.PHONY: setup setup-api setup-web dev dev-api dev-web test lint check

setup:
	npm run setup

setup-api:
	npm run setup:api

setup-web:
	npm run setup:web

dev:
	npm run dev

dev-api:
	npm run dev:api

dev-web:
	npm run dev:web

test:
	npm test

lint:
	npm run lint

check:
	npm run check
