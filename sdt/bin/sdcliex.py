#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
#  @program        synda
#  @description    climate models data transfer program
#  @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
#                             All Rights Reserved”
#  @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module contains command line examples.

Note
    sdcliex means 'SynDa Command LIne EXample'
"""

def autoremove():
    buf=""""""
    return buf

def cache():
    buf=""""""
    return buf

def certificate():
    buf=""""""
    return buf

def contact():
    buf=""""""
    return buf

def daemon():
    buf=""""""
    return buf

def dump():
    buf=""""""
    return buf

def facet():
    buf=""""""
    return buf

def help():
    buf=""""""
    return buf

def history():
    buf=""""""
    return buf

def install():
    buf=""""""
    return buf

def intro():
    buf=""""""
    return buf

def list():
    buf=""""""
    return buf

def metric():
    buf=""""""
    return buf

def param():
    buf=""""""
    return buf

def pexec():
    buf=""""""
    return buf

def queue():
    buf=""""""
    return buf

def remove():
    buf=""""""
    return buf

def replica():
    buf=""""""
    return buf

def reset():
    buf=""""""
    return buf

def retry():
    buf=""""""
    return buf

def search(prog):
    buf="""  %s experiment=rcp45,rcp85 model=CCSM4
  %s project=ISI-MIP%%20Fasttrack searchapi_host=esg.pik-potsdam.de
  %s project=CMIP5 realm=atmos
  %s realm=atmos project=CMIP5
  %s atmos 50
  %s MIROC rcp45 2
  %s CCSM4 rcp45 atmos mon r1i1p1
  %s title=rlds_Amon_MPI-ESM-LR_amip_r1i1p1_1979-2008.nc project=EUCLIPSE
  %s title=rlds_Amon_MPI-ESM-LR_amip_r1i1p1_1979-2008.nc
  %s clt_day_CanESM2_esmControl_r1i1p1_19010101-22501231.nc
  %s pr_day_MPI-ESM-LR_abrupt4xCO2_r1i1p1_18500101-18591231.nc
  %s c20c.UCT-CSAG.HadAM3P-N96.NonGHG-Hist.HadCM3-p50-est1.v1-0.mon.atmos.run060.v20140528
  %s title=rlds_bced_1960_1999_gfdl-esm2m_rcp8p5_2051-2060.nc searchapi_host=esg.pik-potsdam.de
  %s tamip.output1.NCAR.CCSM4.tamip200904.3hr.atmos.3hrSlev.r9i1p1.v20120613|tds.ucar.edu
  %s tamip.output1.NCAR.CCSM4.tamip200904.3hr.atmos.3hrSlev.r9i1p1.v20120613
  %s dataset_id=tamip.output1.NCAR.CCSM4.tamip200904.3hr.atmos.3hrSlev.r9i1p1.v20120613|tds.ucar.edu
  %s cmip5.output1.CCCma.CanESM2.historicalGHG.fx.atmos.fx.r0i0p0.v20120410.orog_fx_CanESM2_historicalGHG_r0i0p0.nc"""%((prog,)*17)

    return buf

def selection():
    buf=""""""
    return buf

def show():
    buf=""""""
    return buf

def stat():
    buf=""""""
    return buf

def test():
    buf=""""""
    return buf

def update():
    buf=""""""
    return buf

def upgrade():
    buf=""""""
    return buf

def version():
    buf=""""""
    return buf

def watch():
    buf=""""""
    return buf