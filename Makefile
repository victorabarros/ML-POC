APP_NAME?=machLearnPoc
APP_DIR = /src/${APP_NAME}
PWD=$(shell pwd)
IMAGE?=python
COMMAND?=bash

YELLOW=$(shell printf '\033[0;1;33m')
COLOR_OFF=$(shell printf '\033[0;1;0m')

container-clean-up:
	@docker rm -f ${APP_NAME}

container-debug:
	@echo "${YELLOW}Debug Mode${COLOR_OFF}"
	@docker run -it \
		--env-file .env \
		-v ${PWD}:${APP_DIR} \
		-w ${APP_DIR} \
		--rm --name ${APP_NAME} ${IMAGE} ${COMMAND}
