from gwemlightcurves.KNModels import KNTable
from gwemlightcurves import lightcurve_utils
import matplotlib.pyplot as plt
t = KNTable.read_samples('posterior_samples.dat')
t = t.calc_tidal_lambda(remove_negative_lambda=True)
t = t.calc_compactness(fit=True)
t = t.calc_baryonic_mass(EOS=None, TOV=None, fit=True)
t = t.downsample(Nsamples=100)
tini = 0.1; tmax = 50.0; dt = 0.1; vmin = 0.02; th = 0.2; ph = 3.14; kappa = 1.0; eps = 1.58*(10**10); alp = 1.2; eth = 0.5; flgbct = 1; beta = 3.0; kappa_r = 1.0; slope_r = -1.2; theta_r = 0.0; Ye = 0.3
t['tini'] = tini; t['tmax'] = tmax; t['dt'] = dt; t['vmin'] = vmin; t['th'] = th; t['ph'] = ph; t['kappa'] = kappa; t['eps'] = eps; t['alp'] = alp; t['eth'] = eth; t['flgbct'] = flgbct; t['beta'] = beta; t['kappa_r'] = kappa_r; t['slope_r'] = slope_r; t['theta_r'] = theta_r; t['Ye'] = Ye
distance = 100 #Mpc
t['dist'] = distance

# Create dict of tables for the various models, calculating mass ejecta velocity of ejecta and the lightcurve from the model
models = ["DiUj2017","Me2017"]
model_tables = {}
for model in models:
    model_tables[model] = KNTable.model(model, t)
# Now we need to do some interpolation
for model in models:
   model_tables[model] = lightcurve_utils.calc_peak_mags(model_tables[model])
   model_tables[model] = lightcurve_utils.interpolate_mags_lbol(model_tables[model])

plot = KNTable.plot_mag_panels(model_tables, distance=distance)
plt.savefig("test.png")
