### to do:
"Aanpak algoritmen, docs toevoegen bij Structuur?
- Alle code om de resultaten uit de presentatie te produceren is aanwezig.
- De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
- Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Vaak produceren de zonnepanelen meer dan voor eigen consumptie nodig is. Dit overschot kan worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden. Voor een feasibility study zijn drie dummy-woonwijken opgesteld, met daarin vijf batterijen. De huizen hebben zonnepanelen met een maximale output en de batterijen hebben een maximale capaciteit. Exacte details zijn te vinden in [deze bestanden](https://github.com/Thomas61197/SmartGrid/tree/main/data/Huizen%26Batterijen). Kabels om huizen en batterijen te verbinden liggen op de gridlijnen. De kosten van kabels zijn afhankeljk van de lengte en kosten 9 per grid-segment. De batterijen kosten 5000 per stuk.

Het doel van SmartGrid is om met de meest slimme configuratie van het kabel netwer, de huizen met batterijen te verbinden waarbij de kosten worden geminimaliseerd. 

Voor een valide oplossing gelden de volgende eisen:<br>
- De maximumcapaciteit van de huizen die van de batterijen niet mag overschrijden.
- De afstand van een huis tot een batterij wordt berekend volgens de Manhattan distance. 
- Kabels mogen gridpunten met een huis passeren. 
- Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
- Een huis mag niet aan meerdere batterijen verbonden zijn.


Daarnaast zijn er twee scenario's voor het leggen van de kabels:<br>
#### Scenario 1
- Elk huis heeft een eigen unieke kabel nodig naar de batterij.
- Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.

#### Scenario 2
- Huizen mogen wel via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.<br><br>


## Aan de slag

### Vereisten
Deze codebase is geschreven in Python 3.7. Alle benodigde packages zijn beschreven in requirements.txt 

Onderstaand zijn de instructies beschreven om deze te installerenn en de code succesvol te draaien:


Via pip:

```console
pip install -r requirements.txt
```


Of via conda:

```console
conda install --file requirements.txt
```

 ## Aanpak algoritmen 
 
- hoe de resultaten te reproduceren zijn, via een interface (command line), 
- argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, 
- of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.<br>

 
Keuze uit: scenario 1 of scenario 2 

Wijken met district nummer 1, 2 of 3 

Algoritmen: 

baseline!!!

- district_number: "1", "2" of "3"
- greedy_version: None, 1, 2, of 3
- run_simulated_annealing = "yes" of "no"
- run_hill_climber = "yes" of "no"
- generate_output = "yes" of "no"

 ```console
python main.py
```

Visualisatie:



#### Een voorbeeldje kan gerund worden door aanroepen van:

 ```console
python main.py
```


### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de vier benodigde classes voor deze case
  - **/code/visualisation**: bevat de matplotlib code voor de visualisatie<br>
  
- **/data**: bevat de verschillende databestanden die benodigd zijn om de algoritmen te runnen 
  - **/data/Huizen&Batterijen** bevat de databestanden van de verschillende wijken met huizen en batterijen
  - **/data/solutions** bevat de databestanden van resultaten opgeslagen als objecten verkregen met de algoritmen<br>

- **/docs**: bevat gevisualiseerde resultaten van de grid configuraties
  - **/docs/final** bevat visualisaties van de grid configuraties gesorteerd per district verkregen met het simulated annealling algoritme
  - **/docs/** output.json<br>


## Auteurs
Ysanne de Graaf <br>
Thomas Boer <br>
Thijs Wijnheijmer <br>


