from soilgrids import SoilGrid

soil_grids = SoilGrids()
data = soil_grids.get_coverage_data(service_id="phh2o", coverage_id="phh2o_0-5cm_mean", 
                                    west=47.5, south=-18.8, east=47.6, north=-18.7)
