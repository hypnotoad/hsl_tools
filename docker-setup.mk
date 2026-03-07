user = $(shell id --user):$(shell id --group)
hslfile = $(number)_$(name).hsl

python = docker run --user ${user} --volume "$(shell pwd):/project" --workdir /project lindra/hsl3 /usr/bin/python3


.PHONY: clean default

default: $(hslfile)

$(hslfile): config.json *.py
	$(python) /hsl/generator.pyc --source config.json --target "$@" --debug

$(hslfile).zip: $(hslfile)
	zip "$@" "$^"

clean:
	rm -f "$(hslfile)"


