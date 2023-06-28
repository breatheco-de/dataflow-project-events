# For further developers or Data Scientist

1. Is better if you work in Gitpod, its easily
2. Run
```
pipenv install
```
You will need to install the dependencies of the Pipfile.lock to make this project work.


# How use this project

1. Clone into your computer (or gitpod).
2. Add your transformations into the `./transformations/<pipeline>/` folder.
3. Configure the project.yml to specify the piplines and transformations in the order you want to execute them.
4. Add new transofrmation files as you need them, make sure to include `expected_input` and `expected_output` as examples.
5. Update your project.yml file as needed to change the order of the transformations.
6. Validate your transformations running `$ pipenv run validate`.
7. Run your pipline by running `$ pipenv run pipeline <pipeline_slug> <dataset_name>`
8. If you need to clean your outputs :`$ pipenv run clear`