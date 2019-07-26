# NAME

**imagelayout** - arrange images into a large image according to a layout

# SYNOPSYS

**imagelayout(.py)** [**-w**|**--watch**] [**-s**] [**-h|--help**] _configfile_

NOTE: Depending on how you installed the program, the command is either 
**imagelayout.py** or just **imagelayout**.

# DESCRIPTION

**imagelayout** arranges several images according to a predefined
layout and produces a larger image consisting of the sub-images. It
can optionally label the individual images. Additional features
include the ability to crop and add borders to the images, to add a
border and a title to the final image, and to add arbitrary labels and
lines or arrows to the final image. The intended use of
**imagelayout** is the creation of figures from sub-figures for
articles and science publications. **imagelayout** is a
command-line Python application guided by a configuration file _configfile_
(provided as the only command line argument); it has
no graphical interface or interactive features. Thus, it is suitable
for use in scripts, Makefiles, and automated and reproducible
workflows.

# OPTIONS

* **-w, --watch**\
  Run once, then watch the configuration file for changes and re-run whenever a   
  change is detected. This is useful for developing the configuration file and 
  making adjustments. **Tip:** View the output image file with a viewer that 
  also watches the image file and reloads it when it changes. `feh` for Linux 
  systems is such a viewer, e.g. `feh -r 0.5 out.png` will reload `out.png` 
  every 0.5 seconds.
* **-s**\
  Report the pixel sizes of input images and exit.
* **-h, --help**\
  Display short help message and exit.
  
# DEFINING THE IMAGE LAYOUT

The desired layout of the images can be defined as a combination of
horizontally and vertically joined images. Two keywords are used for
this in the configuration file. The `hjoin` keyword defines a
horizontally joined image sequence, e.g.

~~~
layout:
  hjoin: [A, B, C]
~~~
will result in the following image arrangement:
~~~
+---+---+---+
| A | B | C |
+---+---+---+
~~~
while the `vjoin` keyword produces a vertical arrangement:
~~~
layout:
  vjoin: [A, B, C]
~~~
will result in this arrangement:
~~~
+---+
| A |
+---+
| B |
+---+
| C |
+---+
~~~

More complex layouts can be defined by combining and nesting the
`hjoin` and `vjoin` specifications. For example,

~~~
hjoin:
  - vjoin:
      - hjoin: [A, B]
      - C
  - D
~~~
results in this layout:
~~~
+---+---+---+
| A | B |   |
+---+---+ D |
|   C   |   |
+-------+---+
~~~

Horizontally joined images will be resized to fit the same height (the
highest image), and vertically joined images will be
resized to fit the same width (the widest image). If the **fixedsize** option
is used for an image, it will be padded rather than scaled.

# CONFIGURATION FILE

The only command line argument to **imagelayout** is the configuration
file _configfile_, which should be written as a YAML format file, and
contains all information about the input/output files, the layout, and
the requested operations.

The two main mandatory parts of the configuration file are the
**images** section and the **layout** section; in addition the output
file must also be specified using the **outputfile** keyword. The
simplest configuration file may look something like this:

~~~
images:
  A: imageA.png
  B: imageB.png
outputfile: out.png
layout:
  hjoin: [A, B]
~~~

This will produce the file `out.png` consisting of `imageA.png` and
`imageB.png` joined horizontally. If the

```
labels:
  add: yes
```

lines are added then each image will be labeled in the top left corner
with the letters A and B, respectively.

The configuration file may contain numerous other keywords and options
to specify image labels, font names, font sizes and colors,
cropping images or adding borders to them, adding a title, adding
arbitrary labels, lines, and arrows to the final image. The detailed
list of keywords and options follows.

# COMPLETE LIST OF CONFIGURATION FILE OPTIONS

