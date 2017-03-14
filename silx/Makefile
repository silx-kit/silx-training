
SLIDES = introduction io plot processing conclusion

PNGS_FROM_SVGS=$(shell find | grep \\.svg | sed -e 's/svg$$/png/g')

.PHONY: clean html pdf png

%.png: %.svg
	inkscape -z $< -e $@

build/html/%.html: %/index.rst png
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

build/pdf/%.pdf: %/index.rst
	@mkdir -p build/pdf
	cd $(dir $<);landslide -d ../$@ index.rst

png: $(PNGS_FROM_SVGS)

html: $(patsubst %,build/html/%.html, $(SLIDES))

build/pdf/slides.pdf: $(patsubst %,build/pdf/%.pdf, $(SLIDES))
	pdfunite $^ $@

pdf: build/pdf/slides.pdf

clean:
	@rm -rf build
