#!/usr/bin/env python

import fabric.colors as fc
from fabric.decorators import task

from bosun import agcm
from bosun import mom4
from bosun import coupled
from bosun import tasks
from bosun.tasks import env_options


@task
@env_options
def deploy(environ, **kwargs):
    '''Deploy cycle: prepare, compile.

    Depends on:
      prepare
      compilation
    '''
    print(fc.green("Started"))
    prepare(environ)
    compilation(environ)


@task
@env_options
def deploy_and_run(environ, **kwargs):
    '''Full model cycle: prepare, compile and run.

    Depends on:
      prepare
      compilation
      run
    '''
    print(fc.green("Started"))
    prepare(environ)
    compilation(environ)
    run(environ)


@task
@env_options
def compilation(environ, **kwargs):
    '''Compile code for model run and post-processing.

    Depends on:
      instrument_code
      compile_model
      check_code
    '''
    if environ['instrument']:
        tasks.check_code(environ)
        tasks.instrument_code(environ)
    elif tasks.check_code(environ):
        tasks.compile_model(environ)


@task
@env_options
def prepare(environ, **kwargs):
    '''Create all directories and put files in the right places.

    Depends on:
      prepare_expdir
      link_agcm_inputs
      prepare_workdir
    '''
    tasks.prepare_expdir(environ)
    if environ['type'] in ('coupled', 'atmos'):
        agcm.link_agcm_inputs(environ)
    tasks.prepare_workdir(environ)


@task
@env_options
def run(environ, **kwargs):
    '''Run the model.

    Depends on:
      run_model
    '''
    tasks.run_model(environ)


@task
@env_options
def restart(environ, **kwargs):
    '''Restart the model.

    Depends on:
      run_model
      prepare_restart
    '''
    environ['mode'] = 'warm'
    tasks.run_model(environ)


@task
@env_options
def generate_grid(environ, **kwargs):
    tasks.prepare_expdir(environ)
    tasks.check_code(environ)
    mom4.compile_pre(environ)
    mom4.generate_grid(environ)


@task
@env_options
def make_xgrids(environ, **kwargs):
    tasks.prepare_expdir(environ)
    tasks.check_code(environ)
    mom4.compile_pre(environ)
    mom4.make_xgrids(environ)


@task
@env_options
def regrid_3d(environ, **kwargs):
    tasks.prepare_expdir(environ)
    tasks.check_code(environ)
    mom4.compile_pre(environ)
    mom4.regrid_3d(environ)

@task
@env_options
def regrid_2d(environ, **kwargs):
    tasks.prepare_expdir(environ)
    tasks.check_code(environ)
    mom4.compile_pre(environ)
    mom4.regrid_2d(environ)