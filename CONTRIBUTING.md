# How to contribute

Customer and Partner patches are essential for keeping Blue Planet Resource Adapters great. We want to keep it as easy as possible to contribute changes that get things working in your environment. There are a few guidelines that we need contributors to follow so that we can have a chance of keeping on top of things.

## Getting Started

* Register with the Ciena Community
* Join the Blue Planet DevOps Exchange
* Fork the repository on git.blueplanet.com

## Making Changes

* Create a topic branch from where you want to base your work.
  * This is usually a branch off the master branch.
  * Only target release branches if you are certain your fix must be on that branch.
  * To quickly create a topic branch based on master, run `git checkout -b fix/master/my_contribution master`. Please avoid working directly on the `master` branch.
* Make commits of logical and atomic units.
* Make sure you have added the necessary tests for your changes.
* At a minimum, each command.json should have a test

## Submitting Changes

* Push your changes to a topic branch in your fork of the repository.
* Submit a pull request to the repository in the devops-validated-ra organization.
* The RA repo team looks at Pull Requests as they are submitted.
* After feedback has been given we expect responses within two to four weeks. After four weeks we may close the pull request if it isn't showing any activity.

## Revert Policy

By running tests in advance and by engaging with peer review for prospective changes, your contributions have a high probability of becoming long lived parts of the project. After being merged, the code will run through a series of testing pipelines.

If the code change results in a test failure, we will make our best effort to correct the error. If a fix cannot be determined and committed within 24 hours of its discovery, the commit(s) responsible _may_ be reverted, at the discretion of the committer and RA repo maintainers. This action would be taken to help maintain passing states in our testing pipelines.
