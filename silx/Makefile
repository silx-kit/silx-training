
SLIDES = introduction io plot gui processing conclusion

PNGS_FROM_SVGS=$(shell find | grep \\.svg | sed -e 's/svg$$/png/g')

NOTEBOOK_V3_FROM_NOTEBOOK=$(shell find | grep '\.ipynb$$' | grep -v '\.v3\.' | grep -v '\.ipynb_checkpoints' | sed -e 's/ipynb$$/v3.ipynb/g')


.PHONY: clean html pdf png notebook_v3

#
# RESOURCES
#

%.png: %.svg
	inkscape -z $< -e $@

png: $(PNGS_FROM_SVGS)

#
# HTML
#

build/html/%.html: %/index.rst png
	@mkdir -p build/html
	cd $(dir $<);landslide --embed -d ../$@ index.rst

html: $(patsubst %,build/html/%.html, $(SLIDES))

#
# PDF
#

build/pdf/%.pdf: build/html/%.html
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

build/pdf/slides.pdf: $(patsubst %,build/html/%.html, $(SLIDES))
	@mkdir -p build/pdf
	prince $^ -o $@ -s prince.css

pdf: build/pdf/slides.pdf

#
# NOTEBOOK
#

%.v3.ipynb: %.ipynb
	echo $<
	jupyter nbconvert --to notebook --nbformat 3 $<

notebook_v3: $(NOTEBOOK_V3_FROM_NOTEBOOK)

#
# CLEAN
#

clean:
	@rm -rf build
