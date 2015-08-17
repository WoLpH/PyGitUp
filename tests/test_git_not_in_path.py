# System imports
import os
from os.path import join

# 3rd party libs
from nose.tools import *

# PyGitup imports
from tests import basepath
from PyGitUp.git_wrapper import GitError

test_name = 'git-not-in-path'
repo_path = join(basepath, test_name + os.sep)


def setup():
    os.makedirs(repo_path, 0o700)


def test_not_a_git_repo():
    """ Run 'git up' with git no being in PATH """
    os.chdir(repo_path)
    environ = os.environ.copy()
    os.environ['PATH'] = ''

    with assert_raises(GitError) as e:
        from PyGitUp.gitup import GitUp
        GitUp(testing=True)

    assert e.exception.message == "The git executable could not be found"

    os.environ.update(environ)
