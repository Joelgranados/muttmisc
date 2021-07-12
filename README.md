# Building

## Dependencies
You need to have shiv installed https://shiv.readthedocs.io/en/latest/

## Building
Just run `make`
This will create a self contained python binary (zipped file) that should just run

# Installing
For now this is done by manually copying files to where you need them

## Ical To Todoist
1. Copy build/ical_to_todoist to where your mutt scripts are.
2. In the same directory where you copied ical_to_todoist to, create a file named
   todoist_token.json where you put your todoist API token.
   You can execute the following:

   echo "{\"todoist_token\" : \"TOKEN\"}" > /PATH/TO/MUTT/SCRIPTS/todoist_token.json
3. Create a macro in mutt that pipes mail to script and has the json argument:
   Example:
   ```
   macro index,pager,attach I "<pipe-message>/PATH/TO/ical_to_todoist /PATH/TO/todoist_token.json<enter>" "Documentation"
   ```
