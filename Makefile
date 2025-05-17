DOCKER_BUILDS=flask-app rabbit-consumer
K8S_DEPLOYMENTS=consumer flask-app rabbitmq redis

build:
	for x in ${DOCKER_BUILDS}; do docker build -t docker.io/tkolstee/sample-$${x} $${x}; done

push: build
	for x in ${DOCKER_BUILDS}; do docker push docker.io/tkolstee/sample-$${x}; done

deploy:
	for x in ${K8S_DEPLOYMENTS}; do kubectl apply -f k8s-resources/$${x}.yaml; done
