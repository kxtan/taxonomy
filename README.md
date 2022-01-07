# taxonomy
[![Python application test with Github Actions](https://github.com/kxtan/taxonomy/actions/workflows/python-test.yml/badge.svg?branch=main)](https://github.com/kxtan/taxonomy/actions/workflows/python-test.yml)

Exploration of methods to extract keywords in texts to create a taxonomy. The idea is to combine various methods to generate keywords based on a given text input, currently via command line interface. 

Currently explored methods:

1. [FLAIR](https://github.com/flairNLP/flair)

## Quick Start

### Requirements and Installation

The project is based on Python 3.8+ which we can install a barebones version from [here](https://www.python.org/downloads/) or via [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)

Next, we can clone the repository via [Git](https://git-scm.com/downloads) using the following command:

```
git clone https://github.com/kxtan/taxonomy.git
```

## Usage Example

### Checking CLI parameters

Navigate to the cloned repository location.

Run the following the check available commands: ```python run.py --help```

Expected output:

![image](https://user-images.githubusercontent.com/15542227/148484777-9dd52fa4-b6ed-4cb6-8fbf-dff3d05a2154.png)

The keywords command is the main functionality that we need, to check the required and optional parameters, we can run this command: ```python run.py keywords --help```

Expected output:

![image](https://user-images.githubusercontent.com/15542227/148485562-bc9bb8f8-eb56-4bc6-b419-ade2ef08432c.png)

### Generating keywords

1. We need a csv/tsv file containing rows of unique identifiers and their corresponding texts. Example:

 id | text | 
|  ---  | ----------- | 
| 001 | This is a sentence containing the keyword of WHO |
| 002 | Another sentence with the keyword UNESCO |

2. We will identify the output path for the keywords generated in csv form. Example: ```/output/keywords.csv```

3. Next, we can run the following command to generate the keywords: 

```python run.py keywords /your_input_path/yourfile.csv /your_output_path/yourkeywords.csv```

4. To specify the identifier and text column names, we can simply add optional parameters to the command above:

```python run.py keywords /your_input_path/yourfile.csv /your_output_path/yourkeywords.csv --identifier your_custom_id --textcolumn your_custom_column```

5. Finally, we should have extracted keywords in the output path specified.
