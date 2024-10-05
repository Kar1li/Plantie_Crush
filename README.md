
IMPORTANT: Do not input anything while playing until you are told to do so. 
Or you will miss important messages.

Welcome to Plantie Crush! A puzzle game that combines the fun of candy crush and plant vs zombies! 

If you have watched our trailer, you will know that our game is based on the story of Dirk who turned from a plant into a zombie. 
The aim of the game is to match different plants together to make it three in a row. 
You will earn coins throughout the process, which could be used to combine elements to kill zombies.

There are two gamemodes, story and infinite.
Story allows for the player to go through a few round of tutorials. 
The player should be familiar with the game after the tutorial, which would then allow for the 'main' part of the game.
There are three levels to complete in this game, after which it will end. 

Infinite mode allows for the game to go on for as many rounds as you want until all the plants are killed by the zombies.

Basic gameplay:

A board will be printed with different plants. The board works by rotating a 2 by 2 square clockwise dictated by your input. 

   🌰(→)  🌻(↓)  
   🏹(↑)  🥔(←)

   will turn into:

   🏹  🌰
   🥔  🌻

For a more detailed look:

   00    01    02    03    04    05    06    07             
|  🥔    🌻    🥔    🏹    🌰    🥔    🥔    🌻             
   10    11    12    13    14    15    16    17             
|  🌰    🌻    🌻    🥔    🥔    🌰    🌰    🥔             
   20    21    22    23    24    25    26    27             
|  🥔    🥔    🌻    🌻    🥔    🌰    🥔    🥔             
   30    31    32    33    34    35    36    37             
|  🌰    🥔    🌰    🌰    🌻    🥔    🏹    🏹             
   40    41    42    43    44    45    46    47             
|  🏹    🌻    🏹    🏹    🌻    🏹    🌰    🏹   

A valid input will be '01'

This will happen:

   00    01    02    03    04    05    06    07             
|  🥔    🌻    🌻    🏹    🌰    🥔    🥔    🌻             
   10    11    12    13    14    15    16    17             
|  🌰    🌻    🥔    🥔    🥔    🌰    🌰    🥔             
   20    21    22    23    24    25    26    27             
|  🥔    🥔    🌻    🌻    🥔    🌰    🥔    🥔             
   30    31    32    33    34    35    36    37             
|  🌰    🥔    🌰    🌰    🌻    🥔    🏹    🏹             
   40    41    42    43    44    45    46    47             
|  🏹    🌻    🏹    🏹    🌻    🏹    🌰    🏹   


12, 13, 14 forms three in a row, and therefore will be eliminated.

For every successful elimination, you will gain two 'costs'. 
Five of these costs can be used to attach elements. 

Zombies will attack from the right. Each flower will have different healthpoints (hp).
Each plant will take a different number of 'hits' before it dies.
When two zombies come together on the same row, they will combine to make a bigger and stronger zombie. 
When a plant dies, it will turn into a hole (+). No rotation can be done across holes. 

   00    01    02    03    04    05    06    07             
|  🌻    🥔    🌻    🥔    🌰    🌻    🏹    🌻             
   10    11    12    13    14    15    16                   
|  🥔    🥔    🏹    🏹    🥔    🌰    🏹     +             
   20    21    22    23    24    25    26    27             
|  🌰    🌻    🌰    🌰    🥔    🌻    🌰    🌻             
   30    31    32    33    34    35    36    37             
|  🌰    🥔    🏹    🥔    🌰    🏹    🏹    🥔             
   40    41    42    43    44    45    46           
|  🏹    🌰    🌰    🌻    🥔    🌰    🥔     +   

Therefore, '06' and '16' will be an invalid input as holes cannot be moved. 

To more effectively kill zombies, you can use elements.
Here are the elements:

\# -> fire         (red)
= -> light        (orange)
~ -> wind         (green)
! -> electricity  (purple)


To represent the different elements on the different emoticons, the corresponding colours will be attached to the emoticons.
(We cannot show you this on readme.txt, you would have to try it out yourself)

Elements can be attached by adding 'e' to the number. For example, if I want to attach a fire element to 20, I would input:
'e20#'
Do not worry, all of this is taught again in story mode. 

Below are all of the elements and reactions:

Any element attached to the shooter (🏹) == zombie attached with that element

fire + bomb (🥔) == AOE 
fire + sunflower (🌻) == Adjacent flowers will have their healthpoints increased by 1


light + bomb (🥔) == cleaning a hole randomly
light + wall (🌰) == zombie will go to another line
light + sunflower (🌻) == eliminate a plant adjacent to sunflower (type 'h' and the number of the plant)

wind + sunflower (🌻) == push a plant adjacent to sunflower (type 'p' and the number of the corresponding plant)
wind + bomb (🥔) == All zombie are attached with wind
wind + wall (🌰) == Zombie(only small ones) is pushed to right by one

electricity + sunflower (🌻) == change the position of plants that are adjacent to sunflower 
      (type 't' and the two numbers of two plants, such as t3445 to switch 34 and 45)
electricity + bomb (🥔)== a zombie will turn into your friend and attach other zombies

As mentioned above, if you attach any element to the shooter, the zombie will also be attached with that element.
With these combinations:

fire + electricity == Burst reaction! All Zombie HP decrease by 2
fire + light == Freeze reaction! Small Zombies cannot combine to bigger zombies
light + electricity == Photoelectric reaction! All zombies attacked in horizontal, vertical and diagonal path!
wind + fire/light == Spread reaction! The element will be spread out!

More to be found!

After the different rounds of tutorial, you will finally get to the three rounds of gameplay. 

Round 1: Survive 20 rounds of gameplay.
Round 2: Gain 200 costs
Round 3: (Very challenging) Clear all holes, with seven consecutive rounds of less than 4 zombies on the board.

Have fun!

The special command is at line 1610. Please make use of it.
