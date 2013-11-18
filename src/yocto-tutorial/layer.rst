.. _create-new-layer:

Creating a new Layer
====================

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

It is suggested to create a layer when creating or modifying any
metadata file (recipe, configuration file or class). The main reason is
simple: modularity. In the other hand, make sure your new metadata has
not already be implemented (layer, recipe or machine), so before
proceeding check
`this <http://layers.openembedded.org/layerindex/layers/>`_ link.

* To have access to Yocto scripts, setup the enviroment from the BASE
  folder:

  ::

      tqs-community-bsp $ . setup-environment build

* Move to the place you want to create your layer and choose a name
  (e.g. ``meta-tqs-custom``):

  ::

      sources $ yocto-layer create meta-tqs-custom
      # Answer the questions. Make sure the priority is set correctly
      # (higher numbers, higher priorities). Set the priority equal to
      # the lowest already present, except when you have introduce a
      # new recipe with the same name as other and want to shadow the
      # original one.

* Add any metadata content. Suggestion: Version the layer with Git and
  upload your local git repo to a server.

* Edit and add the layer to the ``build/conf/bblayers.conf`` file.

  .. todo:: 

     The issue `Add the Layer` to the ``build/conf/bblayers.conf``
     file (modify this file) and `versioning new custom layer with
     Git` should describe more precise in focus of the underlayed
     ``repo`` tool. **Maybe that this part of the tutorial is not
     proper!**

* To verify that your layer is *seen* by BitBake, run the following
  command under the BUILD folder:

  ::

      build $ bitbake-layers show-layers
