
import numpy as np
from gwemlightcurves.KNModels import KNTable
from astropy.table import Table, Column

def generate_lightcurve(model,samples):

    t = Table()
    for key, val in samples.iteritems():
        t.add_column(Column(data=[val],name=key))
    samples = t
    model_table = KNTable.model(model, samples)

    if len(model_table) == 0:
        return [], [], []
    else:
        t, lbol, mag = model_table["t"][0], model_table["lbol"][0], model_table["mag"][0]
        return t, lbol, mag

def KaKy2016_model(q,chi_eff,mns,mb,c,th,ph):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    vmin = 0.00
    kappa = 10.0
    eps = 1.58*(10**10)
    alp = 1.2
    eth = 0.5

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['q'] = q
    samples['chi_eff'] = chi_eff
    samples['mns'] = mns
    samples['mb'] = mb
    samples['c'] = c
    samples['th'] = th
    samples['ph'] = ph
    samples['vmin'] = vmin
    samples['kappa'] = kappa
    samples['eps'] = eps
    samples['alp'] = alp
    samples['eth'] = eth

    model = "KaKy2016"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def KaKy2016_model_ejecta(mej,vej,th,ph):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    vmin = 0.00
    kappa = 10.0
    eps = 1.58*(10**10)
    alp = 1.2
    eth = 0.5

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['th'] = th
    samples['ph'] = ph
    samples['vmin'] = vmin
    samples['kappa'] = kappa
    samples['eps'] = eps
    samples['alp'] = alp
    samples['eth'] = eth

    model = "KaKy2016"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Me2017_model(m1,mb1,c1,m2,mb2,c2,beta,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['beta'] = beta
    samples['kappa_r'] = kappa_r

    model = "Me2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Me2017_model_ejecta(mej,vej,beta,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['beta'] = beta
    samples['kappa_r'] = kappa_r

    model = "Me2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Me2017x2_model_ejecta(mej_1,vej_1,beta_1,kappa_r_1,mej_2,vej_2,beta_2,kappa_r_2):

    tmag_1, lbol_1, mag_1 = Me2017_model_ejecta(mej_1,vej_1,beta_1,kappa_r_1)
    tmag_2, lbol_2, mag_2 = Me2017_model_ejecta(mej_2,vej_2,beta_2,kappa_r_2)

    tmag = tmag_1
    lbol = lbol_1 + lbol_2
    mag = -2.5*np.log10(10**(-mag_1*0.4) + 10**(-mag_2*0.4))

    return tmag, lbol, mag

def WoKo2017_model(m1,mb1,c1,m2,mb2,c2,theta_r,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['theta_r'] = theta_r
    samples['kappa'] = kappa_r

    model = "WoKo2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def WoKo2017_model_ejecta(mej,vej,theta_r,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['theta_r'] = theta_r
    samples['kappa'] = kappa_r

    model = "WoKo2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def BaKa2016_model(m1,mb1,c1,m2,mb2,c2):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2

    model = "BaKa2016"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def BaKa2016_model_ejecta(mej,vej):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej

    model = "BaKa2016"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Ka2017_model(m1,mb1,c1,m2,mb2,c2,Xlan):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['Xlan'] = Xlan

    model = "Ka2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Ka2017_model_ejecta(mej,vej,Xlan):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['Xlan'] = Xlan

    model = "Ka2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def Ka2017x2_model_ejecta(mej_1,vej_1,Xlan_1,mej_2,vej_2,Xlan_2):

    tmag_1, lbol_1, mag_1 = Ka2017_model_ejecta(mej_1,vej_1,Xlan_1)
    tmag_2, lbol_2, mag_2 = Ka2017_model_ejecta(mej_2,vej_2,Xlan_2)

    tmag = tmag_1
    lbol = lbol_1 + lbol_2
    mag = -2.5*np.log10(10**(-mag_1*0.4) + 10**(-mag_2*0.4))

    return tmag, lbol, mag

def RoFe2017_model(m1,mb1,c1,m2,mb2,c2,Ye):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['Ye'] = Ye

    model = "RoFe2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def RoFe2017_model_ejecta(mej,vej,Ye):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    mej = 0.04
    vej = 0.10
    Xlan = 0.01

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['Ye'] = Ye

    model = "RoFe2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def SmCh2017_model(m1,mb1,c1,m2,mb2,c2,slope_r,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['slope_r'] = slope_r
    samples['kappa_r'] = kappa_r

    model = "SmCh2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def SmCh2017_model_ejecta(mej,vej,slope_r,kappa_r):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['slope_r'] = slope_r
    samples['kappa_r'] = kappa_r

    model = "SmCh2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def DiUj2017_model(m1,mb1,c1,m2,mb2,c2,th,ph):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    vmin = 0.00
    kappa = 10.0
    eps = 1.58*(10**10)
    alp = 1.2
    eth = 0.5

    flgbct = 1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['m1'] = m1
    samples['mb1'] = mb1
    samples['c1'] = c1
    samples['m2'] = m2
    samples['mb2'] = mb2
    samples['c2'] = c2
    samples['th'] = th
    samples['ph'] = ph
    samples['vmin'] = vmin
    samples['kappa'] = kappa
    samples['eps'] = eps
    samples['alp'] = alp
    samples['eth'] = eth
    samples['flgbct'] = flgbct

    model = "DiUj2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def DiUj2017_model_ejecta(mej,vej,th,ph):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    vave = 0.267
    vmin = 0.00
    kappa = 10.0
    eps = 1.58*(10**10)
    alp = 1.2
    eth = 0.5

    flgbct = 1

    samples = {}
    samples['tini'] = tini
    samples['tmax'] = tmax
    samples['dt'] = dt
    samples['mej'] = mej
    samples['vej'] = vej
    samples['th'] = th
    samples['ph'] = ph
    samples['vmin'] = vmin
    samples['kappa'] = kappa
    samples['eps'] = eps
    samples['alp'] = alp
    samples['eth'] = eth
    samples['flgbct'] = flgbct

    model = "DiUj2017"
    t, lbol, mag = generate_lightcurve(model,samples)

    return t, lbol, mag

def sn_model(z,t0,x0,x1,c):

    tini = 0.1
    tmax = 50.0
    dt = 0.1

    t, lbol, mag = SALT2.lightcurve(tini,tmax,dt,z,t0,x0,x1,c)

    return t, lbol, mag
