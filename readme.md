
# Heaven's Globe

Heaven's Globe is a discrete simulation engine desined around two principles.

 - Simplicity of design
 - Ability for ground-truth data to stay in original formats
 - Ability to ingest data from several formats:
    - SQlite database
    - Folder of `.csv` files
    - `.json` file(s)
    - Esri File Geodatabase (`.gdb/`)

Because of the design, several invariants will be upheld:

 - 2D data will always gain a 3D component, even if it means all data has a `0` or a `0 above elevation` `z` value.
 - Source data will be duplicated into a SQlite database and modified according to simulation steps there, to keep source data immutable


# Dev testing

```bash
python runme.py

```




