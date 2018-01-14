import importlib

from flask import Flask, render_template, request

from dm.Actor import Actor
from dm.State import State

application = Flask(__name__)


@application.route('/', methods=["GET"])
def get_index():
    return render_template("ui.html",
                           poles=["Rationality", "Risk", "Particular Holistic", "Primacy Recency", "Routine Creative",
                                  "Emotional", "Generosity"],
                           io_values=["A", "B", "C", "D", "E"])


@application.route('/', methods=["POST"])
def post_index():
    #    def __init__(self, poles, currentState, desiredState, maxTime, error, history, criticalState, allActors, ioValues, end_io_state):
    poles_list = [pole for pole in request.form if pole.endswith("val")]
    poles = []
    for pole in poles_list:
        name = pole.replace(" ", "").replace("_val", "")
        MyClass = getattr(importlib.import_module("dm.Pole"), name + "Pole")
        val = float(request.form.get(pole)) / 100
        weight = float(request.form.get(pole.replace("val", "weight"))) / 100

        poles.append(MyClass(val, weight))

    with open("static/resource_vocab.txt", 'r') as file:
        resources = [line.rstrip('\n') for line in file]

    current_resources = {resource: 1 for resource in request.form.get("cur_resources").replace("," "").split()}
    desired_resources = {resource: 1 for resource in request.form.get("des_resources").replace("," "").split()}
    critical_resources = {resource: 1 for resource in request.form.get("critical_resources").replace("," "").split()}

    current_infra = {infra: 1 for infra in request.form.get("cur_infra").replace("," "").split()}
    desired_infra = {infra: 1 for infra in request.form.get("des_infra").replace("," "").split()}
    critical_infra = {infra: 1 for infra in request.form.get("critical_infra").replace("," "").split()}

    current_state = State(current_resources, current_infra)
    desired_state = State(desired_resources, desired_infra)
    critical_state = State(critical_resources, critical_infra)
    max_time = int(request.form.get("max_time"))

    error = int(request.form.get("error"))

    # TODO history is blank for now

    # TODO allActors is blank for now

    io_list = [io for io in request.form if io.endswith("end")]
    io_values = {}
    desired_io_values = {}
    for io in io_list:
        val = float(request.form.get(io)) / 100
        io_values[io.replace("_value_end", "")] = val

        desired_val = float(request.form.get(io.replace("_end", "")))
        desired_io_values[io.replace("_value_end", "")] = desired_val

    actor = Actor(poles, current_state, desired_state, max_time, error, [], critical_state, [], io_values,
                  desired_io_values)


application.secret_key = 'na3928ewafds'

if __name__ == "__main__":
    application.debug = True
    application.run(threaded=True)
