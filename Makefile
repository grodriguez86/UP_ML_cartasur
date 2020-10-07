install_osx_pip:
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
	python3 get-pip.py && \
	rm get-pip.py

install_osx: install_osx_pip install

install:
	pip install \
		--use-feature=2020-resolver \
		-r requirements_osx.txt

run:
	python3 work.py
