build:
	docker build -t tkolstee/sample-flask-app:latest src

push:  build
	docker push tkolstee/sample-flask-app:latest

deploy:
	kubectl apply -f k8s/deploy.yaml

