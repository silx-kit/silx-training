

PNGS_FROM_SVGS=$(shell find | grep \\.svg | sed -e 's/svg$$/png/g')

.PHONY: clean html pdf png

%.png: %.svg
	inkscape -z $< -e $@

build/html/%.html: %/index.rst
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

build/pdf/%.pdf: %/index.rst
	@mkdir -p build/pdf
	cd $(dir $<);landslide -d ../$@ index.rst

png: $(PNGS_FROM_SVGS)

html: build/html/io.html

build/pdf/slides.pdf: build/pdf/io.pdf
	pdfunite $^ $@

pdf: build/pdf/slides.pdf

clean:
	@rm -rf build
