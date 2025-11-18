# interaktiv.alttexts

[![interaktiv.alttexts CI](https://github.com/interaktivgmbh/interaktiv.alttexts/actions/workflows/ci.yml/badge.svg)](https://github.com/interaktivgmbh/interaktiv.alttexts/actions/workflows/ci.yml)

Add alternative texts for images.

## Contribute

- [Issue tracker](https://github.com/interaktivgmbh/interaktiv.alttexts/issues)
- [Source code](https://github.com/interaktivgmbh/interaktiv.alttexts/)

### Prerequisites

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Adding this add-on to your project

In your `mx.ini` file, add:

```ini
[interaktiv.alttexts]
url = git@github.com:interaktivgmbh/interaktiv.alttexts.git
branch = main
extras = test
```

Or using https:

```ini
[interaktiv.alttexts]
url = https://github.com/interaktivgmbh/interaktiv.alttexts.git
branch = main
extras = test
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (c0b5a93)](https://github.com/plone/cookieplone-templates/commit/c0b5a93e16bc7da0fb36f37242a5dcf7f792323f) on 2025-11-14 08:18:01.173490. A special thanks to all contributors and supporters!
