### Vereisen:
- Eventuele afhankelijkheden (dependencies) staan in een requirements.txt of soortgelijks.
- Alle code om de resultaten uit de presentatie te produceren is aanwezig.


- De case waar de studenten mee bezig geweest zijn is duidelijk geïntroduceerd in de README.



- De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.


- Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SmartGrid

Veel huizen hebben tegenwoordig zonnepanelen om zelf energie mee te produceren. Vaak produceren de zonnepanelen meer dan voor eigen consumptie nodig is. Dit overschot kan worden terugverkocht aan de leverancier, maar de infrastructuur (het grid) is daar veelal niet op berekend. Om de pieken in consumptie en productie te kunnen managen moeten er batterijen geplaatst worden. Voor een feasibility study zijn drie dummy-woonwijken opgesteld, met daarin vijf batterijen. De huizen hebben zonnepanelen met een maximale output, de batterijen hebben een maximale capaciteit en kosten 5000 per stuk. Exacte data is te vinden in >>> deze bestanden. <<<

De kabels om huizen en batterijen te verbinden liggen op de gridlijnen kosten 9 van één grid-segment.

Het doel van SmartGrid is om de huizen te met batterijen te verbinden op de meest slimme configuratie van het kabel netwerk waarbij de kosten worden geminimaliseerd. 

Algemene vereisten: 
- De maximumcapaciteit van de huizen die van de batterijen niet mag overschrijden.
- De afstand van een huis tot een batterij wordt berekend volgens de Manhattan distance. 
- Kabels mogen gridpunten met een huis passeren. 
- Batterijen mogen niet aan elkaar verbondenden zijn. Ook niet via een huis.
- Een huis mag niet aan meerdere batterijen verbonden zijn.

#### Scenario 1
- Elk huis heeft een eigen unieke kabel nodig naar de batterij.
- Er mogen meerdere kabels over dezelfde gridsegmenten lopen. Het blijven echter wel unieke kabels en leveren geen kostenvermindering op.

#### Scenario 2
- Huizen mogen wel via eenzelfde kabel aan een batterij verbonden zijn. Ze mogen dus een kabel delen.

## Aanpak Algoritmen




