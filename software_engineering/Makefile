
SLIDES = 0_Introduction 1_Architecture 2_Git 3_Distribution 4_Virtualenv 5_Test 6_Documentation

PNGS_FROM_SVGS=$(shell find | grep \\.svg | sed -e 's/svg$$/png/g')

.PHONY: clean html pdf png

#
# RESOURCES
#

%.png: %.svg
	inkscape -z $< -e $@

png: $(PNGS_FROM_SVGS)

#
# SLIDES
#

build/html/%.html: %/notebook.ipynb
	@mkdir -p build/html
	cd $(dir $<);jupyter nbconvert --to html notebook.ipynb --output=../$@

build/html/%.html: %/index.rst png
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

html: $(patsubst %,build/html/%.html, $(SLIDES))

build/pdf/%.pdf: build/html/%.html
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

build/pdf/slides.pdf: $(patsubst %,build/html/%.html, $(SLIDES))
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

pdf: build/pdf/slides.pdf

#
# CLEAN
#

clean:
	@rm -rf build
