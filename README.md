# Football-Passes-Plot

Football passing plot using Python, Matplotlib, and the mplsoccer library. This project allows to analyze and visualize the passing patterns of a soccer players during a match.

# Features

## Data parsing

Using StatsBomb [data](https://github.com/statsbomb/open-data/) is parsed to get a list of every single pass of a player, pass start and end position and information if the pass was succesful or not. Players list is printed to standard output at start, so the user can easily choose the player whose passes will be displayed on the plot.
![SB - Icon Lockup - Colour positive](https://github.com/gharazka/Football-Passes-Plot/assets/148285170/81ed686c-782d-4eaf-b574-9e9870265716)


## mplsoccer

mplsoccer is used to put football field on the background of the plot.

## matplotlib

Matplotlib module with tkinter is used to create the passes plot and display it.
