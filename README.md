This is a command line utility to view some basic statistics about transfigured gems in PoE1. It uses dat from poe.ninja.

It pulls the current values of a transfiguration gems to give you the current mean, median and standard deviation of all possible outcomes of the transfiguration shrine in the labyrinth. This assumes you are selecting the option "Transform a Skill Gem to be a random Transfigured Gem of the same colour".

This will help you choose what color gem to use when running the labyrinth for profit.

***Installation***
1. Copy the contents of the dist folder to desired directory
2. Run transfigStats.exe in command line

***Usage***

  usage: transfigStats.exe [-h] [--league LEAGUE] [--topGemListSize TOPGEMLISTSIZE]
                           [--cheapestGemListSize CHEAPESTGEMLISTSIZE]
  
  options:
    -h, --help            show this help message and exit
    --league LEAGUE       The name of the league to search
    --topGemListSize TOPGEMLISTSIZE
                          The number of top gems to show
    --cheapestGemListSize CHEAPESTGEMLISTSIZE
                          The number of cheapest gems to show
