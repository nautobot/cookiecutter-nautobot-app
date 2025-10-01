# Release Checklist

This document is intended for cookie maintainers and outlines the steps to perform when releasing a new version of the cookie.

!!! important
    Before starting, make sure your **local** `develop`, `main`, and (if applicable) the current LTM branch are all up to date with upstream!

    ```
    git fetch
    git switch develop && git pull # and repeat for main/ltm
    ```

Choose your own adventure:

- LTM release? Jump [here](#ltm-releases).
- Patch release from `develop`? Jump [here](#all-releases-from-develop).
- Minor release? Continue with [Minor Version Bumps](#minor-version-bumps) and then [All Releases from `develop`](#all-releases-from-develop).

## Minor Version Bumps

### Update Requirements

Every minor version release should refresh `poetry.lock`, so that it lists the most recent stable release of each package. To do this:

0. Run `poetry update --dry-run` to have Poetry automatically tell you what package updates are available and the versions it would upgrade to. This requires an existing environment created from the lock file (i.e. via `poetry install`).
1. Review each requirement's release notes for any breaking or otherwise noteworthy changes.
2. Run `poetry update <package>` to update the package versions in `poetry.lock` as appropriate.
3. If a required package requires updating to a new release not covered in the version constraints for a package as defined in `pyproject.toml`, (e.g. `Django ~3.1.7` would never install `Django >=4.0.0`), update it manually in `pyproject.toml`.
4. Run `poetry install` to install the refreshed versions of all required packages.
5. Run all tests (`poetry run invoke tests`) and check that the UI and API function as expected.

### Update Documentation

If there are any changes to the compatibility matrix (such as a bump in the minimum supported Nautobot version), update it accordingly.

Commit any resulting changes from the following sections to the documentation before proceeding with the release.

!!! tip
    Fire up the documentation server in your development environment with `poetry run mkdocs serve`! This allows you to view the documentation site locally (the link is in the output of the command) and automatically rebuilds it as you make changes.

### Create Release Notes

For every minor version, we need to create a new release notes file, update `tool.towncrier.filename` in `pyproject.toml`  and update the `mkdocs.yml` table of contents.

The new release notes file should be named `version_<major>.<minor>.md` (e.g. `version_2.7.md`) and placed in the `docs/admin/release_notes/` directory. The easiest way to create this file is to copy the most recent existing version (e.g. `version_2.6.md`) and then delete anything after the `<!-- towncrier release notes start -->` line. Update the rest of the copied content to reflect the new version number and release overview section.

Find the `tool.towncrier` section in `pyproject.toml` and update the `filename` value to match the new release notes file you just created.

Finally, open `mkdocs.yml` and add an entry for the new release notes file in the table of contents under `nav`.`Administrator Guide`.`Release Notes`.

### Verify the Cookie Outputs Valid Code

Follow the [usage instructions](https://github.com/nautobot/cookiecutter-nautobot-app/#usage-with-cookiecutter) to bake a new cookie. If possible run `invoke tests` in the newly created app to verify that the cookie outputs valid code.

---

## All Releases from `develop`

### Verify CI Build Status

Ensure that continuous integration testing on the `develop` branch is completing successfully.

### Update the Changelog

!!! important
    The changelog must adhere to the [Keep a Changelog](https://keepachangelog.com/) style guide.

This guide uses `nautobot-app-v2.7.0` as the new version in its examples, so change it to match the version you wish to use! Every. single. time. you. copy/paste commands :)

First, create a release branch off of `develop` (`git switch -c release-nautobot-app-2.7.0 develop`).

> You will need to have the project's poetry environment built at this stage, as the towncrier command runs **locally only**. If you don't have it, run `poetry install` first.

Generate release notes with `invoke generate-release-notes --version nautobot-app-v2.7.0` and answer `yes` to the prompt `Is it okay if I remove those files? [Y/n]:`. This will update the release notes in `docs/admin/release_notes/version_2.7.md`, stage that file in git, and `git rm` all the fragments that have now been incorporated into the release notes.

Stage all the changes (`git add`) and check the diffs to verify all of the changes are correct (`git diff --cached`).

Commit `git commit -m "Release nautobot-app-v2.7.0"` and `git push` the staged changes.

### Submit Release Pull Request

Submit a pull request titled `Release nautobot-app-v2.7.0` to merge your release branch into `main`. Copy the documented release notes into the pull request's body.

!!! important
    Do not squash merge this branch into `main`. Make sure to select `Create a merge commit` when merging in GitHub.

Once CI has completed on the PR, merge it.

### Create a New Release in GitHub

Draft a [new release]({{ cookiecutter.repo_url }}/releases/new) with the following parameters.

* **Tag:** Input current version (e.g. `nautobot-app-v2.7.0`) and select `Create new tag: nautobot-app-v2.7.0 on publish`
* **Target:** `main`
* **Title:** Version and date (e.g. `nautobot-app-v2.7.0 - 2024-04-02`)

Click "Generate Release Notes" and edit the auto-generated content as follows:

- Change the entries generated by GitHub to only the usernames of the contributors. e.g. `* Updated dockerfile by @nautobot_user in {{ cookiecutter.repo_url }}/pull/123` -> `* @nautobot_user`.
    - This should give you the list for the new `Contributors` section.
    - Make sure there are no duplicated entries.
- Replace the content of the `What's Changed` section with the description of changes from the release PR (what towncrier generated).
- If it exists, leave the `New Contributors` list as it is.

The release notes should look as follows:

```markdown
## What's Changed

**Towncrier generated Changed/Fixed/Housekeeping etc. sections here**

## Contributors

* @alice
* @bob

## New Contributors

* @bob

**Full Changelog**: https://github.com/nautobot/cookiecutter-nautobot-app/compare/nautobot-app-v2.6.1...nautobot-app-v2.7.0
```

Publish the release!

### Create a PR from `main` back to `develop`

!!! note
    Since this project doesn't use poetry to maintain a python package, there is no need to bump a version in `pyproject.toml`. You can open a PR directly from `main` to `develop` in GitHub without creating a third branch.

!!! important
    Do not squash merge this PR into `develop`. Make sure to select `Create a merge commit` when merging in GitHub.

Open a new PR from `main` against `develop`, wait for CI to pass, and merge it.

### Final checks

At this stage, documentation should have been built for the tag on ReadTheDocs and if you're reading this page online, refresh it and look for the new version in the little version fly-out menu down at the bottom right of the page.

All done!

## LTM Releases

For projects maintaining a Nautobot LTM compatible release, all development and release management is done through the `ltm-x.y` branch. The `x.y` relates to the LTM version of Nautobot it's compatible with, for example `1.6`.

The process is similar to releasing from `develop`, but there is no need for post-release branch syncing because you'll release directly from the LTM branch:

1. Make sure your `ltm-1.6` branch is passing CI.
2. Create a release branch from the `ltm-1.6` branch: `git switch -c release-1.2.3 ltm-1.6`.
3. Generate the release notes: `invoke generate-release-notes --version nautobot-app-v1.6.3`.
4. Add all the changes and `git commit -m "Release v1.2.3"`, then `git push`.
5. Open a new PR against `ltm-1.6`. Once CI is passing in the PR, merge it.
6. Create a New Release in GitHub - use the same steps documented [here](#create-a-new-release-in-github).
7. Open a separate PR against `develop` to synchronize all LTM release changelogs into the latest version of the docs for visibility.
