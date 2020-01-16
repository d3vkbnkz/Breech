#!./env/bin/python

from multiprocessing import Pool
from tqdm import tqdm
import requests
import datetime
import click
import time
import sys
import os

BANNER = """
____________________________________________________________
            ____                     _     
            | __ ) _ __ ___  ___  ___| |__  
            |  _ \| '__/ _ \/ _ \/ __| '_ \ 
            | |_) | | |  __/  __/ (__| | | |
            |____/|_|  \___|\___|\___|_| |_|

                Website Directory Scanner
            Made by @d3vkbnkz with <3 in Python
                      Version 1.0
____________________________________________________________
"""


class Application:
    def __init__(self):
        self.results    = []
        self.target     = None
        self.input      = None

    def check_URL(self, line):
        try:
            response = requests.get(line, headers={'User-Agent': 'XY'})
            if response.status_code == 200:
                # click.echo(click.style('[+] Found: %s' % line, bold=True, fg='green'), nl=False)
                self.results.append(line)
                with open('results.txt', mode='a') as file:
                    click.echo(line, file=file, nl=False)
        except KeyboardInterrupt:
            return

    def run(self):
        try:
            if os.path.exists(self.input) == True:
                # Start.
                start_time = datetime.datetime.now()
                click.echo(click.style('[%s] Starting...\n' % start_time, bold=True))
                with open(self.input, 'r') as file:
                    lines = file.readlines()
                    for line in tqdm(lines):
                        line = self.target + '/' + line
                        self.check_URL(line)
                # End.
                end_time = datetime.datetime.now()
                # Results.
                click.echo('\n[~] Found %s entries.' % len(self.results))
                for result in self.results:
                    click.echo(click.style('[+] Found: %s' % result, bold=True, fg='green'), nl=False)
                click.echo('\n[%s] Finished. Time: %ss\n' % (end_time, (end_time - start_time).total_seconds()))
            else:
                click.echo('[-] Could not open %s' % self.input)
        except KeyboardInterrupt:
            exit()

@click.command()
@click.option('-t', '--target', help='Sets the target URL.', required=True)
@click.option('-i', '--input', help='Sets the input file.', required=True, type=str)
def main(target, input):
    application = Application()

    application.target     = target
    application.input      = input

    application.run()

if __name__ == '__main__':
    click.echo(BANNER)
    main()