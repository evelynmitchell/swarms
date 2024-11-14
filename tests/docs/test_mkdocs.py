from mkdocs_test import DocProject

project = DocProject() # declare the project
                       # (by default, the directory where the program resides)
project.build(strict=False, verbose=False)
              # build the project; these are the default values for arguments

assert project.success # return code of the build is zero (success) ?
print(project.build_result.returncode) # return code from the build

# perform automatic integrity checks (do pages exist?)
project.self_check()
