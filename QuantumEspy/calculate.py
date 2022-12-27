import click 
import os

@click.command()
@click.argument("-scf", type=click.PATH(False))
@click.argument("-espr", prompt="Directory of Self-Consistent Calculus input file")
def calc_scf(scf, espresso):
    if os.system("plocate espressp.scf.in") == True:
        return os.system(f"/{scf}/bin/pw.x {espresso}/espresso.scf.inp > {espresso}/espresso.scf.out")
    else:
        return "No input file generated"

