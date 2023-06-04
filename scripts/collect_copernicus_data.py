# add to console: pip install cdsapi
import cdsapi

c = cdsapi.Client()

# consult datasets: https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset 

c.retrieve(
    'satellite-precipitation-microwave',
    {
        'time_aggregation': 'daily',
        'year': [
            '2015', '2016', '2017',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'variable': 'all',
        'version': 'v1.0',
        'format': 'zip',
    },
    'download.zip')

print('FINISHED') 
