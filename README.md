# Education
This repository was created to share basic python scripts to make life easier for students (and teachers). In order to use the modules just place the `module.py` file in the same directory as your script and add the `import module` line in your code. 

The following modules are present:

### Cashflow:

A simple cashflow diagram plotter, takes arrays an input and saves the plot as a .png file

`import cashflow`

`cashflow.diagram (time, value, cashflow, 'g', 'k', '$', 'diagram.png', [12,9], bar = False)`

### Python grep:

A python based implementation of the Unix utility grep, with suport for pattern and regular expression matching.

`python grep.py -f [FILENAME] -p "[PATTERN]"`
