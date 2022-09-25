from task_4 import app

def test_head(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#header',timeout=10)
def test_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#graph',timeout=10)
def test_region(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#regionPick',timeout=10)
