<h1 align="center">Stand Are Nodes Project</h1> 

<p align="center">Welcome to the Stand Are Nodes Project! This draft aims to produce a POC for the evaluation of the relationships between norms in a visual way <i>(but not only)</i> to evaluate the cyber threat impact on normative ecosystems.</p> 

<p align="center">A demo will take place soon at <a href="https://sigspatial2022.sigspatial.org/">SIG Spatial 2022.</a></p>

<h2>Setup</h2>

<p>
You need to install python3 dependencies before running. All of them are in the <i>requirements.txt</i> file. Execute it like this :
</p>

```bash
python3 pip install -r requirements.txt
```

<p>
You need to install geos library :
</p>
<p>
If you are using aptitude :
</p>
```bash
sudo apt install libgeos-dev
```
<p>
or Fedora :
</p>
```bash
sudo yum install geos-devel
```
<p>
or Arch :
</p>
```bash
sudo pacman -Sy geos
```
<h2>Configuration</h2>

<p>Before running the script you have to create an input JSON file (Put it in the directory <i>databases</i>). It is concerned with the norms you want to analyze. If you need to analyze an ISO ecosystem, you have to create a file in which each entry is a norm of the ISO ecosystem. You will need the code of the norm like a key, the likes to the iso preview of the norm, the title of this norm, and fill the file like this :</p>

<b>isolist.json :</b>
```json
{
    "ISO 19101-1:2014": {
        "lien": "https://www.iso.org/obp/ui/#iso:std:iso:19101:-1:en",
        "nom": "ISO 19101-1:2014 Geographic information — Reference model — Part 1: Fundamentals"
    },
    "ISO 19101-2:2018": {
        "lien": "https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:en",
        "nom": "ISO 19101-2:2018 Information géographique — Modèle de réference — Partie 2: Imagerie"
    },

    [...]

}
```

<h2>Running</h2>

To run scripts, use the shell commands  :

```
$ chmod u+x stand_are_nodes.sh
$ ./stand_are_nodes.sh
           __                          .___                                                          .___                   
  ______ _/  |_  _____      ____     __| _/     _____    _______    ____         ____     ____     __| _/   ____     ______ 
 /  ___/ \   __\ \__  \    /    \   / __ |      \__  \   \_  __ \ _/ __ \       /    \   /  _ \   / __ |  _/ __ \   /  ___/ 
 \___ \   |  |    / __ \_ |   |  \ / /_/ |       / __ \_  |  | \/ \  ___/      |   |  \ (  <_> ) / /_/ |  \  ___/   \___ \  
/____  >  |__|   (____  / |___|  / \____ |      (____  /  |__|     \___  >     |___|  /  \____/  \____ |   \___  > /____  > 
     \/               \/       \/       \/           \/                \/           \/                \/       \/       \/  
Welcome in Stand are Nodes project !
Options:
    1. Populate the database
    2. Vizualize the database
    Other to skip and end
Choose your option here :
```

<h3><b>(Option 1) Populate the database :</b></h3>

<p>Use choose this option to get all dependencies present in norms that are in the file you've just filled before. This script will store links of all dependencies present in the normative text <i>(public access part)</i>.</p>

```
Choose your option here :
1
Precise the json in file name (with json extension) :
isolist.json
Precise the json output file name (with json extension) :
data.json
```

<p>You have now all dependencies present (under links form) in the norms you filled in the input file in the output file which has approximately the same format as your input file.</p>

<h3><b>(Option 2) Vizualize the database :</b></h3>

<p><b>⚠️<i>To run this option you firstly need to run the first option if you don't run it before.</i>⚠️</b></p>

<p>For this option, you will have to precise two input files. The first one is the output file from the first option. The second one is the input file from the first option. Finally, you need to give a name to the output file with the <i>.html</i> extension.</p>

```
Choose your option here :
2
Precise the json in file name (with json extension) :
data.json
Precise the json file used in input of the database (with json extension) :
isolist.json
Precise the name output file name (with html extension) :
iso_net.html
```

<p>Next, we propose 2 ways to visualize your database :</p>
<h4><b>1. Network</b></h4>
<p><img src=img/iso19100.png  width="500" height="400"></p>
<h4><b>2. Circle (Bokeh)</b></h4>
<p><img src=img/bokeh_plot.png  width="400" height="400"></p>

<p><b>⚠️<i>Visualization going in the results file.</i>⚠️</b></p>