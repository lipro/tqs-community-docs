.. _patching-kernel:

Patching the Linux Kernel
=========================

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

The Linux Kernel is just another recipe for Yocto, so learning to patch
it you learn to patch any other package. In the other hand, Yocto
**should not** be used for package development, but in those rare cases
follow the steps below. It is assumed that you have already build the
package you want to patch.

* Create the patch or patches. In this example we are patching the
  Linux kernel for tqma35_ machine; in other words, the value of
  MACHINE on the ``build/conf/local.conf`` is
  ``MACHINE ??= 'tqma35_'``. In case you already have the patches,
  make sure these can be nicely applied with the commands
  ``git apply --check <PATCH_NAME>``, and jump this step.

::

    build $ cd tmp/work/tqma35-poky-linux-gnueabi/\
    linux-tqs/2.6.34.14+gitAUTOINC+6b4ea726b39f32041ac4d2dd03cf056c57b638ac-r32.1/git
    build $ # Edit any files you want to change
    build $ git add <modified file 1> <modified file 2> ..  # Select the files you 
                                                            # want to commit
    build $ git commit -s -m '<your commit's title>'        # Create the commit
    build $ git format-patch -1                             # Create the patch

    # e.g. 0001-calibrate-Add-printk-example.patch

* Create a new layer (see section :ref:`create-new-layer`)

* On the new layer (e.g. ``meta-tqs-custom``), create the corresponding
  subfolders and the ``.bbappend`` file:

::

    sources $ mkdir -p meta-tqs-custom/recipes-kernel/linux/linux-tqs-2.6.34.14
    sources $ cat > meta-tqs-custom/recipes-kernel/linux/linux-tqs_git.bbappend
    FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}-${PV}:"
    SRC_URI += "file://0001-calibrate-Add-printk-example.patch"
    PRINC := "${@int(PRINC) + 1}"
    ^d

* Move the patch to the new layer

::

    sources $ mv ../build/tmp/work/tqma35-poky-linux-gnueabi/linux-tqs/\
    2.6.34.14+gitAUTOINC+6b4ea726b39f32041ac4d2dd03cf056c57b638ac-r32.1/\
    git/0001-calibrate-Add-printk-example.patch \
        meta-tqs-custom/recipes-kernel/linux/linux-tqs-2.6.34.14

* Setup the enviroment and clean previous package's build data (sstate)

::

    tqs-community-bsp $ . setup-environment build
    build $ bitbake -c cleansstate linux-tqs

* Compile and Deploy

::

    build $ bitbake -f -c compile linux-tqs
    build $ bitbake -c deploy linux-tqs

* Insert the SD into your host and copy the ``uImage`` into the first
  partition. Do not forget to unmount the partition before removing the
  card!

  .. todo::

     The issue `SD Card preperation` with new Linux kernel needs
     to be evaluated! Do not yet apply this description!

::

    build $ sudo cp tmp/deploy/images/uImage /media/boot

* Insert the SD into your board and test your change.


.. ##################################################################
.. Link list to external references:

.. _tqma35: http://support.tq-group.com/doku.php?id=en:arm:tqma35
