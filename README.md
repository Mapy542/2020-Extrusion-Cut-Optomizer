# 2020 Extrusion Cut Optimizer

A bin packing problem program to generate the most efficient material use from a 1D stock.

## Getting Started

The list of cut pieces are entered into the 2020Cuts.csv file in the following format:

`Length, Quantity (Optional assumed 1), Type 2020/2040 (Optional assumed 2020)`

The program can then be run. On the first one a required package will be installed, and then then additional information will be requested.

Enter the maximum length of the stock material. The units of the stock material and the cut pieces must match but decimals are allowed.
Then enter the thickness of the cutting blade since there will be material loss due to the blade width. This is known as the kerf of the blade.

The program will then run and output the most efficient cut list to the console and to a file called 2020CutsOutput.txt. Each [] list represents one length of stock material and the numbers inside are the length of parts to cut out of that stock.

As an example the material needed for my K400 Laser Cutter project is loaded. The stock includes both 2020 and 2040 material intermixed in the project. More information about the laser here: https://leboeuflasing.ddns.net/k400-laser-cutter/
