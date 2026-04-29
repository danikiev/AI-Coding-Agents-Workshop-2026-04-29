# Outputs

## Required

- Reproduced figure image
- Short note on assumptions or approximation choices
- Minimal explanation of how the result was generated

## Good Stretch Goals

- Add a validation plot
- Compare the reproduced version against the target figure
- Refactor plotting logic into reusable functions

## Output Structure

- keep `input/` folder unchanged
- use `src/` folder for code, including a clear entry point script that generates the figure, any necessary helper functions or modules, and README with instructions
- add `environment.yml` for conda environment setup
- use `output/` folder for the generated figure images