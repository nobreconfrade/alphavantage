from alpha_vantage.timeseries import TimeSeries
from av_service import API_KEY
import matplotlib.pyplot as plt

ts = TimeSeries(key=API_KEY.key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='ITSA4.SAO', interval='1min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the ITSA4 stock (1 min)')
plt.show()