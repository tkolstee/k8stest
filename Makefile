SUBDIRS=flask-app rabbit-consumer redis rabbitmq

build:
	for x in ${SUBDIRS}; do cd ${x}; make build; cd -; done

push: build
	for x in ${SUBDIRS}; do cd ${x}; make push; cd -; done

deploy:
	for x in ${SUBDIRS}; do cd ${x}; make deploy; cd -; done
