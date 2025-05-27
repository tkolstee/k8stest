SUBDIRS=flask-app rabbit-consumer redis rabbitmq

build:
	for x in ${SUBDIRS}; do make build -C $${x}; done

push: build
	for x in ${SUBDIRS}; do make push -C $${x}; done

deploy:
	for x in ${SUBDIRS}; do make deploy -C $${x}; done
