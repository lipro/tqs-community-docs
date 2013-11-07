Building the Kernel Manually
============================

.. sectionauthor:: Stephan Linz <rexut95@gmail.com>

* To setup the Yocto environment, from the BASE folder run:

::

    tqs-community-bsp $ . setup-environment build

* Build the toolchain:

::

    build $ bitbake meta-toolchain
    # Other toolchains:
    #   Qt Embedded toolchain build: bitbake meta-toolchain-qte
    #   Qt X11 toolchain build: bitbake meta-toolchain-qt

* Install it on your PC:

::

    build $ sudo sh \
        tmp/deploy/sdk/poky-eglibc-x86_64-arm-toolchain-<version>.sh

* Setup the toolchain environment:

::

    build $ source \
        /opt/poky/<version>/environment-setup-armv6-vfp-poky-linux-gnueabi

* Get the Linux Kernel's source code:

::

    $ git clone git://github.com/lipro/linux-tqs.git linux-tqs
    $ cd linux-tqs

* Create a local branch:

::

    linux-tqs $ BRANCH=tqma35 # Change to any branch you want,
                              # Use 'git branch -a' to list all
    linux-tqs $ git checkout -b ${BRANCH} origin/${BRANCH}

* Export ARCH and CROSS_COMPILE:

::

    linux-tqs $ export ARCH=arm  
    linux-tqs $ export CROSS_COMPILE=arm-poky-linux-gnueabi-
    linux-tqs $ unset LDFLAGS

* Choose configuration and compile:

::

    linux-tqs $ make tqma35_defconfig  
    linux-tqs $ make uImage  

* To Test your changes, insert the SD into your host and copy
  the ``uImage`` into the first partition:

  .. todo::

     The issue `SD Card preperation` with new Linux kernel needs
     to be evaluated! Do not yet apply this description!

::

    linux-tqs $ sudo cp arch/arm/boot/uImage /media/boot

* If case you want your changes to be reflected on your Yocto
  Framework, create the patches following the section
  :ref:`patching-kernel`.
