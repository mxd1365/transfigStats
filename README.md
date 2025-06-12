This is a command line utility to view some basic statistics about transfigured gems in PoE1. It uses dat from poe.ninja.

It pulls the current values of a transfiguration gems to give you the current mean, median and standard deviation of all possible outcomes of the transfiguration shrine in the labyrinth. This assumes you are selecting the option "Transform a Skill Gem to be a random Transfigured Gem of the same colour".

This will help you choose what color gem to use when running the labyrinth for profit.

***Installation***
1. Unzip transfigStats.zip into desired directory.
2. Run transfigStats.exe in command line.

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

****Example Output****

All prices are in chaos
```
--------------RED GEMS----------------
RED gems: mean of profit: 218.6271986166008, median of profit: 174.03, normal standard deviation of gem values: 0.004786885908996312

Top 10 RED transfiguration gems
        1. Boneshatter of Complex Trauma: 537.09
        2. Volcanic Fissure of Snaking: 340.16
        3. Smite of Divine Judgement: 210.13
        4. Dominating Blow of Inspiring: 179.03
        5. Molten Strike of the Zenith: 179.03
        6. Shield Crush of the Chieftain: 179.03
        7. Summon Flame Golem of Hordes: 179.03
        8. Tectonic Slam of Cataclysm: 179.03
        9. Summon Stone Golem of Hordes: 165.33
        10. Earthquake of Amplification: 135.82
        11. Animate Guardian of Smiting: 93.8
        12. Summon Stone Golem of Safeguarding: 86.0
        13. Earthshatter of Prominence: 80.01
        14. Bladestorm of Uncertainty: 60.0
        15. Rage Vortex of Berserking: 59.5
        16. Ground Slam of Earthshaking: 58.0
        17. Glacial Hammer of Shattering: 53.0
        18. Infernal Blow of Immolation: 46.0
        19. Frozen Legion of Rallying: 40.0
        20. Ice Crash of Cadence: 40.0

Top 10 cheapest RED gems
        1. Sunder: 5.0
        2. Cleave: 5.5
        3. Chain Hook: 6.2
        4. Infernal Blow: 6.2
        5. Frozen Legion: 6.4
        6. Tectonic Slam: 6.4
        7. Perforate: 6.5
        8. Holy Flame Totem: 6.8
        9. Dread Banner: 7.5
        10. Exsanguinate: 7.6


--------------GREEN GEMS----------------
GREEN gems: mean of profit: 218.31450015417823, median of profit: 174.43, normal standard deviation of gem values: 0.0020267721354693545

Top 10 GREEN transfiguration gems
        1. Animate Weapon of Ranged Arms: 769.83
        2. Elemental Hit of the Spectrum: 537.09
        3. Lightning Strike of Arcing: 300.45
        4. Mirror Arrow of Bombarding Clones: 270.34
        5. Detonate Dead of Scavenging: 268.54
        6. Frost Blades of Katabasis: 220.21
        7. Explosive Trap of Shrapnel: 184.62
        8. Lancing Steel of Spraying: 184.27
        9. Dual Strike of Ambidexterity: 179.03
        10. Tornado of Elemental Turbulence: 179.03
        11. Frenzy of Onslaught: 150.82
        12. Poisonous Concoction of Bouncing: 139.42
        13. Cremation of Exhuming: 132.42
        14. Bladefall of Volleys: 123.71
        15. Ethereal Knives of Lingering Blades: 123.01
        16. Caustic Arrow of Poison: 120.0
        17. Detonate Dead of Chain Reaction: 116.95
        18. Mirror Arrow of Prismatic Clones: 114.68
        19. Toxic Rain of Withering: 113.61
        20. Cremation of the Volcano: 110.0

Top 10 cheapest GREEN gems
        1. Plague Bearer: 4.6
        2. Poisonous Concoction: 5.0
        3. Alchemist's Mark: 6.8
        4. Viper Strike: 7.2
        5. Explosive Arrow: 7.5
        6. Dual Strike: 7.99
        7. Mirror Arrow: 8.0
        8. Blade Flurry: 8.3
        9. Cremation: 8.8
        10. Explosive Trap: 9.1


--------------BLUE GEMS----------------
BLUE gems: mean of profit: 228.70174741896759, median of profit: 172.53, normal standard deviation of gem values: 0.0014868866320704886

Top 10 BLUE transfiguration gems
        1. Vortex of Projection: 558.38
        2. Crackling Lance of Branching: 465.48
        3. Righteous Fire of Arcane Devotion: 465.48
        4. Galvanic Field of Intensity: 358.06
        5. Summon Skeletons of Mages: 358.06
        6. Soulrend of the Spiral: 269.03
        7. Penance Brand of Dissipation: 266.75
        8. Ice Nova of Frostbolts: 257.8
        9. Summon Chaos Golem of Hordes: 212.42
        10. Frostblink of Wintry Blast: 196.93
        11. Kinetic Blast of Clustering: 179.03
        12. Spark of the Nova: 179.03
        13. Power Siphon of the Archmage: 155.22
        14. Raise Zombie of Falling: 151.61
        15. Raise Zombie of Slamming: 140.32
        16. Glacial Cascade of the Fissure: 139.02
        17. Lightning Conduit of the Heavens: 125.61
        18. Ice Spear of Splitting: 125.02
        19. Flame Surge of Combusting: 119.5
        20. Arc of Surging: 112.02

Top 10 cheapest BLUE gems
        1. Divine Retribution: 6.5
        2. Rolling Magma: 8.0
        3. Dark Pact: 9.0
        4. Essence Drain: 9.0
        5. Lightning Spire Trap: 9.1
        6. Siphoning Trap: 9.2
        7. Storm Call: 9.2
        8. Summon Raging Spirit: 9.2
        9. Vortex: 9.3
        10. Eye of Winter: 9.5
```
