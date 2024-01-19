# Repository Tooling

## Local Quick-start

Pre-requisites:

- git
- Python 3.8+
- cookiecutter

## Baking Cookies

To use templates locally with Docker and Invoke, you need first set up the repository as explained in [local quick-start](#local-quick-start).

Then, you can use the following command:

```shell
cookiecutter https://github.com/nautobot/cookiecutter-nautobot-app.git --directory=nautobot-app
```

Output:

```shell
You've downloaded ~/.cookiecutters/cookiecutter-nautobot-app before. Is it okay to delete and re-download it? [y/n] (y): 
  [1/18] codeowner_github_usernames (): @smith-ntc
  [2/18] full_name (Network to Code, LLC): 
  [3/18] email (info@networktocode.com): 
  [4/18] github_org (nautobot): 
  [5/18] app_name (my_app): 
  [6/18] verbose_name (My App): 
  [7/18] app_slug (my-app): 
  [8/18] project_slug (nautobot-app-my-app): 
  [9/18] repo_url (https://github.com/nautobot/nautobot-app-my-app): 
  [10/18] base_url (my-app): 
  [11/18] min_nautobot_version (2.0.0): 
  [12/18] max_nautobot_version (2.9999): 
  [13/18] camel_name (MyApp): 
  [14/18] project_short_description (My App): 
  [15/18] model_class_name (None): 
  [16/18] Select open_source_license
    1 - Apache-2.0
    2 - Not open source
    Choose from [1/2] (1): 
  [17/18] docs_base_url (https://docs.nautobot.com): 
  [18/18] docs_app_url (https://docs.nautobot.com/projects/my-app/en/latest): 

Congratulations! Your cookie has now been baked. It is located at /tmp/nautobot-app-my-app

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry install
* poetry shell
* invoke makemigrations
* black . # this will ensure all python files are formatted correctly, may require `sudo chown -R <my local username> ./` as migrations may be owned by root

The file `creds.env` will be ignored by git and can be used to override default environment variables.
```

This command, bakes a new cookie using the `nautobot-app` template into `outputs` directory.

### Help

To see all arguments run:

```shell
cookiecutter --help
```

Output:

```shell
Usage: cookiecutter [OPTIONS] [TEMPLATE] [EXTRA_CONTEXT]...

  Create a project from a Cookiecutter project template (TEMPLATE).

  Cookiecutter is free and open source software, developed and managed by
  volunteers. If you would like to help out or fund the project, please get in
  touch at https://github.com/cookiecutter/cookiecutter.

Options:
  -V, --version                Show the version and exit.
  --no-input                   Do not prompt for parameters and only use
                               cookiecutter.json file content. Defaults to
                               deleting any cached resources and redownloading
                               them. Cannot be combined with the --replay
                               flag.
  -c, --checkout TEXT          branch, tag or commit to checkout after git
                               clone
  --directory TEXT             Directory within repo that holds
                               cookiecutter.json file for advanced
                               repositories with multi templates in it
  -v, --verbose                Print debug information
  --replay                     Do not prompt for parameters and only use
                               information entered previously. Cannot be
                               combined with the --no-input flag or with extra
                               configuration passed.
  --replay-file PATH           Use this file for replay instead of the
                               default.
  -f, --overwrite-if-exists    Overwrite the contents of the output directory
                               if it already exists
  -s, --skip-if-file-exists    Skip the files in the corresponding directories
                               if they already exist
  -o, --output-dir PATH        Where to output the generated project dir into
  --config-file PATH           User configuration file
  --default-config             Do not load a config file. Use the defaults
                               instead
  --debug-file PATH            File to be used as a stream for DEBUG logging
  --accept-hooks [yes|ask|no]  Accept pre/post hooks
  -l, --list-installed         List currently installed templates.
  --keep-project-on-failure    Do not delete project folder on failure
  -h, --help                   Show this message and exit.
```

### JSON file

You can reuse existing JSON file with pre-filled template prompts. To do so, you need to pass the path to the JSON file using the `--replay-file` argument. If you are outputing to the same directory you must pass in `--overwrite-if-exists`.

When running the command with `--replay-file` argument, the command will not prompt for any input.

First create the `my-app.json` file:

```json
{
    "cookiecutter": {
        "codeowner_github_usernames": "@smith-ntc",
        "full_name": "Network to Code, LLC",
        "email": "info@networktocode.com",
        "github_org": "nautobot",
        "app_name": "my_app",
        "verbose_name": "My App",
        "app_slug": "my-app",
        "project_slug": "nautobot-app-my-app",
        "repo_url": "https://github.com/nautobot/nautobot-app-my-app",
        "base_url": "my-app",
        "min_nautobot_version": "2.0.0",
        "max_nautobot_version": "2.9999",
        "camel_name": "MyApp",
        "project_short_description": "My App",
        "model_class_name": "None",
        "open_source_license": "Apache-2.0",
        "docs_base_url": "https://docs.nautobot.com",
        "docs_app_url": "https://docs.nautobot.com/projects/my-app/en/latest",
        "_template": "git@github.com:nautobot/cookiecutter-nautobot-app.git",
        "_output_dir": "/tmp",
        "_repo_dir": "~/.cookiecutters/cookiecutter-nautobot-app/nautobot-app",
        "_checkout": null
    }
}
```

Then run the following command:

```shell
cookiecutter https://github.com/nautobot/cookiecutter-nautobot-app.git --directory=nautobot-app --replay-file=my-app.json --overwrite-if-exists
```

Output:

```shell
You've downloaded ~/.cookiecutters/cookiecutter-nautobot-app before. Is it okay to delete and re-download it? [y/n] (y): 

Congratulations! Your cookie has now been baked. It is located at /tmp/nautobot-app-my-app

⚠️⚠️ Before you start using your cookie you must run the following commands inside your cookie:

* poetry lock
* cp development/creds.example.env development/creds.env
* poetry install
* poetry shell
* invoke makemigrations
* black . # this will ensure all python files are formatted correctly, may require `sudo chown -R <my local username> ./` as migrations may be owned by root

The file `creds.env` will be ignored by git and can be used to override default environment variables.
```

The cookiecutter CLI tool uses the default branch when using the above example command, to use a different branch, commit, or tag the `--checkout` command line argument can be used.

- `--checkout=main` will bake the cookie against the main branch
- `--checkout=v1.0.0` will bake the cookie against the `v1.0.0` tag
- `--checkout=6769dee` will bake the cookie against the `6769dee` commit
