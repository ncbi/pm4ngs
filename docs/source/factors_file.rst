Samples description file
========================

The "factors.txt" file is the file where the initial data files names and metadata are specified. This is file is the
base of the workflow and should be copied to the folder **data/DATESET** just after creating the project structure.

It should have the columns:

+----------------+------------+--------------+-----------+
| id             | SampleID   | condition    | replicate |
+================+============+==============+===========+
| classical01    | SRR4053795 | classical    | 1         |
+----------------+------------+--------------+-----------+
| classical01    | SRR4053796 | classical    | 2         |
+----------------+------------+--------------+-----------+
| nonclassical01 | SRR4053802 | nonclassical | 1         |
+----------------+------------+--------------+-----------+
| nonclassical01 | SRR4053803 | nonclassical | 2         |
+----------------+------------+--------------+-----------+

Columns names are required and are case sensitive.
