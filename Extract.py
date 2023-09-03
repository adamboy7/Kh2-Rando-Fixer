from zipfile import ZipFile
import shutil

things_I_Care_About = ["TrsrList.yml", "sys.yml", "PlrpList.yml", "modified_synth_reqs.bin", "modified_synth.bin", "modified_puzzle.bin","LvupList.yml", "ItemList.yml", "FmlvList.yml", "BonsList.yml", "preview.png"]
files_to_patch = []

# TrsrList = Chests ✓
# sys = Seed on title screen, nice to have ✓
# PlrpList = Starting stats, items, and slots ✓
# modified_synth_reqs = Synth recipe? ✓
# modified_synth = Synth ✓
# modified_puzzle = Puzzle ✓
# LvupList = Level up rewards ✓
# ItemList = Weapon stats and abilities ✓
# FmlvList = Form rewards ✓
# BonsList = Bonuses ✓

with ZipFile('randoseed.zip', 'r') as zipObj:
   listOfiles = zipObj.namelist()
   for file in listOfiles:
       if file in things_I_Care_About:
           zipObj.extract(file, "Fixed")
           files_to_patch.append(file)
zipObj.close()

mod = open("mod.yml", "w")
mod.write("assets:\n")

# sys.bar
if "sys.yml" in files_to_patch:
    mod.write("- method: binarc\n  multi:\n  - name: msg/us/sys.bar\n  - name: msg/uk/sys.bar\n  name: msg/jp/sys.bar\n  source:\n  - method: kh2msg\n    name: sys\n    source:\n    - language: en\n      name: sys.yml\n    type: list\n")

# 00battle.bin
if "FmlvList.yml" in files_to_patch or "LvupList.yml" in files_to_patch or "BonsList.yml" in files_to_patch or "PlrpList.yml" in files_to_patch:
    mod.write("- method: binarc\n  name: 00battle.bin\n  source:\n")
    if "FmlvList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: fmlv\n    source:\n    - name: FmlvList.yml\n      type: fmlv\n    type: List\n")
    if "LvupList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: lvup\n    source:\n    - name: LvupList.yml\n      type: lvup\n    type: List\n")
    if "BonsList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: bons\n    source:\n    - name: BonsList.yml\n      type: bons\n    type: List\n")
    if "PlrpList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: plrp\n    source:\n    - name: PlrpList.yml\n      type: plrp\n    type: List\n")

# 03system.bin
if "TrsrList.yml" in files_to_patch or "ItemList.yml" in files_to_patch:
    mod.write("- method: binarc\n  name: 03system.bin\n  source:\n")
    if "TrsrList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: trsr\n    source:\n    - name: TrsrList.yml\n      type: trsr\n    type: list\n")
    if "ItemList.yml" in files_to_patch:
        mod.write("  - method: listpatch\n    name: item\n    source:\n    - name: ItemList.yml\n      type: item\n    type: list\n")

# jiminy.bar
if "modified_puzzle.bin" in files_to_patch:
    mod.write("- method: binarc\n  multi:\n  - name: menu/us/jiminy.bar\n  - name: menu/fr/jiminy.bar\n  - name: menu/gr/jiminy.bar\n  - name: menu/it/jiminy.bar\n  - name: menu/sp/jiminy.bar\n  - name: menu/uk/jiminy.bar\n  name: menu/fm/jiminy.bar\n  source:\n  - method: copy\n    name: puzz\n    source:\n    - name: modified_puzzle.bin\n    type: jimidata\n")

# mixdata.bar
if "modified_synth.bin" in files_to_patch or "modified_synth_reqs.bin" in files_to_patch:
    mod.write("- method: binarc\n  multi:\n  - name: menu/us/mixdata.bar\n  - name: menu/fr/mixdata.bar\n  - name: menu/gr/mixdata.bar\n  - name: menu/it/mixdata.bar\n  - name: menu/sp/mixdata.bar\n  - name: menu/uk/mixdata.bar\n  name: menu/fm/mixdata.bar\n  source:\n")
    if "modified_synth.bin" in files_to_patch:
        mod.write("  - method: copy\n    name: reci\n    source:\n    - name: modified_synth.bin\n    type: synthesis\n")
    if "modified_synth_reqs.bin" in files_to_patch:
        mod.write("  - method: copy\n    name: cond\n    source:\n    - name: modified_synth_reqs.bin\n    type: synthesis\n")

shutil.copy("icon.png", "Fixed")
mod.close()
shutil.move("mod.yml", "Fixed")
shutil.make_archive("Fixed", "zip", "Fixed")
