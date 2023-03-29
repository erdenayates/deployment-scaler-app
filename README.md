<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 1rem;
        }

        h1, h2, h3, h4, h5, h6 {
            font-weight: bold;
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        h2 {
            font-size: 1.5rem;
            margin-bottom: 0.75rem;
        }

        h3 {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }

        p, ul, ol {
            margin-bottom: 1rem;
        }

        ul, ol {
            padding-left: 2rem;
        }

        code {
            font-family: monospace;
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 4px;
        }

        pre {
            font-family: monospace;
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Kubebolt</h1>
    <p>
        Kubebolt is a simple web application to manage Kubernetes deployments.
        It allows users to view, scale, and restart deployments, as well as view logs of associated pods.
    </p>

    <h2>Prerequisites</h2>
    <p>
        Before you get started, ensure you have the following prerequisites installed:
    </p>
    <ul>
        <li>Python 3.x</li>
        <li>pip (Python package manager)</li>
        <li>kubectl (Kubernetes command-line tool)</li>
    </ul>

    <h2>Installation</h2>
    <p>
        Follow these steps to set up Kubebolt on your machine:
    </p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/yourusername/kubebolt.git</code></li>
        <li>Change to the project directory: <code>cd kubebolt</code></li>
        <li>Install required packages: <code>pip install -r requirements.txt</code></li>
    </ol>

    <h2>Usage</h2>
    <p>
        To start the Kubebolt application, run the following command in the project directory:
    </p>
    <pre>python app.py</pre>
    <p>
        Open your web browser and visit <a href="http://localhost:5000" target="_blank">http://localhost:5000</a> to access the Kubebolt interface.
    </p>

    <h2>Contributing</h2>
    <p>
        Contributions to Kubebolt are welcome! To contribute, please follow these steps:
    </p>
    <ol>
        <li>Fork the repository on GitHub.</li>
        <li>Create a new branch with a descriptive name.</li>
    <li>Make your changes and commit them to your branch.</li>
    <li>Push your changes to your forked repository.</li>
    <li>Create a pull request from your branch to the original repository.</li>
</ol>
<p>
    Please ensure that your code follows the project's style guidelines and passes any tests before submitting a pull request.
</p>

<h2>License</h2>
<p>
    Kubebolt is released under the MIT License. For more information, see the <a href="https://github.com/yourusername/kubebolt/blob/main/LICENSE" target="_blank">LICENSE</a> file in the project repository.
</p>

<h2>Contact</h2>
<p>
    If you have any questions or suggestions, feel free to open an issue or submit a pull request on GitHub. You can also reach out to the maintainers through their contact information listed on their GitHub profiles.
</p>
</body>
</html>
