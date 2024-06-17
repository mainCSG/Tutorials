Repository For Packaging Simulator Code Into A Webpage
=======================================

# Conda Environment Setup 
1) Run `conda env create -f qudipy_web_environment.yml -v`
to create a conda environment with the required dependencies.
2) Activate the conda environment in the IDE of choice.

Copy the most recent simulator code into this folder on a user's machine.
Once Jupyter notebooks are run on a user's local machine, copy the tutorials' folder with the notebooks into the source directory. 

Then run the following from:

`docs/` directory: 

1) `make clean`

2) `make html`

`maincsg.github.io/` directory

1) `git add .`

2) `git commit -m"<some message>"`

3) `git push`


# create conda environment with necessary package dependencies
conda create --name qudipy_web --file 'QuDiPy webpage package list'.txt

# install sphinx in environment
sudo apt install python3-sphinx

# install sphinx extension for Jupyter notebooks
conda install -c conda-forge nbsphinx

# install myst_parser
# MyST is a rich and extensible flavor of Markdown meant for technical documentation and publishing
conda install -c conda-forge myst-parser

# install sphinx theme
pip install sphinx-rtd-theme