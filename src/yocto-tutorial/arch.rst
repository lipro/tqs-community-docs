Yocto Architecture
==================

.. only:: html

   .. sectionauthor:: |slz_obfuscated|

.. only:: latex or man or texinfo or text

   .. sectionauthor:: |slz_plain_text|

See `introducing the Yocto Project`_ and the
`general Yocto Project Development Environment figure`_
for more detailed informations:

.. figure:: ./_images/yocto-environment.*
   :align: center
   :alt: 

.. _`introducing the Yocto Project`: http://www.yoctoproject.org/docs/1.5/yocto-project-qs/yocto-project-qs.html#yp-intro
.. _`general Yocto Project Development Environment figure`: http://www.yoctoproject.org/docs/1.5/ref-manual/ref-manual.html#general-yocto-environment-figure


Yocto Release History
---------------------

See `Yocto Project Releases`_ for more detailed (and latest) informations:

========= ========== ======== ===== ===== =========
Name      Date       Yocto    Poky  BB    Links
========= ========== ======== ===== ===== =========
\         2014-04-25 1.6 [#]_             `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.6_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.6_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.6_Status>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.6_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.6_Milestone_Test_Report>`__
Dora      2013-10-18 1.5      10.0  1.20  `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.5_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.5_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.5_Status>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.5_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.5_Milestone_Test_Report>`__
Dylan     2013-04-26 1.4      9.0   1.18  `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.4_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.4_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.4_Status>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.4_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.4_Milestone_Test_Report>`__
Danny     2012-10-26 1.3      8.0   1.16  `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.3_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.3_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.3_Status>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.3_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.3_Milestone_Test_Report>`__
Denzil    2012-04-27 1.2      7.0   1.15  `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.2_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.2_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.2_Status>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.2_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.2_Milestone_Test_Report>`__
Edison    2011-10-06 1.1      6.0   1.13  `Features <http://wiki.yoctoproject.org/wiki/Yocto_1.1_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.1_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.1_Release_Criteria>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.1_Overall_Test_Plan>`__,
                                          `Test Report <http://wiki.yoctoproject.org/wiki/Yocto_1.1_Milestone_Test_Report>`__
Bernard   2011-04-06 1.0      5.0   1.11  `Features <http://wiki.yoctoproject.org/wiki/Yocto_Features>`__,
                                          `Schedule <http://wiki.yoctoproject.org/wiki/Yocto_1.0_Schedule>`__,
                                          `Status <http://wiki.yoctoproject.org/wiki/Yocto_Project_v1.0_Release_Criteria>`__,
                                          `Test Plan <http://wiki.yoctoproject.org/wiki/Yocto_1.0_Overall_Test_Plan>`__
Laverne              0.9      4.0   1.11
Purple                        3.2
Pinky                         3.1
Blinky                        3.0
Clyde                         2.0
Inky                          1.0
========= ========== ======== ===== ===== =========

.. _`Yocto Project Releases`: http://wiki.yoctoproject.org/wiki/Releases

.. rubric:: Footnotes

.. [#] in planning
