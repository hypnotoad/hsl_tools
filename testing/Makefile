install_dir = $(shell python3 -c "import site; print(site.getusersitepackages())")/hsl3

install: *.py
	mkdir -p $(install_dir)
	install --target-directory $(install_dir) $^
