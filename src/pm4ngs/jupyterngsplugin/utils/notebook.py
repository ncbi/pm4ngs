import subprocess
from IPython.display import Javascript


def save_2_html(nb_name):
    script = '''
    require(["base/js/namespace"],function(Jupyter) {
        Jupyter.notebook.save_checkpoint();
    });
    '''

    Javascript(script)
    subprocess.run(["jupyter", "nbconvert", "--to", "html", nb_name])
