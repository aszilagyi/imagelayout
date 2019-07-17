## imagelayout yaml configuration file
* **inputdir:** _**directoryname**_\
  Input directory; input image files will be loaded from here
* **images:**\
  Input images are specified here. Each file must have an identifier, and either a single file name or a number of parameters.
    * **_imageid_:** **_filename_**\
      An identifier and a filename. If you don't want to specify any further parameters for the image other than the filename then this form can be used. Otherwise, see below.
    * **_imageid_:**\
      An identifier for an image
        * **file:** **_filename_**\
          Name of the image file
        * **label:** **_label_**\
          A label for the image. A text string if you don't want to specify any parameters such as position, font, color, etc; in this case the parameters specified in the toplevel **labels** option will be used. If you want to specify further parameters here then provide a mapping (see next line). Optional; if omitted then the image identifier will be used for labeling.
        * **label:**\
          A label for the image along with parameters such as position, font, etc. These parameters will override those given in the toplevel **labels** option.
            * **text:** **_labeltext_**\
              Text of the label; if omitted then the image identifier will be used.
            * **fontname:** **_fontname_**\
              Name of a truetype font available on the system. Example: `Arial_Bold`.
            * **fontsize:** **_size_**\
              Font size in pixels.
            * **fontcolor:** **_colorspec_**\
              Font color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
            * **pos:** (**`top`**|`center`|`bottom`)`-`(**`left`**|`center`|`right`)\
              Position of the label relative to the image. A combination of the words (`top`, `center`, `bottom`) and (`left`, `center`, `right`), separated with a dash (no space in between!). Default: `top-left`.
            * **offset:** **[ _xoffset_**, **_yoffset_ ]**\
              Offset, in pixels, for the label, relative to the position defined in **pos**. Default: `[0, 0]`
        * **fixedsize:** **`no`** | `yes`\
          If `yes`, the image will never be resized during the layout (it may still be resized along with the final image if the **finalwidth** or **finalheight** option is used). Instead, padding will be used (either on the top and bottom or on left and right of the image) to fit the image to its neighbors. The color of the padding is determined by the **paddingcolor** toplevel parameter (default is white).
        * **autocrop:** **`no`**|`yes`\
          If `yes`, the image will be autocropped using the color of the top-left pixel.
        * **crop:** **_width_ | [ _xwidth, ywidth_ ] | [ _leftwidth_, _topwidth_, _rightwidth_, _bottomwidth_ ]**\
          Crop the image on all four sides. A single number specifies the width of a uniform crop. Two numbers refer to the left/right and top/bottom crop widths. If four numbers are given, the crop widths of all four sides can be specified separately. Optional.
        * **border:**\
          Optionally add a border to the image.
            * **size:** **_width_ | [ _xwidth_, _ywidth_ ] | [ _leftwidth_, _topwidth_, _rightwidth_, _bottomwidth_ ]**\
              Border size. A single number, or a list of 2 or 4 numbers. A single number specifies the width of a uniform border. Two numbers refer to the left/right and top/bottom widths of the border. If four numbers are given, the widths of the border on all four sides can be specified separately. If not specified then the **size** defined under the top-level **border** property will be used; or zero if there is no top-level **border** property.
            * **color:** **_colorspec_**\
              Color of the border. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`. Default: white.
    * **_imageid_:** ...\
      Any number of further images can be specified.
* **layout:**\
  The layout of the output image is specified here. It can be omitted if there is only one input image.
    * **vjoin | hjoin:**\
      Join the following images vertically (**vjoin**) or horizontally (**hjoin**). Must be followed by a list of the images to join. List elements can be further **hjoin**/**vjoin** lists and individual images. The list can be specified either on the same line in bracket notation (e.g. `vjoin: [A, B, C]`) or on separate lines using the dash notation, e.g.
      
      ```
      vjoin:
        - A
        - B
        - C
      ```
      
        * **- vjoin: | hjoin: | _imageid_**\
          List element: another list of images to join vertically or horizontally, or an image identifier for an individual image.
        * ... \
          Images and **vjoin**/**hjoin** 
          lists can be arbitrarily combined and nested. Example:
          
          ```
          vjoin:
            - hjoin: [A, B, C]
            - hjoin:
              - D
              - vjoin: [E, F]
          ```
          
* **outputfile:** **_filename_**\
  Name of the output file relative to the current directory. The extension will determine the image file type. See [Pillow documentation](https://pillow.readthedocs.io/en/3.1.x/handbook/image-file-formats.html) for the available file formats.
* **finalwidth:** **_size_**\
  The final width of the output image after joining the individual images. The image will be resized to fit this value, retaining the aspect ratio unless **finalheight** is also provided. Note that this is before the **title** and the **globalborder** are added. Optional. If not given, and **finalheight** is also omitted, the image will not be resized.
* **finalheight:** **_size_**\
  The final height of the output image after joining the individual images. The image will be resized to fit this value, retaining the aspect ratio unless **finalwidth** is also given. Note that this is before the **title** and the **globalborder** are added. Optional. If not given, and **finalwidth** is also omitted, the image will not be resized.
* **resizemethod:** **`nearest`**|`bilinear`|`bicubic`|`lanczos`\
  Which algorithm to use to resize the individual images. Default: `nearest`. 
* **pixelscaling:** **_scale_ | [ _xscale_, _yscale_ ]**\
  Apply this scaling factor to all pixel sizes. Default: 1. This parameter allows one to easily resize the output image without having to separately adjust the font sizes, border sizes, offsets, line coordinates, etc. For example, `pixelscale: 0.5` will result in a half-size image, `pixelscale: 2.0` in a double-size image.
* **autocrop:** **`no`**|`yes`\
  If set to `yes`, all individual images will be autocropped. This can be overridden with the **autocrop** parameter for any individual image.
* **paddingcolor:** **_colorspec_**\
  Color to use for the padding if the **fixedsize** option is used for any image. This will also be the background color of the whole image, which will become visible if any of the input images has transparency or an alpha channel. Default: white.
* **border:**\
  Draw a border around around each individual image before joining them. The border parameters defined here will be used as defaults, and can be overridden for each indivual image.
    * **size:** **_width_ | [ _xwidth_, _ywidth_ ] | [ _leftwidth_, _topwidth_, _rightwidth_, _bottomwidth_ ]**\
      Border size. A single number, or a list of 2 or 4 numbers. A single number specifies the width of a uniform border. Two numbers refer to the left/right and top/bottom widths of the border. If four numbers are given, the widths of the border on all four sides can be specified separately. Default: 10.
    * **color:** **_colorspec_**\
      Color of the border. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`. Default: white.
* **labels:**\
  Specify how labels should be added to the individual images. These settings can be overridden for each individual image.
    * **add:** `yes`|**`no`**\
      Whether to add labels. Default: no.
    * **fontname:** **_fontname_**\
      Name of a truetype font available on the system. Example: `Arial_Bold`. Default: FreeSans.
    * **fontsize:** **_size_**\
      Font size in pixels. Default: 32
    * **fontcolor:** **_colorspec_**\
      Font color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`. Default: black.
    * **pos:** (**`top`**|`center`|`bottom`)`-`(**`left`**|`center`|`right`)\
      Position of the label relative to the image. A combination of the words (`top`, `center`, `bottom`) and (`left`, `center`, `right`), separated with a dash (no space in between!). Default: `top-left`.
    * **offset:** **[ _xoffset_, _yoffset_ ]**\
      Offset, in pixels, for the label, relative to the position defined in **pos**. Default: `[0, 0]`
* **globallabels:**\
  Add arbitrary labels to the final image. Note: they will be added before adding the **globalborder**.
    * **fontname:** **_fontname_**\
      Name of a truetype font available on the system. Example: `Arial_Bold`. Optional, can be overridden for each label.
    * **fontsize:** **_size_**\
      Font size in pixels. Optional, can be overridden for each label.
    * **fontcolor:** **_colorspec_**\
      Font color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`. Optional, can be overridden for each label.
    * **labellist:**\
      List the labels.
        * **-**\
          Specify a label
            * **text:** **_labeltext_**\
              Text of the label. To specify a multi-line label, put it in double quotes and use `\n` to indicate line breaks, e.g. `"First line\nsecond line"`. Use the **align** property to specify the justification of lines.
            * **coords:** **[ _x_, _y_ ]**\
              Coordinates to place the label at.
            * **fontname:** **_fontname_**\
              Name of a truetype font available on the system. Example: `Arial_Bold`. Optional.
            * **fontsize:** **_size_**\
              Font size in pixels. Optional.
            * **fontcolor:** **_colorspec_**\
              Font color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`. Optional.
            * **align:** `left` | `center` | `right`\
              Justification of lines in multi-line labels.
        * **-**\
          Another label.
            * ...\
              Arbitrary number of further labels can be specified.
* **title:**\
  To add a title to the final image. It will always be placed top-center in a separate title bar.
    * **add:** **`no`**|`yes`\
      Whether to add a title. Default: no.
    * **text:** **_title_**\
      Title text, any string.
    * **fontname:** **_fontname_**\
      Name of a truetype font available on the system. Example: `Arial_Bold`. Default: FreeSans.
    * **fontsize:** **_size_**\
      Font size in pixels. Default: 36
    * **fontcolor:** **_colorspec_**\
      Font color. Default: black. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
    * **bgcolor:** **_color_**\
      Background color for the title bar.  Default: white. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
    * **height:** **_size_**\
      Height of the title bar in pixels. The title will be placed in the middle of the title bar. Default: 1.1*fontsize
* **lines:**\
  Add arbitrary lines or arrows to the final image. Note: they will be added before the **globalborder**.
    * **width:** **_width_**\
      Line width. Optional, can be ovverridden for each line. Default: 3.
    * **color:** **_colorspec_**\
      Line color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
    * **linelist:**\
      List the lines.
        * **-**
            * **fromto:** **[ _x1_, _y1_, _x2_, _y2_ ]**\
              Coordinates of start and end of line. Mandatory. Further line segments can be specified by continuing the list with **_x3, y3, x4, y4, ..._**
            * **arrowsize:** **_length_**\
              Length of the small lines forming the arrowhead. Default: 0. If not provided or zero, no arrow will be drawn. Optional.
            * **width:** **_width_**\
              Line width. Optional.
            * **color:** **_colorspec_**\
              Line color. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
        * **-**\
          Any number of further lines can be defined
            * ...\
              Another line specification
* **globalborder:**\
  Draw a border around the final image. It will be added after adding the **title**.
    * **size:** **_width_ | [ _xwidth_, _ywidth_ ] | [ _leftwidth_, _topwidth_, _rightwidth_, _bottomwidth_ ]**\
      Border size. A single number, or a list of 2 or 4 numbers. A single number specifies the width of a uniform border. Two numbers refer to the left/right and top/bottom widths of the border. If four numbers are given, the widths of the border on all four sides can be specified separately.
    * **color:** **_colorspec_**\
      Color of the border. A color name like `red`, an RGB color specified as `#rrggbb` or `rgb(red, green, blue)` with values between 0 and 255 or percentages, or a HSL color as `hsl(hue, saturation%, lightness%)`.
