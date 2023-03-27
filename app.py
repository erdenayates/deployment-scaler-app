from flask import Flask, render_template, request, redirect
from kubernetes import client, config

# Configure Kubernetes API client
config.load_incluster_config()

# Initialize Flask app
app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    deployments = get_deployments()
    deployment_pods = {}
    for deployment in deployments.items:
        namespace = deployment.metadata.namespace
        deployment_name = deployment.metadata.name
        deployment_pods[deployment_name] = get_pods_by_deployment(namespace, deployment_name)
    return render_template("index.html", deployments=deployments, deployment_pods=deployment_pods)


@app.route("/scale", methods=["POST"])
def scale():
    namespace = request.form["namespace"]
    deployment_name = request.form["deployment_name"]
    replicas = int(request.form["replicas"])

    scale_deployment(namespace, deployment_name, replicas)

    return redirect("/")

@app.route("/logs", methods=["POST"])
def logs():
    namespace = request.form["namespace"]
    pod_name = request.form["pod_name"]
    container_name = request.form.get("container_name", None)

    logs = get_pod_logs(namespace, pod_name, container_name)
    return render_template("logs.html", logs=logs)

def get_deployments():
    api_instance = client.AppsV1Api()
    deployments = api_instance.list_deployment_for_all_namespaces()
    return deployments

def scale_deployment(namespace, deployment_name, replicas):
    api_instance = client.App
    AppsV1Api()
    body = {"spec": {"replicas": replicas}}
    api_instance.patch_namespaced_deployment_scale(deployment_name, namespace, body)

def get_pod_logs(namespace, pod_name, container_name=None):
    api_instance = client.CoreV1Api()
    logs = api_instance.read_namespaced_pod_log(pod_name, namespace, container=container_name)
    return logs

def get_pods_by_deployment(namespace, deployment_name):
    api_instance = client.CoreV1Api()

    # Get deployment to find the correct label selector
    apps_v1_api = client.AppsV1Api()
    deployment = apps_v1_api.read_namespaced_deployment(namespace=namespace, name=deployment_name)

    # Use the deployment's label selector to find its pods
    label_selector = ','.join([f"{k}={v}" for k, v in deployment.spec.selector.match_labels.items()])
    pods = api_instance.list_namespaced_pod(namespace, label_selector=label_selector)
    return pods



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
