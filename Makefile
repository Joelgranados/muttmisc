BUILDDIR = build
.DEFAULT_GOAL := help
.PHONY: help ical_to_todoist dump_ical

help: ## Output this help
	@echo "\033[33mAvailable targets, for more information, see \033[36mREADME.md\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: ical_to_todoist dump_ical ## Create all executables

dir:
	mkdir -p $(BUILDDIR)

ical_to_todoist: dir ## Create the calendar to todoist executable
	shiv -c $@ -o ./$(BUILDDIR)/$@ .

dump_ical: dir ## Create the ical to text executable
	shiv -c $@ -o ./$(BUILDDIR)/$@ .
