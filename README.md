# Raycast Scripts

![lang] ![mit]

> Scripts for automating my daily tasks

[Raycast] support python, bash and apple scripts.

I wrote a [blog post] explain the logic of the webp converting in bash + apple script.

Here are some notable scripts:

| script file               | description                                                             |
| ------------------------- | ----------------------------------------------------------------------- |
| `convert-images.py`       | convert selected images in Finder to target format with quality option  |
| `resize-images.py`        | resize selected images in Finder to target % or px                      |
| `vscode-here.applescript` | open Finder selected folder in VSCode                                   |
| `rename-files`            | batch rename files selected in Finder with specific prefix and numbered |

## Prerequisite

- image manipulation uses [ImageMagick]

## Installation

Put the scrips and image files in Raycast's Script Command folder.

🔗 [source code]

## More

- Check out my [Projects ![git-logo]][github]
- Ping me on [Twitter ![twitter-icon]][Twitter]

[git-logo]: https://api.iconify.design/bi/github.svg?color=%236FD886&width=20
[github]: https://hoishing.github.io
[Twitter]: https://twitter.com/hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[raycast]: https://raycast.com
[mit]: https://img.shields.io/github/license/hoishing/raycast-scripts
[lang]: https://img.shields.io/badge/lang-python%20%7C%20bash%20%7C%20applescript-black
[blog post]: https://dev.to/hoishing/convert-images-to-webp-with-raycast-2pln
[source code]: https://github.com/hoishing/raycast-scripts
[ImageMagick]: https://github.com/imagemagick/imagemagick
