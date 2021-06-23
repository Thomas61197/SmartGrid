### to do:
"Aanpak algoritmen, Gebruik, docs toevoegen bij Structuur?
- Alle code om de resultaten uit de presentatie te produceren is aanwezig.
- De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
- Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


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



 ## Aanpak algoritmen 
 To Do 
 
 ```console
python main.py
```
- **Baseline / greedy /simulated annealing**
- **Scenario 1 scenario 2**

- hoe de resultaten te reproduceren zijn, via een interface (command line), 
- argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, 
- of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.<br>



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

To Do
Een voorbeeldje kan gerund worden door aanroepen van:

```console
python main.py
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de vier benodigde classes voor deze case
  - **/code/visualisation**: bevat de matplotlib code voor de visualisatie
- **/data**: bevat de verschillende databestanden die benodigd zijn om de algoritmen te runnen 
  - **/data/Huizen&Batterijen** bevat de databestanden van de verschillende wijken met huizen en batterijen
  - **/data/solutions** bevat de databestanden van resultaten opgeslagen als objecten verkregen met de algoritmen

To docs? - **/docs**: 


## Auteurs
Ysanne de Graaf <br>
Thomas Boer <br>
Thijs Wijnheijmer <br>


