from flask import Flask, render_template, request, redirect
from kubernetes import client, config

# Configure Kubernetes API client
config.load_incluster_config()

# Initialize Flask app
app = Flask(__name__, static_folder="static")
@app.route("/")
def index():
    deployments = get_deployments()
    return render_template("index.html", deployments=deployments)

@app.route("/scale", methods=["POST"])
def scale():
    namespace = request.form["namespace"]
    deployment_name = request.form["deployment_name"]
    replicas = int(request.form["replicas"])

    scale_deployment(namespace, deployment_name, replicas)

    return redirect("/")

def get_deployments():
    api_instance = client.AppsV1Api()
    deployments = api_instance.list_deployment_for_all_namespaces()
    return deployments

def scale_deployment(namespace, deployment_name, replicas):
    api_instance = client.AppsV1Api()
    body = {"spec": {"replicas": replicas}}
    api_instance.patch_namespaced_deployment_scale(deployment_name, namespace, body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

