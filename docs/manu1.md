# NAME

**imagelayout** - arrange images into a large image according to a layout

# SYNOPSYS

**imagelayout(.py)** [**-w**|**--watch**] [**-s**] [**-o** _outputfile_] [**-h|--help**] _configfile_ [_imagefile_ [_imagefile_ ...]]

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
  also watches the image file and reloads it when it changes. `qiv` for Linux 
  systems is such a viewer, e.g. `qiv -T out.png` will reload `out.png` 
  as soon as it changes.
* **-s**\
  Report the pixel sizes of input images and exit.
* **-o** _outputfile_\
  Name of the output image file (optional)
* **-h, --help**\
  Display short help message and exit.
* _configfile_\
  The configuration file (yaml format)
* _imagefile(s)_\
  Optionally, the image files to be used as inputs can be specified here.

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

# INPUT AND OUTPUT FILE NAMES

The names of the input and output image file names can be specified in the configuration
file. However, to facilitate the use of `imagelayout.py` in scripts
and Makefiles, the file names can also be provided on the command line.

Input file names can be provided on the command line after the
configuration file name. In this case, you can refer to them in the
configuration file as `$1`, `$2`, etc. For example, if the command
line is

~~~
imagelayout.py config.yaml image1.png image2.jpg image3.png
~~~

then you can refer to the three input image files in the configuration
file as follows:

~~~
images:
  A: $1
  B: $2
  C: $3
~~~

To specify the output file name on the command line, the `-o` option
can be used. In this case, you can refer to it in the configuration
file as any string starting with a `$` (a single `$` is enough). For
example, if the command line is

~~~
imagelayout.py -o output.png config.yaml
~~~

then you refer to the output file in the configuration file as follows:

~~~
outputfile: $
~~~

# CONFIGURATION FILE

The only mandatory command line argument to **imagelayout** is the
configuration file _configfile_, which should be written as a YAML
format file, and contains all information about the input/output
files, the layout, and the requested operations.

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

**Note on font names:** On Linux, the system fonts may be listed using the
`fc-list` command. On Windows, look in the `\Windows\Fonts` directory. Use
the font file names without the extension (e.g. `.ttf`) as font names.
For example, bold Arial is specified in Linux as `Arial_Bold`
(assuming the `msttcorefonts` package is installed), but on
Windows as `arialbd` (as the `\Windows\Fonts` directory contains the
`arialbd.ttf` file).

# COMPLETE LIST OF CONFIGURATION FILE OPTIONS

