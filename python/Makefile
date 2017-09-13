

PNGS_FROM_SVGS=$(shell find | grep \\.svg | sed -e 's/svg$$/png/g')

.PHONY: clean html pdf png

%.png: %.svg
	inkscape -z $< -e $@

png: $(PNGS_FROM_SVGS)

#
# HTML
#

build/html/%.html: %/index.rst
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

html: build/html/python.html build/html/numpy.html build/html/io.html

#
# PDF
#

build/pdf/%.pdf: build/html/%.html
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

build/pdf/slides.pdf: build/html/python.html build/html/numpy.html build/html/io.html
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

pdf: build/pdf/slides.pdf

#
# CLEAN
#

clean:
	@rm -rf build
