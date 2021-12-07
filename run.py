#!/usr/bin/env python
"""
Command line tool for taxonomy operations
"""

import click
from modules import extract, util
import click_spinner
#from nlib import csvops
#from nlib import utils


#@click.version_option(modules.__version__)
@click.group()
def cli():
    """Taxonomy operations tool"""

@cli.command("keywords")
@click.argument("fileinput")
@click.argument("fileoutput")
@click.option("--identifier", help="identifier of sentences")
@click.option("--textcolumn", help="column name of sentences")
@click.option("--method", help="taxonomy generation method")
@click.option("--outputstyle", help="output style")
def keywords(fileinput, fileoutput, identifier, textcolumn, method, outputstyle):
    """Generate taxonomy based on selected method
    """

    click.echo(f"Reading file from : {fileinput}")
    input_df = util.read_file(fileinput)
    
    click.echo("Processing file...")
    if identifier is None:
        identifier = "id"
    if textcolumn is None:
        textcolumn = "text"

    text_dict = util.generate_text_dict(input_df, identifier, textcolumn)

    keywords_dict = {}

    if method is None:
        click.echo("Defaulting to using Flair to generate keywords")
        method = "flair"

    click.echo("Generating keywords...")

    if method == "flair":
        with click_spinner.spinner():
            keywords_dict = extract.flair_keywords(text_dict)
    else:
        click.echo(f"Unknown method : {method}")
        click.Abort()

    keywords_df = util.keywords_to_df(keywords_dict)

    if outputstyle is None:
        click.echo("Defaulting to compact output")
        outputstyle = "compact"

    if outputstyle == "compact":
        output_df = util.compact_df(keywords_df)
        click.echo(f"Storing output to : {fileoutput}")
        output_df.to_csv(fileoutput)
    else:
        click.echo(f"Outputstyle {outputstyle} is not supported")

if __name__ == "__main__":
    cli()