import os
from fontTools.designspaceLib import DesignSpaceDocument
# Change this import:
from ufoProcessor.ufoOperator import UFOOperator 

def generate_clean_instances(designspace_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ds = DesignSpaceDocument.fromfile(designspace_path)
    
    # 1. Strip rules and filter instances
    ds.rules = []
    target_styles = ["Thin", "Regular", "Bold"]
    ds.instances = [inst for inst in ds.instances if inst.styleName in target_styles]

    # 2. Initialize using the specific submodule class
    operator = UFOOperator(ds)
    
    # 3. Load the fonts into the operator
    operator.loadFonts()

    for instance in ds.instances:
        print(f"Interpolating: {instance.styleName}...")
        
        # 1. Get the dictionary of coordinates. 
        # Note the () at the end because it's a method!
        loc = instance.location
        
        # 2. Pass 'loc' (the dictionary) as the first argument, 
        # not 'instance' (the object).
        instance_ufo = operator.makeOneInstance(loc, doRules=False)
        
        # 3. Use the stylename for the filename
        if "Kanji" in output_dir:
            out_path = os.path.join(output_dir, f"M+1p-{instance.styleName}.ufo")
        else:
            out_path = os.path.join(output_dir, f"MPLUS1-{instance.styleName}.ufo")
        instance_ufo.save(out_path)
        print(f"Saved: {out_path}")

if __name__ == "__main__":
    # Adjust these paths to your local setup
    DS_PATH = "sources/MPLUS1/masters/MPLUS1.designspace"
    OUT_DIR = "sources/MPLUS1/instances/"
    
    generate_clean_instances(DS_PATH, OUT_DIR)

    DS_PATH = "sources/MPLUSKanji/masters/M+1p.designspace"
    OUT_DIR = "sources/MPLUSKanji/instances/"
    
    generate_clean_instances(DS_PATH, OUT_DIR)