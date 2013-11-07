Yocto Folders
=============

.. sectionauthor:: Stephan Linz <rexut95@gmail.com>

* **tqs-community-bsp**: Base (BASE) directory where all Yocto data
  resides (recipes, source code, built packages, images, etc)

* **BASE/sources**: Source (SOURCE) directory where metadata (layers)
  resides

* `BASE/build`_: Build (BUILD) directory where ``bitbake`` commands
  are executed

* `BASE/build/tmp`_: Target (TMP) directory for all bitbake commands

* `BASE/build/tmp/work`_: Working (WORKING) directory for recipes
  tasks

* `BASE/build/tmp/deploy`_: Deploy (DEPLOY) directory where bitbake's
  output data is found

* `BASE/build/tmp/deploy/images`_: Complete and partial images are
  found under this folder



.. ##################################################################
.. Link list to Yocto reference manual:

.. _`BASE/build`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build
.. _`BASE/build/tmp`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-tmp
.. _`BASE/build/tmp/work`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-tmp-work
.. _`BASE/build/tmp/deploy`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-tmp-deploy
.. _`BASE/build/tmp/deploy/images`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#structure-build-tmp-deploy-images
