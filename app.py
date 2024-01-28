import subprocess


def run_streamlit_app():
    # Command to run the Streamlit app
    command = ['streamlit', 'run', 'examples/react_web_demo.py',  '--server.port', '6006']

    # Execute the command
    subprocess.Popen(command)

if __name__ == '__main__':
    run_streamlit_app()
