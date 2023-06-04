# Automated predictions of the avalanche danger level for dry-snow conditions in Switzerland

Data sets of the publication: Data-driven automated predictions of the avalanche danger level for dry-snow conditions in Switzerland

Pérez-Guillén, C., Techel, F., Hendrick, M., Volpi, M., van Herwijnen, A., Olevski, T., Obozinski, G., Pérez-Cruz, F., and Schweizer, J.: Data-driven automated predictions of the avalanche danger level for dry-snow conditions in Switzerland, Nat. Hazards Earth Syst. Sci. Discuss. [preprint], https://doi.org/10.5194/nhess-2021-341, in review, 2021.


### Description of data sets:

These data sets include the meteorological variables (resampled 24-hour averages) and the profile variables extracted from the simulated profiles using SNOWPACK with input data of the weather stations of the IMIS network in Switzerland.  In addition, the data set of 'Data_RF1_forecast.csv' contains the danger ratings for dry-snow conditions assigned in the Swiss avalanche bulletin to the location of the weather station and the data set of 'Data_RF2_tidy.csv' a quality-controlled subset of danger ratings for dry-snow conditions.

 Description of the data:
 
 - 'datum': date of the issued avalanche forecast
 - 'station_code': code of the weather station of the IMIS network
 - 'sector_id': number code of the region of the location of the weather station 
 - 'warnreg': number code for mapping the warning regions 
 - 'elevation_station': elevation (m a.s.l.) of the weather station
 - 'forecast_initial_date': initial date and time of the forecast window
 - 'forecast_end_date':  end date and time of the forecast window
 - 'dangerLevel': danger level assigned according to the five-level European Avalanche Danger Scale (1-Low, 2-Moderate; 3-Considerable, 4-High, and 5-Very High)
 - 'elevation_th': critical elevation (m a.s.l.) forecast in the bulletin for the region
 - 'set': training or test set
 - 'Qs': sensible heat [W/m2]
 - 'Ql': latent heat [W/m2]
 - 'TSG': ground temperature [°C]
 - 'Qg0': ground heat at soil interface [W/m2]
 - 'Qr':  rain energy [W/m2]
 - 'OLWR': outgoing long wave radiation [W/m2]
 - 'ILWR': incoming long wave radiation [W/m2]
 - 'LWR_net': net long wave radiation [W/m2]
 - 'OSWR': reflected short wave radiation [W/m2]
 - 'ISWR': incoming short wave radiation [W/m2]
 - 'Qw': net short wave radiation [W/m2]
 - 'pAlbedo': parametrized albedo [-]
 - 'ISWR_h': incoming short wave on horizontal [W/m2]
 - 'ISWR_diff': direct incoming short wave [W/m2]
 - 'ISWR_dir': diffuse incoming short wave [W/m2]
 - 'TA': air temperature [°C]
 - 'TSS_mod': surface temperature (modelled) [°C]
 - 'TSS_meas': surface temperature (measured) [°C]
 - 'T_bottom': bottom temperature [°C]
 - 'RH': relative humidity [-]
 - 'VW': wind velocity [m/s]
 - 'VW_drift': wind velocity drift [m/s]
 - 'DW':  wind direction [°]
 - 'MS_Snow': solid precipitation rate [kg/m2/h]
 - 'HS_mod': snow height (modelled) [cm]
 - 'HS_meas': snow height (measured) [cm]
 - 'hoar_size': hoar size [cm]
 - 'wind_trans24': 24h wind drift [cm]
 - 'wind_trans24_7d': 7d wind drift [cm]
 - 'wind_trans24_3d': 3d wind drift [cm]
 - 'HN24': 24h height of new snow [cm]
 - 'HN72_24': 3d sum of daily height of new snow [cm]
 - 'HN24_7d': 7d sum of daily height of new snow [cm]
 - 'SWE': snow water equivalent [kg/m2] 
 - 'MS_water': total amount of water [kg/m2]
 - 'MS_Wind': erosion mass loss [kg/m2]
 - 'MS_Rain': rain rate [kg/s2/h]
 - 'MS_SN_Runoff': virtual lysimeter [kg/s2/h]
 - 'MS_Sublimation': sublimation mass [kg/m2]
 - 'MS_Evap': evaporated mass [kg/m2]
 - 'TS0': snow temperature at 0.25 m [°C]
 - 'TS1': snow temperature at 0.5 m [°C]
 - 'TS2': snow temperature at 1 m [°C]
 - 'Sclass2': stability class [-]
 - 'zSd_mean': depth of deformation rate stability index [cm]
 - 'Sd': deformation rate stability index [-]
 - 'zSn': depth of natural stability index [cm]
 - 'Sn': natural stability index [-]
 - 'zSs': depth of natural stability index [cm]
 - 'Ss': Sk38 skier stability index [-]
 - 'zS4': depth of Sk38 skier stability index [cm]
 - 'S4': structural stability index [-]
 - 'zS5': depth of stability index 5 [cm]
 - 'S5': stability index 5 [-]
 - 'pwl_100': Persistent weak layer(s) in the 100 cm from the surface [-]
 - 'pwl_100_15': Persistent weak layer(s) at depths between 15 cm and 100 cm [-]
 - 'base_pwl':  Persistent weak layer at bottom [-]
 - 'ssi_pwl': Structural stability index at weak layer [-]
 - 'sk38_pwl': Sk38 skier stability index at weak layer [-]
 - 'sn38_pwl': Natural stability index at weak layer [-]
 - 'ccl_pwl':  Critical cut length at weak layer [m]
 - 'ssi_pwl_100': Structural stability index at surface weak layer [-]
 - 'sk38_pwl_100': Sk38 skier stability index at surface weak layer [-]
 - 'sn38_pwl_100': Natural stability index at surface weak layer [-]
 - 'ccl_pwl_100':  Critical cut length at surface weak layer [m] 
 - 'Pen_depth': Skier penetration depth [cm]
 - 'min_ccl_pen': Minimum critical cut length at a deeper layer of the penentration depth [m]


### SNOWPACK model:

- snowpack-ams_pmod: Modeled parameters based on the weather stations data.
- snowpack-ams_pmod_profile: Modeled Snowpack Layers based on stations data.

Documentation of the meteorological and snowpack variables used in this study: https://models.slf.ch/docserver/snowpack/html/index.html




