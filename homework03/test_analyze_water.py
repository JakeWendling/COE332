from analyze_water import calcTurbidity, calcMinTime, calcTurbidityAverage
import pytest

def test_calcTurbidity():
    assert calcTurbidity(1.0, 2.0) == 2
    assert round(calcTurbidity(1.1, -2.2), 2) == 2.42
    assert type(calcTurbidity(1.0, 2.0)) == float

def test_calcMinTime():
    assert calcMinTime(1.0, 0.5, 0.5) == 1.0
    assert calcMinTime(16, 0.75, 1) == 2.0
    assert type(calcMinTime(16, 0.75, 1)) == float

def test_calcTurbidityAverage():
    data = []
    for i in range(1,6):
        data.append({'cc': i*0.2, 'dc': i*0.4})
    data1 = {'td': data}
    assert round(calcTurbidityAverage(data1, 'td', 'cc', 'dc'), 2) == 0.88
    data2 = {'td': data[:4]}
    assert round(calcTurbidityAverage(data2, 'td', 'cc', 'dc'), 2) == 0.60
    data3 = {'td': data[2:4]}
    assert round(calcTurbidityAverage(data3, 'td', 'cc', 'dc'), 2) == 1.00

def test_calcTurbidityAverage_exceptions():
    with pytest.raises(KeyError):
        calcTurbidityAverage({}, 'td', 'cc', 'dc')
    with pytest.raises(KeyError):
        calcTurbidityAverage({'td':[{}]}, 'td', 'cc', 'dc')
    with pytest.raises(KeyError):
        calcTurbidityAverage({'td':[{'a':0}]}, 'td', 'cc', 'dc')   
    with pytest.raises(KeyError):
        calcTurbidityAverage({'td':[{'cc': 0}]}, 'td', 'cc', 'dc')   
    with pytest.raises(KeyError):
        calcTurbidityAverage({'td':[{'cc': 0, 'a': 0}]}, 'td', 'cc', 'dc')
    with pytest.raises(TypeError):
        calcTurbidityAverage({'td':[{'cc': 'a', 'dc': 0}]}, 'td', 'cc', 'dc')
    with pytest.raises(TypeError):
        calcTurbidityAverage({'td':[{'cc': 0.0, 'dc': 'a'}]}, 'td', 'cc', 'dc')
        
