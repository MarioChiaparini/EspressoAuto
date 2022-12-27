import click 
import os 
import sys
#create the scf file for the calculation
@click.command()
@click.argument("-pse", prompt="Enter pseudo Potentials")
@click.argument("-scf", prompt="Input file for Self-Conscistent Calculation", type=click.PATH(False))
def scf_control(pseudopot, inpfile,tstress,tprnfor, outdir):
    with open(inpfile) as file:
        #control
        file.write(
            "&control"\
                "calculation='scf'," \
                    "restart_mode='from_scratch'," \
                        f"tstress='{tstress}'," \
                            f"tprnfor='{tprnfor}'," \
                                "prefix='alas'," \
                                    f"pseudo_dir='{pseudopot}/'" \
                                        "/" 

        )

#def scf_system(ibrav, celldm, )
#        #system
#        file.write(
#            "&system"\

#        )
        
        #electrons


OPTIONS = {
    "sh":"Shellfile",
    "jr":"Jar file"
}

#burai open
@click.command()  
@click.argument("-burai", prompt="Burai directory", type=click.PATH(False))
@click.argument("-jre", prompt="JRE directory", type=click.PATH(False))
@click.argument("-file", prompt="What burai file", type=click.Choice(OPTIONS.keys()))
def open_burai(burai,jre, file):
    if file == "sh":
        return os.system(f"{burai}/burai.sh")
    else:
        return os.system(f"java --module-path /usr/share/openjfx/lib --add-modules=javafx.base,javafx.controls,javafx.fxml,javafx.graphics,javafx.media,javafx.swing,javafx.web -jar .{burai}/burai.jar $@")            

if __name__=="main":
    open_burai()

