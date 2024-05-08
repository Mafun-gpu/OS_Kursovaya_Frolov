import json
import subprocess
import logging
import sys

# Настройка логирования
logging.basicConfig(filename='job_queue.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_jobs(filename):
    """Загрузить задания из файла JSON."""
    try:
        with open(filename, 'r') as file:
            jobs = json.load(file)
        return jobs
    except FileNotFoundError:
        logging.error(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from {filename}")

def run_job(job):
    """Запустить задание и вернуть результат."""
    try:
        # Запуск команды, указанной в задании
        result = subprocess.run(job['command'], shell=True, check=True, capture_output=True, text=True)
        logging.info(f"Job '{job['name']}' executed successfully: {result.stdout}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Job '{job['name']}' failed: {e.stderr}")
        return e.stderr

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    jobs = load_jobs(filename)
    if jobs is None:
        print("Error loading jobs. Check the log for details.")
        sys.exit(1)

    results = []
    for job in jobs:
        result = run_job(job)
        results.append(result)

    print("All jobs executed. Results:")
    for result in results:
            print(result)

if __name__ == "__main__":
            main()
