TQ Systems Community BSP Documentation
======================================

This project hosts the documentation of TQ Systems Community BSP
and related repositories.

The documentation is written using Sphinx documentation system. To
install it in Debian/Ubuntu, please do:

  soudo apt-get install python-sphinx

The integrated SVG to image conversion is using SAX-based renderer
library for SVG files. To install it in Debian/Ubuntu, please do:

  soudo apt-get install librsvg2-bin

Once this has been complete, you can run a 'make' and check the
possible targets for building.


--------------------------------------------------------------------------

Optional you can setup Python's virtual environment to use th latest
Sphinx build packages:

    sudo apt-get install python-dev
    sudo apt-get install python-virtualenv
    sudo apt-get install libfreetype6-dev

    virtualenv --no-site-packages pyvenv
    source pyvenv/bin/activate
    pip install reportlab
    pip install sphinx
    pip install sphinxcontrib-email
    pip install sphinxcontrib-tikz
    pip install sphinxcontrib-blockdiag

    cd src
    make ...

    deactivate
