# Makefile for Sphinx documentation
#

VERSION = 1
PATCHLEVEL = x
SUBLEVEL =
EXTRAVERSION =

ifneq "$(SUBLEVEL)" ""
DOC_VERSION = $(VERSION).$(PATCHLEVEL).$(SUBLEVEL)$(EXTRAVERSION)
else
DOC_VERSION = $(VERSION).$(PATCHLEVEL)$(EXTRAVERSION)
endif

DOC_RELEASE = $(DOC_VERSION)$(shell ../scripts/setlocalversion ..)

# You can set these variables from the command line.
SPHINXOPTS    = -D version=$(DOC_VERSION) -D release=$(DOC_RELEASE)
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build
BUILDNAME     = TQSystemsCommunityBSP

# Internal variables.
SOURCEDIR       = .
# the IMAGEDIRS can be a list of directories that contain SVG files and are relative to the SOURCEDIR
IMAGEDIRS       = _images release-notes/_images yocto-tutorial/_images
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(SOURCEDIR)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(SOURCEDIR)

# Build a list of SVG files to convert to PDFs
PDFs := $(foreach dir, $(IMAGEDIRS), $(patsubst %.svg,%.pdf,$(wildcard $(SOURCEDIR)/$(dir)/*.svg)))

# Build a list of SVG files to convert to PNGs
PNGs := $(foreach dir, $(IMAGEDIRS), $(patsubst %.svg,%.png,$(wildcard $(SOURCEDIR)/$(dir)/*.svg)))

# SVG to PDF conversion
SVG2PDF       = rsvg-convert
SVG2PDF_FLAGS = --format=pdf --keep-aspect-ratio

# SVG to PNG conversion
SVG2PNG       = rsvg-convert
SVG2PNG_FLAGS = --format=png --dpi-x=90 --dpi-y=90 --keep-aspect-ratio
#SVG2PNG_FLAGS += --background-color=\#00

# Fix #1352 (http://bitbucket.org/birkenfeld/sphinx/issue/1352/)
HTML_LOGO = $(shell awk '/html_logo/{print $$3}' conf.py | head -1 | xargs basename)

.PHONY: help fixes clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf xelatex xelatexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  xelatex    to make XeTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  xelatexpdf to make XeTeX files and run them to generate PDF"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

fixes:
	@echo "Fix known issues introduced with different new Sphinx versions:"
	@echo "  #1352      http://bitbucket.org/birkenfeld/sphinx/issue/1352/"
	@echo "             touch $(HTML_LOGO)"
	@touch -f $(HTML_LOGO)

clean: clean-images
	-rm -rf $(BUILDDIR)/*
	-rm -f $(HTML_LOGO)

html: images-png fixes
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml: images-png fixes
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml: images-png fixes
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle: images-png fixes
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json: images-png fixes
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp: images-png fixes
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp: images-png fixes
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/$(BUILDNAME).qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/$(BUILDNAME).qhc"

devhelp: images-png fixes
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/$(BUILDNAME)"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/$(BUILDNAME)"
	@echo "# devhelp"

epub: images-png fixes
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

xelatex: images-pdf fixes
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/xelatex
	sed -i -e 's/pdflatex/xelatex/g' $(BUILDDIR)/xelatex/Makefile
	for pdf in $(BUILDDIR)/xelatex/blockdiag-*.pdf; do pdftops $$pdf; done
	for ps  in $(BUILDDIR)/xelatex/blockdiag-*.ps;  do epstopdf $$ps;  done
	@echo
	@echo "Build finished; the XeTeX files are in $(BUILDDIR)/xelatex."
	@echo "Run \`xelatex *.tex' in that directory to generate PDF" \
	      "(use \`make xelatexpdf' here to do that automatically)."

xelatexpdf: images-pdf fixes
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/xelatex
	sed -i -e 's/pdflatex/xelatex/g' $(BUILDDIR)/xelatex/Makefile
	for pdf in $(BUILDDIR)/xelatex/blockdiag-*.pdf; do pdftops $$pdf; done
	for ps  in $(BUILDDIR)/xelatex/blockdiag-*.ps;  do epstopdf $$ps;  done
	@echo "Running XeTeX files through xelatex..."
	$(MAKE) -C $(BUILDDIR)/xelatex all-pdf
	@echo "xelatex finished; the PDF files are in $(BUILDDIR)/xelatex."

latex: # images-pdf fixes
	@echo "TEMPORARY OFF: use \`make xelatex' instead."
	@#$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@#echo
	@#echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@#echo "Run \`make' in that directory to run these through (pdf)latex" \
	 #     "(use \`make latexpdf' here to do that automatically)."

latexpdf: # images-pdf fixes
	@echo "TEMPORARY OFF: use \`make xelatexpdf' instead."
	@#$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@#echo "Running LaTeX files through pdflatex..."
	@#$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@#echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text: fixes
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man: fixes
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo: fixes
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info: fixes
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext: fixes
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes: fixes
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck: fixes
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest: fixes
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

# Pattern rule for converting SVG to PDF
%-logo.pdf : %-logo.svg
	$(SVG2PDF) $(SVG2PDF_FLAGS) --width=100 --height=100 $< > $@

%.pdf : %.svg
	$(SVG2PDF) $(SVG2PDF_FLAGS) $< > $@

# Pattern rule for converting SVG to PNG
%-logo.png : %-logo.svg
	$(SVG2PNG) $(SVG2PNG_FLAGS) --width=100 --height=100 $< > $@

%.png : %.svg
	$(SVG2PNG) $(SVG2PNG_FLAGS) $< > $@

# Make a rule to build the PDFs
images-pdf: $(PDFs)

# Make a rule to build the PNGs
images-png: $(PNGs)

# Make a rule to build the images
images: images-pdf images-png

clean-pdf:
	-rm $(PDFs)

clean-png:
	-rm $(PNGs)

clean-images: clean-pdf clean-png
