# DS5111_FALL2023_SW2_Lab
Repo for DS 5111 SW2 Lab

## Questions from Lab
- __What did you have to do to get `make` to work?__
	- First, I had to make sure `make` was installed into my ubuntu instance. I performed `sudo apt install make` to make sure it existed.

- __Similarly for `python3 -m venv env`, what did you have to do? (How likely are you to have guessed that without their clear error message?)__
	- After creating the `makefile` with the `env` requirements from the lab, I tried running `make env` and received an error saying the package was not installed. I had run `sudo apt update` and then `sudo apt install python3.10-venv` which was all listed out for me in the provided error message. This is something I would not have enough prior to running the `make` command.

- __Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a `;`, the first of which activates. Why can't we just do that on a separate line? In other words, why do we have to do that in one line and separate the commands with a `;`__
	- The commands need to be on the same line because within a makefile, every new line represents a new bash call with its own command to run. In order for the commands to be run in sequence, they have to be written on the same line.

- __As it is, both the `env` and `tests` jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job `run`? What would happen if you accidentaly had a file called `run` in your directory? What can we do to fix this?__
	- We would need a `.PHONY: run` callout within the `makefile` to indiciate that we are wanting to execute the command `run` not interact with the directory `run`.

- __The code provided to you for the test file starts with two lines, seemingly to append something to `sys.path`. What is the purpose of these lines?__
	- This is to indicate that the file path location of the `clockwork_decorator.py` file can be shortened to `./bin/clockwork_decorator.py` utilizing relative paths rather than absolute paths. 

## Extra Credit
- __1 point: Execute `sudo apt install tree`, and use that application to print out the file and directory structure, just as it is shown in this document at the top. You will have to look up in the reading, or google it in stackoverflow, what flag you need to exclude the 'env' directory. No need to cut and paste the structure, just include the full line you used to get it working.__
	- `tree -l env`

- __1 point: Your .gitignore has 'env/', and also a callout to ignore the compiled python files, the ones in `__pycache__` folders. What is the meaning of the `**/*` ?__
	- `**/*` signifies select everything in all directories that matches the selected folder. In this case, we use it in front of `__pycache__` which means select all files in the entire directory. Since we put it in the `.gitignore` file, this means in the entire directory ignore all files and folders from `__pycache__`.

- __1 point: do a `pip list` or `pip freeze` and call out versions of the pytest and pylint packages in your requirements.txt. Include them in your requirements.txt, and for the extra credit, just add a note reminding me you included them.__
	- My `pytest`(7.4.2) and `pylint`(2.17.5) package versions were included in the `requirements.txt` file.

- __1 points: In the sample code from the book, why does the line if `__name__=="__main__":` allow the script to run if called directly, but not otherwise? What's going on there?__
	- The line `__name=="__main__"` needs to be included in a python script, because when the python script is run it is looking for a "main" file to run. The line that is added treats that file as the main executable/main program to run. However, if we were to import the file into another python script, we can call the file by it's actual file name.

- __1 point: If you add two print statements, (or any statements for that matter), one above and one below the if `__name__...` line, what would happen when I do an `import` of the file? What happens when I call the file directly with `python <filename>`. Most importantly, why?__
	- The print statement before the `__name__` line will always print out regardless of how the file is called. However, the print statment after the `__name__` line will only print out if the file is caled directly (i.e. `python3 file.py`) and not if it is imported as a module. This is because of scope. Calling the file directly treats the entire script as a executable while the import only looks for functions/methods that are invoked in the applicable program.

