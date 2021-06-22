### to do:
- Eventuele afhankelijkheden (dependencies) staan in een requirements.txt of soortgelijks.
- Alle code om de resultaten uit de presentatie te produceren is aanwezig.

+ De case waar de studenten mee bezig geweest zijn is duidelijk geïntroduceerd in de README.

- De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.

- Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Vaak produceren de zonnepanelen meer dan voor eigen consumptie nodig is. Dit overschot kan worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden. Voor een feasibility study zijn drie dummy-woonwijken opgesteld, met daarin vijf batterijen. De huizen hebben zonnepanelen met een maximale output en de batterijen hebben een maximale capaciteit. Exacte details zijn te vinden in >>> deze bestanden. <<< Batterijen kosten 5000 per stuk. Kabels om huizen en batterijen te verbinden liggen op de gridlijnen de kosten van kabels zijn afhankeljk van de lengte namelijk 9 per grid-segment.

Het doel van SmartGrid is om de huizen te met batterijen te verbinden op de meest slimme configuratie van het kabel netwerk waarbij de kosten worden geminimaliseerd. 

Deze volgende eisen gelden voor een valide oplossing: 
- De maximumcapaciteit van de huizen die van de batterijen niet mag overschrijden.
- De afstand van een huis tot een batterij wordt berekend volgens de Manhattan distance. 
- Kabels mogen gridpunten met een huis passeren. 
- Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
- Een huis mag niet aan meerdere batterijen verbonden zijn.


Daarnaast zijn er 
#### Scenario 1
- Elk huis heeft een eigen unieke kabel nodig naar de batterij.
- Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.

#### Scenario 2
- Huizen mogen wel via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.



## Algoritmen 
- **Baseline / greedy /simulated annealing**
- **Scenario 1 scenario 2**

- hoe de resultaten te reproduceren zijn, via een interface (command line), 
- argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, 
- of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.



## Aan de slag

### Vereisten
Deze codebase is geschreven in Python 3.7. Alle benodigde packages zijn beschreven in requirements.txt 

Onderstaand zijn de instructies bescheven om deze te installeeren en de code succesvol te draaien:


Via pip:

```console
pip install -r requirements.txt
```


Of via conda:

```console
conda install --file requirements.txt
```



### Gebruik

Een voorbeeldje kan gerund worden door aanroepen van:

```console
python main.py
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de bokeh code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren

## Auteurs
Ysanne de Graaf <br>
Thomas Boer <br>
Thijs Wijnheijmer <br>


