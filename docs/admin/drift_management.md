# Drift Management

Drift management is a process that allows semi-automated updates of cookies (Nautobot apps) based on the changes to the cookiecutter template. Network to Code has built and maintains a private project that is used for drift management.

This process consists of the steps explained below.

## Push the Tag to the Repository

Pushing the release tag, e.g., `nautobot-app-v2.X.Y`, to the repository will trigger the GitHub Actions workflow. This workflow uses the latest `Drift Manager` Docker image to re-bake all the cookies specified in the workflow file.

## Examining the Workflow

The workflow runs individual jobs for each cookie. Each job runs the Drift Manager and creates a pull request with the drift changes since the last re-bake.

Individual jobs can fail for various reasons, including the presence of a stale drift pull request.

Stale drift pull requests must be either merged or closed manually; the drift management process will include the changes again along with any new drift in the next re-bake.

After resolving the cause of the failure, the job can be re-run by clicking the `Re-run jobs` button in the workflow.

## Pull Request Cleanup

Once the workflow finishes, it creates a pull request with the drift changes since the last re-bake for each cookie. If there are no changes, a pull request will not be generated.

Drift pull requests often require manual cleanup before being marked as ready for review. The reasons for this include:

- An obsolete `poetry.lock` file.
    To resolve this, run `poetry lock` and commit the changes.
- Linter issues after updating the tooling.
    To resolve these, run `invoke autoformat`. Manual code updates may also be needed.
- Code or documentation changes.
    The drift manager might rewrite existing code or documentation. In such cases, the changes must be reverted manually.

## Reviewing and Merging the Pull Request

The standard review and merging procedures apply to drift pull requests. These pull requests can be merged only after the review is complete, and the CI checks have passed.

It is good practice to merge pull requests promptly to manage subsequent drift pull requests effectively and avoid issues with conflicts if other changes are pushed to the repository's `HEAD`.
