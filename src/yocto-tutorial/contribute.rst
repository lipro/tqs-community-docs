Contributing to the TQ Systems Yocto Project
============================================

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

The Yocto Project is open-source, so anyone can contribute. No matter
what your contribution is (bug fixing or new metadata), contributions
are sent through patches to a community list. Many eyes will look into
your patch and at some point it is either rejected or accepted. Follow
these steps to contribute:

* Make sure you have previously configured your personal info:

::

    $ git config --global user.name "Your Name Here"
    $ git config --global user.email "your_email@example.com"

.. * Subscribed to the Freescale Yocto Project `Mailing
..   List <https://lists.yoctoproject.org/listinfo/meta-tqsystems>`_

* Download ``master`` branches:

::

    tqs-community-bsp $  repo init \
        -u git://github.com/lipro/tqs-community-bsp-platform \
        -b master

* Update:

::

    tqs-community-bsp $ repo sync

* Create local branches so your work is *not* done on master:

::

    tqs-community-bsp $ repo start <branch name> --all

Where ``<branch name>`` is any name you want to give to your local
branch (e.g. ``fix_uboot_recipe``, ``new_gstreamer_recipe``, etc.).

* Make your changes in any TQ Systems related folder (e.g.
  sources/meta-tqs-arm). In case you modified a recipe
  (``.bb``) or include (``.inc``) file, do not forget to
  *bump* (increase the value by one) either the ``PR`` or
  ``INC_PR`` value.

* Commit your changes using ``git``. In this example we assume your
  change is on ``meta-tqs-arm`` folder:

::

    sources/meta-tqs-arm $ git add <file 1> <file 2>
    sources/meta-tqs-arm $ git commit

On the commit's log, the title must start with the filename change
or introduced, then a brief description of the patch's goal,
following with a long description. Make sure you follow the
standards (type :program:`git log --pretty=oneline` to see previous
commits).

* Create a patch:

::

    sources/meta-tqs-arm $ git format-patch -s \
        --subject-prefix='meta-tqs-arm][PATCH' -1

Where the last parameter (``-1``) indicate to patch last commit. In
case you want to create patches for older commits, just indicate the
correct index. If your patch is done in other folder, just make sure
you change the ``--subject-prefix`` value.

* Send your patch or patches with:

.. ::
.. 
..     sources/meta-tqs-arm $ git send-email \
..         --to meta-tqsystems@yoctoproject.org <patch>

::

    sources/meta-tqs-arm $ git send-email \
        --to linz@li-pro.net <patch>

Where ``<patch>`` is the file created by :program:`git format-patch`.

* Keep track of patch's responses on the mailing list. In case you need
  to rework your patch, repeat the steps but this time the patch's
  subject changes to ``--subject-prefix='meta-tqs-*][PATCH v2'``.

* Once your patch has been approved, you can delete your working
  branches:

::

    tqs-community-bsp $ repo abandon <branch name>
