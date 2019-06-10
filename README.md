Cookiecutter Jupyter Notebook Template for NGS data analysis
============================================================

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), 
[Jupyter Notebook](https://jupyter.org/) and [CWL](https://www.commonwl.org/).

Features
---------
* Works with Python 3.6+
* Jupyter Notebook as interface for workflow execution
* Jupyter Notebook for Data management
* Automatic report project

Constraints
-----------
* Designed for running  in a single server. Modify it if HPC or cloud systems will be used

Installation
------------

Let's pretend you want to create a RNA-Seq project called "rnaseq-sra-single" to analyze samples 
included in the NCBI BioProject [PRJNA339968](https://www.ncbi.nlm.nih.gov/bioproject/339968).
These are single-end samples from  FACS-purified monocytes in human.

First, install Cookiecutter. 

    $ pip install cookiecutter

Now run it against this repo:

    $ cookiecutter https://github.com/ncbi/cookiecutter-jupyter-rnaseq
    
You'll be prompted for some values. 

    author_name: "Roberto Vera Alvarez"
    user_email: "veraalva@ncbi.nlm.nih.gov"
    project_name: "rnaseq-sra-single"
    dataset_name: "PRJNA339968"
    is_data_in_SRA: "y"
    ngs_data_type: "RNA-Seq"
    sequencing_technology: "single-end"
    organism: "human"
    genome_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38"
    genome_name: "hg38"
    aligner_index_dir: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/STAR"
    genome_fasta: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genome.fa"
    genome_gtf: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gtf"
    genome_gff: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gff"
    genome_gff3: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.gff3"
    genome_bed: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/genes.bed"
    genome_mappable_size: "hg38"
    genome_blacklist: "/gfs/data/genomes/igenomes/Homo_sapiens/UCSC/hg38/hg38-blacklist.bed"
    fold_change: "2.0"
    fdr: "0.05"
    use_docker: "y"
    pull_images: "y"
    cwl_runner: "cwl-runner"
    cwl_workflow_repo: "https://gitlab.com/r78v10a07/cwl-workflow/raw/master"
    create_virtualenv: "y"
    use_gnu_parallel: "y"
    max_number_threads: "16"

Then a project folder will be created for you following this structure. I'm including here all files created after
processing the samples. 
    
    rnaseq-sra-single
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA339968
    ├── index.html
    ├── notebooks
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Quantification.ipynb
    │   ├── 05 - DGA.ipynb
    │   └── 06 - GO enrichment.ipynb
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA339968
    ├── src
    ├── tmp
    └── venv

Then, copy a manually created `factors.txt` to the folder `data/PRJNA339968`.

The "factors.txt" file is the file where the initial data files and metadata are specified.
It should have the columns:

| id | SampleID | condition | replicate |
| --- | --- | --- | --- |
| classical01 | SRR4053795 | classical | 1 |
| classical01 | SRR4053796 | classical | 1 |
| nonclassical01 | SRR4053802 | nonclassical | 1 |
| nonclassical01 | SRR4053803 | nonclassical | 2 |

If the project option `is_data_in_SRA` is set to `y` (Yes) the `01 - Pre-processing QC.ipynb` will use the `SampleID` 
to download the files from the NCBI SRA database using fastq-dump. If the data is `single-end` you will see one 
file per sample `SRR4053795.fastq.gz`. However, if the data is paired-end you will see two files per samples 
`SRR4053795_1.fastq.gz` and `SRR4053795_2.fastq.gz`

If the project option `is_data_in_SRA` is set to `n` (No) you should place your `fastq` files in the `data/PRJNA339968`
(this folder will have the value of the `dataset_name` specified during project creation) folder using the `SampleID` column as the prefix of your sample leaving out the `.fastq.gz`. 

Usage
-----
    
Go inside the project folders and activate virtual environment:

    source venv/bin/activate
    
Start the jupyter notebook server

    jupyter notebook
    
Start executing the Jupyter notebook from the number `01-` in a sequential way. Once everythis is done run the
`00 - Project Report` for the creation of the final report page with tables and figures.

The final file structure should be:

    16 directories, 287 files

    rnaseq-sra-single
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    │   └── init.py
    ├── data
    │   └── PRJNA339968
    │       ├── SRR4053795.fastq.gz
    │       ├── SRR4053795_download.log
    │       ├── SRR4053795_fastqc.html
    │       ├── SRR4053795_fastqc.log
    │       ├── SRR4053795_fastqc.zip
    │       ├── SRR4053796.fastq.gz
    │       ├── SRR4053796_download.log
    │       ├── SRR4053796_fastqc.html
    │       ├── SRR4053796_fastqc.log
    │       ├── SRR4053796_fastqc.zip
    │       ├── SRR4053802.fastq.gz
    │       ├── SRR4053802_download.log
    │       ├── SRR4053802_fastqc.html
    │       ├── SRR4053802_fastqc.log
    │       ├── SRR4053802_fastqc.zip
    │       ├── SRR4053803.fastq.gz
    │       ├── SRR4053803_download.log
    │       ├── SRR4053803_fastqc.html
    │       ├── SRR4053803_fastqc.log
    │       ├── SRR4053803_fastqc.zip
    │       ├── SRR4053804.fastq.gz
    │       ├── SRR4053804_fastqc.html
    │       ├── SRR4053804_fastqc.zip
    │       ├── SRR4053805.fastq.gz
    │       ├── SRR4053805_fastqc.html
    │       ├── SRR4053805_fastqc.zip
    │       ├── SRR4053807.fastq.gz
    │       ├── SRR4053807_fastqc.html
    │       ├── SRR4053807_fastqc.zip
    │       ├── SRR4053818.fastq.gz
    │       ├── SRR4053818_fastqc.html
    │       ├── SRR4053818_fastqc.zip
    │       ├── SraRunTable.txt
    │       ├── commands
    │       └── factors.txt
    ├── index.html
    ├── notebooks
    │   ├── 00 - Project Report.html
    │   ├── 00 - Project Report.ipynb
    │   ├── 01 - Pre-processing QC.ipynb
    │   ├── 02 - Samples trimming.ipynb
    │   ├── 03 - Alignments.ipynb
    │   ├── 04 - Quantification.ipynb
    │   ├── 05 - DGA.ipynb
    │   └── 06 - GO enrichment.ipynb
    ├── requirements
    │   └── python.txt
    ├── results
    │   └── PRJNA339968
    │       ├── alignments
    │       │   ├── SRR4053795Aligned.out.stats
    │       │   ├── SRR4053795Log.final.out
    │       │   ├── SRR4053795_alignment.log
    │       │   ├── SRR4053795_sorted.bam
    │       │   ├── SRR4053795_sorted.bam.bai
    │       │   ├── SRR4053796Aligned.out.stats
    │       │   ├── SRR4053796Log.final.out
    │       │   ├── SRR4053796_alignment.log
    │       │   ├── SRR4053796_sorted.bam
    │       │   ├── SRR4053796_sorted.bam.bai
    │       │   ├── SRR4053802Aligned.out.stats
    │       │   ├── SRR4053802Log.final.out
    │       │   ├── SRR4053802_alignment.log
    │       │   ├── SRR4053802_sorted.bam
    │       │   ├── SRR4053802_sorted.bam.bai
    │       │   ├── SRR4053803Aligned.out.stats
    │       │   ├── SRR4053803Log.final.out
    │       │   ├── SRR4053803_alignment.log
    │       │   ├── SRR4053803_sorted.bam
    │       │   ├── SRR4053803_sorted.bam.bai
    │       │   ├── SRR4053804Aligned.out.stats
    │       │   ├── SRR4053804Log.final.out
    │       │   ├── SRR4053804_sorted.bam
    │       │   ├── SRR4053804_sorted.bam.bai
    │       │   ├── SRR4053805Aligned.out.stats
    │       │   ├── SRR4053805Log.final.out
    │       │   ├── SRR4053805_sorted.bam
    │       │   ├── SRR4053805_sorted.bam.bai
    │       │   ├── SRR4053807Aligned.out.stats
    │       │   ├── SRR4053807Log.final.out
    │       │   ├── SRR4053807_sorted.bam
    │       │   ├── SRR4053807_sorted.bam.bai
    │       │   ├── SRR4053818Aligned.out.stats
    │       │   ├── SRR4053818Log.final.out
    │       │   ├── SRR4053818_sorted.bam
    │       │   ├── SRR4053818_sorted.bam.bai
    │       │   ├── commands
    │       │   └── commands~
    │       ├── dga
    │       │   ├── classical_vs_nonclassical_deseq2_dga.log
    │       │   ├── classical_vs_nonclassical_edgeR_dga.log
    │       │   ├── classical_vs_nonclassical_heatmap_union.log
    │       │   ├── classical_vs_nonclassical_volcano_union.log
    │       │   ├── commands_dga
    │       │   ├── commands_union_plots
    │       │   ├── condition_classical_vs_nonclassical_deseq2.csv
    │       │   ├── condition_classical_vs_nonclassical_deseq2_correlation_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_deseq2_expression_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_deseq2_pca.csv
    │       │   ├── condition_classical_vs_nonclassical_deseq2_pca.pdf
    │       │   ├── condition_classical_vs_nonclassical_deseq2_volcano.pdf
    │       │   ├── condition_classical_vs_nonclassical_edgeR.csv
    │       │   ├── condition_classical_vs_nonclassical_edgeR_correlation_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_edgeR_expression_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_edgeR_pca.pdf
    │       │   ├── condition_classical_vs_nonclassical_edgeR_volcano.pdf
    │       │   ├── condition_classical_vs_nonclassical_union.csv
    │       │   ├── condition_classical_vs_nonclassical_union_correlation_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_union_expression_heatmap.pdf
    │       │   ├── condition_classical_vs_nonclassical_union_over-expressed.csv
    │       │   ├── condition_classical_vs_nonclassical_union_pca.pdf
    │       │   ├── condition_classical_vs_nonclassical_union_under-expressed.csv
    │       │   └── condition_classical_vs_nonclassical_union_volcano.pdf
    │       ├── go
    │       │   ├── go_biological_process_classical_vs_nonclassical_union.png
    │       │   ├── go_cellular_component_classical_vs_nonclassical_union.png
    │       │   ├── go_molecular_function_classical_vs_nonclassical_union.png
    │       │   ├── go_over_biological_process_classical_vs_nonclassical_union.csv
    │       │   ├── go_over_cellular_component_classical_vs_nonclassical_union.csv
    │       │   ├── go_over_molecular_function_classical_vs_nonclassical_union.csv
    │       │   ├── go_under_biological_process_classical_vs_nonclassical_union.csv
    │       │   ├── go_under_cellular_component_classical_vs_nonclassical_union.csv
    │       │   └── go_under_molecular_function_classical_vs_nonclassical_union.csv
    │       ├── quantification
    │       │   ├── ExonReads.tsv
    │       │   ├── ExonTPM.tsv
    │       │   ├── SRR4053795_quantification.log
    │       │   ├── SRR4053795_sorted.tdf
    │       │   ├── SRR4053795_sorted_genes.ent.gz
    │       │   ├── SRR4053795_sorted_genes.out.gz
    │       │   ├── SRR4053795_sorted_genes.uni.gz
    │       │   ├── SRR4053795_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053795_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053795_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053795_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053795_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053795_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053795_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053795_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053795_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053795_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053795_sorted_transcripts.ent.gz
    │       │   ├── SRR4053795_sorted_transcripts.out.gz
    │       │   ├── SRR4053796_quantification.log
    │       │   ├── SRR4053796_sorted.tdf
    │       │   ├── SRR4053796_sorted_genes.ent.gz
    │       │   ├── SRR4053796_sorted_genes.out.gz
    │       │   ├── SRR4053796_sorted_genes.uni.gz
    │       │   ├── SRR4053796_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053796_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053796_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053796_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053796_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053796_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053796_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053796_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053796_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053796_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053796_sorted_transcripts.ent.gz
    │       │   ├── SRR4053796_sorted_transcripts.out.gz
    │       │   ├── SRR4053802_quantification.log
    │       │   ├── SRR4053802_sorted.tdf
    │       │   ├── SRR4053802_sorted_genes.ent.gz
    │       │   ├── SRR4053802_sorted_genes.out.gz
    │       │   ├── SRR4053802_sorted_genes.uni.gz
    │       │   ├── SRR4053802_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053802_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053802_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053802_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053802_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053802_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053802_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053802_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053802_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053802_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053802_sorted_transcripts.ent.gz
    │       │   ├── SRR4053802_sorted_transcripts.out.gz
    │       │   ├── SRR4053803_quantification.log
    │       │   ├── SRR4053803_sorted.tdf
    │       │   ├── SRR4053803_sorted_genes.ent.gz
    │       │   ├── SRR4053803_sorted_genes.out.gz
    │       │   ├── SRR4053803_sorted_genes.uni.gz
    │       │   ├── SRR4053803_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053803_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053803_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053803_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053803_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053803_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053803_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053803_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053803_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053803_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053803_sorted_transcripts.ent.gz
    │       │   ├── SRR4053803_sorted_transcripts.out.gz
    │       │   ├── SRR4053804_sorted.tdf
    │       │   ├── SRR4053804_sorted_genes.ent.gz
    │       │   ├── SRR4053804_sorted_genes.out.gz
    │       │   ├── SRR4053804_sorted_genes.uni.gz
    │       │   ├── SRR4053804_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053804_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053804_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053804_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053804_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053804_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053804_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053804_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053804_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053804_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053804_sorted_transcripts.ent.gz
    │       │   ├── SRR4053804_sorted_transcripts.out.gz
    │       │   ├── SRR4053805_sorted.tdf
    │       │   ├── SRR4053805_sorted_genes.ent.gz
    │       │   ├── SRR4053805_sorted_genes.out.gz
    │       │   ├── SRR4053805_sorted_genes.uni.gz
    │       │   ├── SRR4053805_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053805_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053805_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053805_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053805_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053805_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053805_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053805_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053805_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053805_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053805_sorted_transcripts.ent.gz
    │       │   ├── SRR4053805_sorted_transcripts.out.gz
    │       │   ├── SRR4053807_sorted.tdf
    │       │   ├── SRR4053807_sorted_genes.ent.gz
    │       │   ├── SRR4053807_sorted_genes.out.gz
    │       │   ├── SRR4053807_sorted_genes.uni.gz
    │       │   ├── SRR4053807_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053807_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053807_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053807_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053807_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053807_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053807_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053807_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053807_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053807_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053807_sorted_transcripts.ent.gz
    │       │   ├── SRR4053807_sorted_transcripts.out.gz
    │       │   ├── SRR4053818_sorted.tdf
    │       │   ├── SRR4053818_sorted_genes.ent.gz
    │       │   ├── SRR4053818_sorted_genes.out.gz
    │       │   ├── SRR4053818_sorted_genes.uni.gz
    │       │   ├── SRR4053818_sorted_rseqc.bam_stat.txt
    │       │   ├── SRR4053818_sorted_rseqc.infer_experiment.txt
    │       │   ├── SRR4053818_sorted_rseqc.junction.bed.gz
    │       │   ├── SRR4053818_sorted_rseqc.junction.xls.gz
    │       │   ├── SRR4053818_sorted_rseqc.junctionSaturation_plot.pdf
    │       │   ├── SRR4053818_sorted_rseqc.qual.boxplot.pdf
    │       │   ├── SRR4053818_sorted_rseqc.qual.heatmap.pdf
    │       │   ├── SRR4053818_sorted_rseqc.read_distribution.txt
    │       │   ├── SRR4053818_sorted_rseqc.splice_events.pdf
    │       │   ├── SRR4053818_sorted_rseqc.splice_junction.pdf
    │       │   ├── SRR4053818_sorted_transcripts.ent.gz
    │       │   ├── SRR4053818_sorted_transcripts.out.gz
    │       │   └── commands
    │       └── trimmomatic
    │           ├── SRR4053795.fastq.gz
    │           ├── SRR4053795_fastqc.html
    │           ├── SRR4053795_fastqc.log
    │           ├── SRR4053795_fastqc.zip
    │           ├── SRR4053795_trimming.log
    │           ├── SRR4053796.fastq.gz
    │           ├── SRR4053796_fastqc.html
    │           ├── SRR4053796_fastqc.log
    │           ├── SRR4053796_fastqc.zip
    │           ├── SRR4053796_trimming.log
    │           ├── SRR4053802.fastq.gz
    │           ├── SRR4053802_fastqc.html
    │           ├── SRR4053802_fastqc.log
    │           ├── SRR4053802_fastqc.zip
    │           ├── SRR4053802_trimming.log
    │           ├── SRR4053803.fastq.gz
    │           ├── SRR4053803_fastqc.html
    │           ├── SRR4053803_fastqc.log
    │           ├── SRR4053803_fastqc.zip
    │           ├── SRR4053803_trimming.log
    │           ├── SRR4053804.fastq.gz
    │           ├── SRR4053804_fastqc.html
    │           ├── SRR4053804_fastqc.zip
    │           ├── SRR4053805.fastq.gz
    │           ├── SRR4053805_fastqc.html
    │           ├── SRR4053805_fastqc.zip
    │           ├── SRR4053807.fastq.gz
    │           ├── SRR4053807_fastqc.html
    │           ├── SRR4053807_fastqc.zip
    │           ├── SRR4053818.fastq.gz
    │           ├── SRR4053818_fastqc.html
    │           ├── SRR4053818_fastqc.zip
    │           └── commands
    ├── src
    ├── tmp
    └── venv    
    
Public Domain notice
====================

National Center for Biotechnology Information.

This software is a "United States Government Work" under the terms of the United States
Copyright Act. It was written as part of the authors' official duties as United States
Government employees and thus cannot be copyrighted. This software is freely available
to the public for use. The National Library of Medicine and the U.S. Government have not
 placed any restriction on its use or reproduction.

Although all reasonable efforts have been taken to ensure the accuracy and reliability
of the software and data, the NLM and the U.S. Government do not and cannot warrant the
performance or results that may be obtained by using this software or data. The NLM and
the U.S. Government disclaim all warranties, express or implied, including warranties
of performance, merchantability or fitness for any particular purpose.

Please cite NCBI in any work or product based on this material.
    