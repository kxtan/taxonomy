#!/usr/bin/env python
"""
Command line tool for taxonomy operations
"""

import click
#import modules
#from nlib import csvops
#from nlib import utils


#@click.version_option(modules.__version__)
@click.group()
def cli():
    """Taxonomy operations tool"""

@cli.command("generate")
@click.argument("fileinput")
@click.option("--fileoutput", help="path to output file")
@click.option("--identifier", help="identifier of sentences")
@click.option("--textcolumn", help="column name of sentences")
@click.option("--method", help="taxonomy generation method")
@click.option("--outputstyle", help="output style")
def generate(fileinput, fileoutput, identifier, textcolumn, method, outputstyle):
    """Generate taxonomy based on selected method
    """
    click.echo(fileinput)
    click.echo(fileoutput)
    click.echo(identifier)
    # if not file and not groupby and not applyname and not func:
    #     click.echo("--file and --column and --applyname --func are required")
    #     sys.exit(1)

    # click.echo(
    #     "Processing csvfile: {file} and groupby name: {groupby} and applyname: {applyname}".format(
    #         file=file, groupby=groupby, applyname=applyname
    #     )
    # )
    # # Load Plugins and grab correct one
    # plugins = utils.plugins_map()
    # appliable_func = plugins[func]
    # res = csvops.group_by_operations(
    #     data=file,
    #     groupby_column_name=groupby,
    #     apply_column_name=applyname,
    #     func=appliable_func,
    # )
    # click.echo(res)


# @cli.command("listfuncs")
# def listfuncs():
#     """Lists functions that can be applied to a GroupBy Operation
#     Example Usage:
#     ./csvcli.py listfuncs
#     Appliable Functions: ['npmedian', 'npsum', 'numpy', 'tanimoto']
#     """

#     funcs = utils.appliable_functions()
#     click.echo("Appliable Functions: {funcs}".format(funcs=funcs))

if __name__ == "__main__":
    cli()