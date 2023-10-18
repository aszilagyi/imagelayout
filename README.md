# imagelayout

`imagelayout` arranges several images according to a predefined
layout and produces a larger image consisting of the sub-images. It
can optionally label the individual images. Additional features
include the ability to crop and add borders to the images, to add a
border and a title to the final image, and to add arbitrary labels and
lines or arrows to the final image.

`imagelayout` can use any image format known to the Python PIL
module. This includes JPG, GIF, PNG, TIF, BMP, and lots of other
formats.

## PURPOSE

The intended use of `imagelayout` is the automated creation of
figures from sub-figures for articles and science publications.
`imagelayout` is a command-line Python application guided by a
configuration file; it has no graphical interface or interactive
features. Thus, it is suitable for use in scripts, Makefiles, and
automated and reproducible workflows. Instead of manually creating the
illustration in a visual image editor, you can write a simple
configuration file and generate the illustration with a single
command. Whenever one of the input images changes, simply rerun the
program and the illustration is immediately re-generated, saving you
from again starting up an image editor and doing the manual work
again.

## REQUIREMENTS

`imagelayout` runs under Python 3.x, and needs
[PyYAML](https://pypi.org/project/PyYAML/) and
[Pillow](https://pypi.org/project/Pillow/) to be installed.

## INSTALLATION

The program is a single `.py` file. Put [`imagelayout.py`](imagelayout.py) 
somewhere in your path and make it executable (`chmod +x imagelayout.py`).

If on Linux/Unix, put the man page
[`imagelayout.1`](docs/imagelayout.1) in your MANPATH, e.g.
`/usr/local/man/man1`.

**NOTE:** On Unix/Linux, you can rename the `imagelayout.py` file to
just `imagelayout`. On Windows, the `.py` extension may be required
for Windows to recognize the file as a Python program, and associate
it with the Python interpreter.

## DOCUMENTATION

See the [man page](docs/manu.md) for detailed instructions. The man
page is also available in [man page format](docs/imagelayout.1) and in
[html format](docs/imagelayout.html).

## DEVELOPING THE CONFIGURATION FILE

The configuration file uses the YAML format which is an intuitive,
human-readable language, easily written manually. See the [man
page](docs/manu.md) for a detailed specification of the configuration file.
A quick introduction to the general YAML syntax can be found
[here](https://github.com/darvid/trine/wiki/YAML-Primer).

A [template configuration file](config_template.yaml) is available; it
demonstrates the available options, and can be used as a start to develop 
your own configuration file.

To facilitate the writing of the configuration file,
`imagelayout` also has a "watch" mode (`-w` option) which
monitors the configuration file and immediately regenerates the output
image when it detects a change in the configuration file (i.e. you
save it from an editor). Combined with an image viewer that also
monitors the output image for changes and immediately displays the
changed file, `imagelayout` can be used semi-interactively.

## DEFINING THE LAYOUT

`imagelayout` constructs the output image by joining some input
images horizontally or vertically (`hjoin` and `vjoin` keywords), and
then again combining the resulting images horizontally or vertically,
etc. Thus, the layout is specified as an arbitrarily nested list of
`hjoin`/`vjoin` lists. During joining, all images are resized
(upscaled) to match the highest image in height (for horizontal
joining) or the widest image in width (for vertical joining). 

If the `fixedsize` option is used for an image, padding will be used
for that image instead of resizing. When `fixedsize` is used for
several images, the relative size of those images will be retained in
the final image. This is useful e.g. to avoid font sizes becoming
different when images containing text are combined.

More details on how to specify the layout can be found in the [man
page](docs/manu.md).

## EXAMPLE

A simple example of how `imagelayout` works can be found in the
[demo](demo) directory. Here, 6 input images are combined and labeled
from A to F, and a title is added. The layout is defined as

```
layout:
  hjoin:
    - vjoin:
      - hjoin: [A, B, C]
      - D
    - vjoin: [E, F]
```

Thus, A, B, and C are joined horizontally, then joined with D
vertically; this is then joined horizontally with the vertically
joined E and F. The result is: 

![imagelayout demo](demo/demo_out.png)

The full configuration file is
[imagelayout_demo.yaml](demo/imagelayout_demo.yaml).

## IMAGE GRID

To create a grid of images, either horizontally joined images should
be joined vertically:

```
layout:
  vjoin:
    - hjoin: [A, B, C]
    - hjoin: [D, E, F]
    - hjoin: [G, H, I]
```

or the other way around:

```
layout:
  hjoin:
    - vjoin: [A, D, G]
    - vjoin: [B, E, H]
    - vjoin: [C, F, I]
```

## GENERATING BLANK IMAGES AS PLACEHOLDERS

Sometimes, you want to arrange your images into a grid but you must
leave out a few cells in a grid because you don't have enough images,
e.g. you want to use a 3x2 grid but you only have 5 images. In this
case, you can provide a filename in the format `BLANK-`W`x`H, e.g.
`BLANK-640x480`. `imagelayout` will recognize the pattern and
automatically generate a blank image of the given size to use as a
placeholder. The label of the placeholder will be hidden by default.

## SINGLE-IMAGE USE

Although the main purpose of `imagelayout` is to combine multiple
images, it can also be used as a quick way to resize, crop/autocrop,
add borders, labels, lines or arrows to single images. If only a
single input image is specified, the layout does not have to be
specified, but all the other functions are available.

## SHEBANG TRICK

On Unix-based systems, you can write the `#!/usr/bin/env
imagelayout.py` line as the first line of the configuration file, and
make the file executable. Then you can execute the configuration file
as a command.
