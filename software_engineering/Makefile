
SLIDES = 0_Introduction 1_Project 2_Distribution 3_Virtualenv 4_Test 5_Documentation

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

build/html/%.html: %/index.rst png
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

build/pdf/%.pdf: %/index.rst
	@mkdir -p build/pdf
	cd $(dir $<);landslide -d ../$@ index.rst

html: $(patsubst %,build/html/%.html, $(SLIDES))

build/pdf/slides.pdf: $(patsubst %,build/pdf/%.pdf, $(SLIDES))
	pdfunite $^ $@

pdf: build/pdf/slides.pdf

#
# CLEAN
#

clean:
	@rm -rf build
