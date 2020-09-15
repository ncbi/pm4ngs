import os
import pandas
import seaborn as sns
import matplotlib.pyplot as plt


def tpmcalculator_distribution_plot(column, output_folder, output_suffix, fig_size):
    """
    Parse a TPMCalculator output and create distribution plot
    :param columns: TPMCalculator output column to plot
    :param output_folder: TPMCalculator output folder
    :param output_folder: TPMCalculator output file name sufix
    :param fig_size:  Tuple with figure size
    :return: matplotlib plot
    """
    files = [f for ds, df, files in os.walk(output_folder) for f in files if output_suffix in f]
    matrix_file = os.path.join(output_folder, column + '.tsv')
    if os.path.exists(matrix_file) and os.path.getsize(matrix_file) != 0:
        data = pandas.read_csv(matrix_file, sep='\t')
        f, plot = plt.subplots(figsize=fig_size)
        toPlot = []
        for f in files:
            if f.endswith('.gz'):
                output_suffix_real = output_suffix + '.gz'
            else:
                output_suffix_real = output_suffix
            s = f.replace(output_suffix_real, '')
            if s in data:
                for r in data[s]:
                    toPlot.append([r, s])
        d = pandas.DataFrame(toPlot, columns=[column, 'Sample'])
        sns.boxplot(y='Sample', x=column, data=d, orient="h", palette="Set2")
