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

clean:
	$(RM) ingatesystems-fuego_modules-$(VERSION).tar.gz

all: clean check build install
