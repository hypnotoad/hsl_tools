user = $(shell id --user):$(shell id --group)
hslfile = $(number)_$(name).hsl
hslzfile = $(number)_$(name).hslz
helpfile = doc/log$(number).html


python = docker run --user ${user} --volume "$(shell pwd):/project" --workdir /project lindra.de/gira_hsl3 /usr/bin/python3


.PHONY: clean default

ifdef BUILD_HSLZ
default: $(hslzfile)
else
default: $(hslfile)
endif

$(hslfile): config.json *.py
	$(python) /hsl/generator.pyc --source config.json --target "$@" --debug

$(hslzfile): $(hslfile) $(helpfile)
	zip --filesync --recurse-paths $@ $(hslfile) $(number)
	zip --junk-paths $@ $(helpfile)

clean:
	rm -f "$(hslfile)"


