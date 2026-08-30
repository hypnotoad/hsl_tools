# Tools for HSL2 and HSL3
- compiling
- testing

## Usage to create a new HSL3 project
1. Create docker image and install testing library:
```
cd hsl3 && docker build -t lindra.de/gira_hsl3 .
cd testing && make install
```

2. Copy `template_hsl3_project` to `<name>` for a new HSL3 project and
   add your `config.json` and `hsl3_<nr>_<name>.py` to it.
  
3. Compile your project with make.

4. Use `dummy.Hsl3Framework` to construct your module in tests.

