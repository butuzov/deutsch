help:
	@echo "===================================================================="
	@echo " Makefile: github.com/butuzov/deadlinks - rountine tasks automation "
	@echo "===================================================================="
	@echo ""
	@cat $(MAKEFILE_LIST) | \
		grep -E '^# ~~~ .*? [~]+$$|^[a-zA-Z0-9_-]+:.*?## .*$$' | \
		awk '{if ( $$1=="#" ) {\
			match($$0, /^# ~~~ (.+?) [~]+$$/, a);\
			{print "\n", a[1], "\n"}\
		} else { \
			match($$0, /^([a-zA-Z-]+):.*?## (.*)$$/, a); \
			{printf "  - \033[32m%-20s\033[0m %s\n",   a[1], a[2]} \
		};}'
	@echo ""

venv:
	@if [ -z "${VIRTUAL_ENV}" ]; then\
		echo ">>>>> You need to run this test in virtual environment. Abort!";\
		exit 1;\
	fi

install: venv ## Installs Reqired Packages
	python3 -m pip install yapf pylint pytest -q
	python3 -m pip slovo easydecks -q
	python3 -m pip install -e .

