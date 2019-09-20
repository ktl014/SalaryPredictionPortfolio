"""Configurations for testing"""
# Standard dist imports
import sys
import pytest
import shutil
from pathlib import Path

# Third party imports
from cookiecutter import main

# Project level imports

# Module level constants

CCDS_ROOT = Path(__file__).parents[1].resolve()

args = {
    'project_name': 'SalaryPredictionPortfolio',
    'author_name': 'Kevin Le',
    'open_source_license': 'MIT',
    'python_interpreter': 'python3'
}


def system_check(basename):
    platform = sys.platform
    if 'linux' in platform:
        basename = basename.lower()
    return basename


@pytest.fixture(scope='class', params=[{}, args])
def default_baked_project(tmpdir_factory, request):
    temp = tmpdir_factory.mktemp('data-project')
    out_dir = Path(temp).resolve()

    pytest.param = request.param
    main.cookiecutter(
        str(CCDS_ROOT),
        no_input=True,
        extra_context=pytest.param,
        output_dir=out_dir
    )

    pn = pytest.param.get('project_name') or 'project_name'

    # project name gets converted to lower case on Linux but not Mac
    pn = system_check(pn)

    proj = out_dir / pn
    request.cls.path = proj
    yield

    # cleanup after
    shutil.rmtree(out_dir)