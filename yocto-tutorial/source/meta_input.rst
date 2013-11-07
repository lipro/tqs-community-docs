Bitbake Metadata
================

.. sectionauthor:: Stephan Linz <rexut95@gmail.com>

BitBake handles the parsing and execution of the data files. The data
itself is of various types:

* Recipes: Provides details about particular pieces of software.
* Class Data: Abstracts common build information (e.g. how to build a
  Linux kernel).
* Configuration Data: Defines machine-specific settings, policy
  decisions, and so forth. Configuration data acts as the glue to bind
  everything together.

Layers
------

* Metadata is organized into multiple `layers`.
* Layers allow you to isolate different types of customizations from
  each other.
* DO NOT do your modifications in existing layers, instead create a
  layer and create recipes (``.bb`` files) or modified existing ones
  (``.bbappend`` files)

Configuration Data
------------------

* `build/conf/local.conf`_: Local User Configuration for your build
  environment
* `build/conf/site.conf`_: Local Shared (site wide) Configuration for
  your build environment
* `build/conf/bblayers.conf`_: Define layers, which are directory
  trees, traversed by BitBake.
* `sources/meta-*/conf/layer.conf`_: Layer configuration file
* `sources/meta-*/conf/machine/*.conf`_: Machine configuration files

Build's local configuration file ``build/conf/local.conf``
``````````````````````````````````````````````````````````

::

    MACHINE ??= 'tqma35'
    DISTRO ?= 'poky'
    #PACKAGE_CLASSES ?= "package_rpm"
    EXTRA_IMAGE_FEATURES = "debug-tweaks"
    USER_CLASSES ?= "buildstats image-mklibs image-prelink"
    PATCHRESOLVE = "noop"
    BB_DISKMON_DIRS = "\
        STOPTASKS,${TMPDIR},1G,100K \
        STOPTASKS,${DL_DIR},1G,100K \
        STOPTASKS,${SSTATE_DIR},1G,100K \
        ABORT,${TMPDIR},100M,1K \
        ABORT,${DL_DIR},100M,1K \
        ABORT,${SSTATE_DIR},100M,1K" 
    CONF_VERSION = "1"

    BB_NUMBER_THREADS = '4'
    PARALLEL_MAKE = '-j 4'
    ACCEPT_FSL_EULA = ""

Important variables:

* MACHINE_: Indicates the target machine, `qemuarmv6` is the default.
* BB_NUMBER_THREADS_ and PARALLEL_MAKE_: Indicate the max number
  of threads when baking and compiling.


Build's local configuration file ``build/conf/site.conf``
``````````````````````````````````````````````````````````

::

    SCONF_VERSION = "1"
    BSPDIR := "${@os.path.abspath(os.path.dirname(d.getVar('FILE', True)) + '/../..')}"    
    DL_DIR = "${BSPDIR}/downloads/"

Important variables:

* DL_DIR_: Tarball repository. Several users can share the same
  folder, so data can be reused.

Build's layer configuration file ``build/conf/bblayers.conf``
`````````````````````````````````````````````````````````````

* Automatically created by the ``setup-environment`` script (see
  section :ref:`build-and-boot`)

* Only modified when adding a new layer:

::

    LCONF_VERSION = "6"

    BBPATH = "${TOPDIR}"
    BSPDIR := "${@os.path.abspath(os.path.dirname(d.getVar('FILE', True)) + '/../..')}"

    BBFILES ?= ""
    BBLAYERS = " \
      ${BSPDIR}/sources/poky/meta \
      ${BSPDIR}/sources/poky/meta-yocto \
      \
      ${BSPDIR}/sources/meta-fsl-arm \
      \
      ${BSPDIR}/sources/meta-tqs-arm \
    "

Layer configuration file ``source/meta-tqs-arm/conf/layer.conf``
````````````````````````````````````````````````````````````````

::

    # We have a conf and classes directory, add to BBPATH
    BBPATH .= ":${LAYERDIR}"

    # We have a packages directory, add to BBFILES
    BBFILES += "${LAYERDIR}/recipes-*/*/*.bb \
                ${LAYERDIR}/recipes-*/*/*.bbappend"

    BBFILE_COLLECTIONS += "tqs-arm"
    BBFILE_PATTERN_tqs-arm := "^${LAYERDIR}/"
    BBFILE_PRIORITY_tqs-arm = "6"

Important variables:

* BBFILES_: Indicates where to look for ``.bb*`` files
* BBFILE_PRIORITY_tqs-arm_: Indicates layer's priority
* MIRRORS_: Indicates where to get the source code

Machine configuration file: ``meta-tqs-arm/conf/tqma35.conf``
`````````````````````````````````````````````````````````````

::

    #@TYPE: Machine
    #@NAME: TQ System i.MX35 Embedded module (tqma35)
    #@SOC: i.MX35
    #@DESCRIPTION: Machine configuration for TQ System i.MX35 Embedded module (tqma35)

    include conf/machine/include/soc-family.inc
    include conf/machine/include/imx-base.inc
    include conf/machine/include/tune-arm1136jf-s.inc

    SOC_FAMILY = "mx3:mx35"

    PREFERRED_VERSION_udev_mx3 = "172"

    PREFERRED_PROVIDER_virtual/kernel_mx3 = "linux-tqs"
    PREFERRED_PROVIDER_u-boot = "u-boot-tqs"

    UBOOT_MACHINE = "TQMa35_config"
    UBOOT_SUFFIX = "bin"
    UBOOT_MAKE_TARGET = "u-boot.${UBOOT_SUFFIX}"

    SERIAL_CONSOLE = "115200 ttymxc0"

    MACHINE_FEATURES += "ext2 ext3 screen"

[`conf/machine/include/imx-base.inc`_] (from the `meta-fsl-arm` layer)

Important variables:

* IMAGE_FSTYPES_: Located on `imx-base.inc`_. Defines the type of
  outputs for the Root Filesystem. Default is:
  ``"tar.bz2 ext3 sdcard"``. On the TQMa35 we have to evaluate:
  ``"ubi jffs2 tar.bz2"``.
* `UBOOT_ENTRYPOINT_*`_: Located on `imx-base.inc`_. Defines where
  the Kernel is loaded by U-Boot.
* SOC_FAMILY_: Defines machine's family. Only recipes with the same
  SOC_FAMILY_ (defined with the recipe's variable
  COMPATIBLE_MACHINE_) are taken into account when baking for a
  particular machine.
* UBOOT_MACHINE_: Define the U-Boot configuration file
* `PREFERRED_PROVIDER_*`_: Defines which package name (PN_) of the
  recipe you want to give precedence.

  * `PREFERRED_PROVIDER_virtual/kernel_mx3`_. Default located on
    `imx-base.inc`_. Defines the Freescale community supported
    Linux kernel (`linux-fslc`). On the TQMa35 we force to use the
    TQ Systems supported Linux kernel (`linux-tqs`).
  * `PREFERRED_PROVIDER_u-boot`_. Default located on
    `fsl-default-providers.inc`_. Defines the Freescale community
    supported U-Boot (`u-boot-fslc`). On the TQMa35 we force to use
    the TQ Systems supported U-Boot (`u-boot-tqs`).

* `PREFERRED_VERSION_*`_: Defines which package version (PV_) of the
  recipe you want to give precedence.

  * `PREFERRED_VERSION_udev_mx3`_: Default is nowhere located on and
    is always (and implicitly) defined by the head udev recipe version
    in the Poky distribution (see `poky/meta` layer). On the TQMa35
    we force to use the older but with the TQ Systems supported Linux
    kernel more compatible version 172.

.. _`imx-base.inc`: http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/conf/machine/include/imx-base.inc
.. _`conf/machine/include/imx-base.inc`: `imx-base.inc`_
.. _`fsl-default-providers.inc`: http://git.yoctoproject.org/cgit/cgit.cgi/meta-fsl-arm/tree/conf/machine/include/fsl-default-providers.inc

Machine configuration file: ``meta-tqs-arm/conf/qemuarmv6.conf``
````````````````````````````````````````````````````````````````

::

    #@TYPE: Machine
    #@NAME: arm_versatile_1136jfs
    #@DESCRIPTION: arm_versatile_1136jfs

    require conf/machine/include/qemu.inc
    require conf/machine/include/tune-arm1136jf-s.inc

    PREFERRED_VERSION_udev = "172"

    PREFERRED_PROVIDER_virtual/kernel = "linux-tqs"

    KERNEL_IMAGETYPE = "zImage"

    SERIAL_CONSOLE = "115200 ttyAMA0"

[`conf/machine/include/qemu.inc`_] (from the `poky/meta` layer)

.. _`qemu.inc`: http://git.yoctoproject.org/cgit/cgit.cgi/poky/tree/meta/conf/machine/include/qemu.inc
.. _`conf/machine/include/qemu.inc`: `qemu.inc`_

Important variables:

* IMAGE_FSTYPES_: Located on `qemu.inc`_. Defines the type of
  outputs for the Root Filesystem. Default is:
  ``"tar.bz2 ext3"``. `Ext3` can than used by ``runqemu`` command.
* EXTRA_IMAGEDEPENDS_: Located on `qemu.inc`_. Defines the extra
  dependent tasks to host's native Qemu tools. Default is:
  ``"qemu-native qemu-helper-native"``
* KERNEL_IMAGETYPE_: Define the Linux kernel image binary format.
  `zImage` can than used by ``runqemu`` command.
* SERIAL_CONSOLE_: Define the serial console (`baud rate` and
  `device name`) for getty.
* `PREFERRED_PROVIDER_virtual/kernel`_. Default located on
  `qemu.inc`_. Defines the Freescale community supported
  Linux kernel (`linux-yocto`). On the QemuARMv6 we force to use the
  TQ Systems supported Linux kernel (`linux-tqs`).
* `PREFERRED_VERSION_udev`_: Default is nowhere located on and
  is always (and implicitly) defined by the head udev recipe version
  in the Poky distribution (see `poky/meta` layer). On the TQMa35
  we force to use the older but with the TQ Systems supported Linux
  kernel more compatible version 172.


.. ##################################################################
.. Link list to Yocto reference manual:

.. _`build/conf/local.conf`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-conf-local.conf
.. _`build/conf/site.conf`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#user-configuration
.. _`build/conf/bblayers.conf`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-conf-bblayers.conf
.. _`sources/meta-*/conf/layer.conf`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#metadata-machine-configuration-and-policy-configuration
.. _`sources/meta-*/conf/machine/*.conf`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#bsp-layer
.. _MACHINE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-MACHINE
.. _BB_NUMBER_THREADS: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-BB_NUMBER_THREADS
.. _PARALLEL_MAKE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-PARALLEL_MAKE
.. _DL_DIR: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-DL_DIR
.. _BBFILES: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-BBFILES
.. _BBFILE_PRIORITY_tqs-arm: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-BBFILE_PRIORITY
.. _MIRRORS: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-MIRRORS
.. _IMAGE_FSTYPES: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-IMAGE_FSTYPES
.. _`UBOOT_ENTRYPOINT_*`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-UBOOT_ENTRYPOINT
.. _SOC_FAMILY: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-SOC_FAMILY
.. _COMPATIBLE_MACHINE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-COMPATIBLE_MACHINE
.. _UBOOT_MACHINE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-UBOOT_MACHINE
.. _`PREFERRED_PROVIDER_*`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-PREFERRED_PROVIDER
.. _`PREFERRED_PROVIDER_virtual/kernel_mx3`: `PREFERRED_PROVIDER_*`_
.. _`PREFERRED_PROVIDER_virtual/kernel`: `PREFERRED_PROVIDER_*`_
.. _`PREFERRED_PROVIDER_u-boot`: `PREFERRED_PROVIDER_*`_
.. _PN: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-PN
.. _`PREFERRED_VERSION_*`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-PREFERRED_VERSION
.. _`PREFERRED_VERSION_udev_mx3`: `PREFERRED_VERSION_*`_
.. _`PREFERRED_VERSION_udev`: `PREFERRED_VERSION_*`_
.. _PV: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-PV
.. _EXTRA_IMAGEDEPENDS: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-EXTRA_IMAGEDEPENDS
.. _KERNEL_IMAGETYPE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-KERNEL_IMAGETYPE
.. _SERIAL_CONSOLE: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#var-SERIAL_CONSOLE

