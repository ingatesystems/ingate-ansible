GALAXY        := galaxy.yml
.DEFAULT_GOAL := build

$(eval VERSION := $(shell grep version: $(GALAXY) | \
	awk '{ print $$2 }'))

build:
	ansible-galaxy collection build --force

check: build
	ansible-test sanity --docker default -v
	ansible-test units --docker default -v

install: build
	ansible-galaxy collection install \
		ingatesystems-fuego_modules-$(VERSION).tar.gz --force

html: build install
	[ -d docs/html ] && rm -rf docs/html
	mkdir -p docs/html
	(cd docs && ./build.sh)

clean:
	$(RM) ingatesystems-fuego_modules-$(VERSION).tar.gz
	$(RM) -rf docs/build
	$(RM) -rf docs/rst
	$(RM) -rf docs/temp-rst

all: clean check build install html
