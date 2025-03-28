# Files and directories
MAIN_FILE = src/main.py
PRESETS = ./presets

# Commands
INTEGRAL_FROM_JSON = integral-from-json
INTEGRAL = integral

.DEFAULT_GOAL:=help
.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: rectangle-json
rectangle-json: # Run rectangle method from json
	python3 $(MAIN_FILE) $(INTEGRAL_FROM_JSON) $(PRESETS)/rectangle.json

.PHONY: trapezoid-json
trapezoid-json: # Run trapezoid method from json
	python3 $(MAIN_FILE) $(INTEGRAL_FROM_JSON) $(PRESETS)/trapezoid.json

.PHONY: simpson-json
simpson-json: # Run Simpson method from json
	python3 $(MAIN_FILE) $(INTEGRAL_FROM_JSON) $(PRESETS)/trapezoid.json

.PHONY: discontinuity-json
discontinuity-json: # Try evaluating integral with discontinuity
	python3 $(MAIN_FILE) $(INTEGRAL_FROM_JSON) $(PRESETS)/discontinuity.json

.PHONY: console-help
console-help: # Run help for `integral` command that accepts params from console
	python3 $(MAIN_FILE) $(INTEGRAL) --help