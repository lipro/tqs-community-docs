.. _build-and-boot:

Build and Boot your TQ Systems Yocto Image
==========================================

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

* Check
  `required <http://www.yoctoproject.org/docs/1.4/ref-manual/ref-manual.html#required-packages-for-the-host-development-system>`_
  packages for your Linux Distribution and install them.

* Install the
  `repo <http://source.android.com/source/developing.html>`_ utility
  following these steps:

  ::

      $ mkdir ~/bin
      $ curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > \
        ~/bin/repo
      $ chmod a+x ~/bin/repo
      $ PATH=${PATH}:~/bin

* Download the BSP metadata (recipes + configuration files + classes):

  ::

      $ mkdir tqs-community-bsp
      $ cd tqs-community-bsp
      tqs-community-bsp $ repo init \
                          -u https://github.com/lipro/tqs-community-bsp-platform \
                          -b dylan
      tqs-community-bsp $ repo sync # Takes some minutes the first time 

* Select your machine and prepare the bitbake's environment:

  ::

      # To list all TQS related machines, type
      tqs-community-bsp $ find sources/meta-tqs* -name "*.conf" | grep "conf/machine"
      tqs-community-bsp $ MACHINE=<selected machine> . ./setup-environment build
      # if MACHINE is not set, the default machine is 'qemuarmv6'
      build $

* Choose an image and bake it!

  ::

      build $ bitbake-layers show-recipes | grep image    # To list all possible images
      build $ bitbake <selected image>                    # Bake! The first time can 
                                                          # take several hours.
      # e.g. bitbake core-image-minimal

* Boot (e.g. :option:`core-image-minimal`) on the machine
  :option:`qemuarmv6` with Yocto's :program:`runqemu`:

  ::

      build $ MACHINE=qemuarmv6 runqemu \
              tmp/deploy/images/zImage-qemuarmv6.bin \
              tmp/deploy/images/core-image-minimal-qemuarmv6.ext3

* Flash SD Card for machines other than :option:`qemuarmv6`:

  .. warning::

     The issue `Flash SD Card` needs to be evaluated!
     Do not yet apply this description!

  ::

      # Insert your SD Card
      # Type '$ dmesg | tail' to see the device node being used, e.g /dev/sdb)
      # In case SD to be flash has already some partitions, the host system may have 
      # mounted these, so unmount them, e.g. '$ sudo umount /dev/sdb?'.
      build $ ls -la 'tmp/deploy/images/*.sdcard'

      # Flash the soft link one
      build $ sudo dd \
              if=tmp/deploy/images/<selected image>-<select machine>.sdcard \
              of=/dev/sdX \
              bs=1M
      build $ sync                

* Place your SD Card in the correct board's slot and boot!


.. only:: html

   Found Errors? Subscribe and report it to
   :email:`the author <linz@li-pro.net>`
   with subject "[tqs-community-bsp] Error report: <your_msg>".

.. only:: latex or man or texinfo or text

   Found Errors? Subscribe and report it to
   the author <linz@li-pro.net>
   with subject "[tqs-community-bsp] Error report: <your_msg>".

.. `meta-tqsystems <https://lists.yoctoproject.org/listinfo/meta-tqsystems>`_
.. mailing list.
