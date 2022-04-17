import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'fixedacidity':2.0,'volatileacidity':6.0,'citricacid':2.0,'residualsugar':9.0,'chlorides':6.0,'freesulfurdioxide':9.0,'totalsulfurdioxide':6.0,'density':2.0,'pH':9.0,'sulphates':6.0,'alcohol':6.0})

print(r.json()) ## we can give single value also  'age':2.0000, // 'age':2,
