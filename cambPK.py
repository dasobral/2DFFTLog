import numpy as np
import camb
from camb import model
import yaml
 
with open('params.yaml', 'r') as file:
    parlist = yaml.safe_load(file)

params = camb.CAMBparams()
params.set_cosmology(**parlist['cosmology'])
params.InitPower.set_params(**parlist['initpower'])
#params.set_dark_energy(w=-1.0)
# Calculate CAMB results for these parameter settings
results = camb.get_results(params)

#Now get matter power spectra and sigma8 at redshift 10
#Note non-linear corrections couples to smaller scales than you want
params.set_matter_power(**parlist['set_matterpower'])

#Linear spectra
params.NonLinear = model.NonLinear_none
results = camb.get_results(params)
kh, zlist, pk = results.get_matter_power_spectrum(**parlist['get_matterpower'])
# Stack the columns
pk_out = np.column_stack((kh, pk[0]))
np.savetxt('Pkz'+str(zlist[0])+'.dat', pk_out)
