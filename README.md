# Rigatooly
A tool to help riggers to start their rigging projects with
a good base hierarchy and pivotes already defined.

## Description
Riggatooly is a GUI to simpligy the process of selecting pivotes
when Tahoma2D users select an external application to create their
initial rigs.
The tool takes the following inputs: a *.psd file and a *.tzn file.
The tzn is a simple Tahoma2D scene file. 
The psd file contains an image with many layers(ideally one layer 
by drawing in Tahoma2D scene). Every layer should contain a point
or a little filled circle marked with the color [r,g,b] = [255, 0, 0]
to indicate that inside of that colored region a pivote(or a center)
is located.
With this input, Riggatooly locate the pivotes, assign them to
the drawings and create pegs associated to the drawings pointing to
the same pivote(center).

## Demo video
TODO

## Usage
- Open the program.
- Load tnz and psd file using the file loader.
- If everything is ok, press the "Inject Offsets Parent Pegs" button.
- Re-open Tahoma2D or reload the scene.
- In your FX windows you will new pegs associated to the drawings
and all the pivotes created.

## Status
The project is working at the moment but the GUI has some stuff to polish
regarding the user experience.

## License
See [LICENSE]("LICENSE")

