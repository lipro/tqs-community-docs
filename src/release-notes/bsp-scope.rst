BSP Scope
=========

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

The scope of this release includes meta-tqs-arm.
Please, see in next table the complete supported board list.

.. include:: machine-list.inc


Priority of Dependent Layers
----------------------------

.. blockdiag::
   :desctable:

   blockdiag {
     orientation = portrait;
     default_fontsize = 12;		// default value is 11
     default_shape = roundedbox;	// default value is 'box'
     default_group_color = "#FFF";
     default_node_color = "#FFF";
     
     group {
       orientation = portrait;
       fontsize = 16;
       label = "PRI:6";

       meta-tqs-arm;
     }
     
     group {
       orientation = portrait;
       fontsize = 16;
       label = "PRI:5";
       
       meta-fsl-arm -> poky-meta;
       meta-fsl-arm -> poky-meta-yocto;
     }
       
     meta-tqs-arm -> meta-fsl-arm;
       
     meta-tqs-arm       [fontfamily = "sansserif-bold"];
       
     meta-tqs-arm       [description = "OE/Yocto BSP layer for TQ Systems ARM based platforms (`this <index.html>`_)."];
     meta-fsl-arm 	[description = "OE/Yocto BSP layer for Freescale's ARM platforms: `DOC <http://freescale.github.io/>`__, `GIT <https://github.com/Freescale/meta-fsl-arm>`__"];
     poky-meta    	[description = "Poky Build Tool and Metadata: `DOC <https://www.yoctoproject.org/documentation>`__, `GIT <http://git.yoctoproject.org/cgit/cgit.cgi/poky/tree/meta>`__"];
     poky-meta-yocto	[description = "Yocto Build Tool and Metadata: `DOC <https://www.yoctoproject.org/documentation>`__, `GIT <http://git.yoctoproject.org/cgit/cgit.cgi/poky/tree/meta-yocto>`__"];
   }
