.PHONY: help

help:
	@echo "I am here"


commit:
	git commit -am"${MESSAGE}"

push:
	git push origin main


bootstrap-init:
	python3.9 -m venv myenv/${APP_NAME}
	myenv/${APP_NAME}/bin/pip3.9 install -U pip setuptools wheel

bootstrap-100:
	@make bootstrap-init APP_NAME=venv100
	myenv/venv100/bin/pip3.9 install -r 100_days_of_code/req_100doc.txt

black100:
	myenv/venv100/bin/black 100_days_of_code/


