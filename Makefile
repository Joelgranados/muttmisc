
BUILDDIR = build

.PHONY: ical_to_todoist dump_ical

all: ical_to_todoist dump_ical

dir:
	mkdir -p $(BUILDDIR)

ical_to_todoist: dir
	shiv -c $@ -o ./$(BUILDDIR)/$@ .

dump_ical: dir
	shiv -c $@ -o ./$(BUILDDIR)/$@ .
