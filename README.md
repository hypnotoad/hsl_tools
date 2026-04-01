# Tools for HSL2 and HSL3
- compiling
- testing

## HSL2 -> HSL3 Snippets
```
xq config.xml  -j > config.json
```

## Usage
1. create docker image
```
cd hsl2 && docker build -t lindra.de/gira_hsl2 .
cd hsl3 && docker build -t lindra.de/gira_hsl3 .
```

2. Copy Makefile and docker-setup.mk into your project and adapt
   them. They are made for a flat hierarchy.
  
3. Compile your project with make

