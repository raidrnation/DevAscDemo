from pathlib import Path
import csv
import paramiko

CSV_FILE = Path("C:/Users/ohana/Downloads/data.csv")

def csv_reader():
    devices = {}

    with open (CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            device_name = row["Device Name"]
            devices[device_name] = {
                "ip_address" : row["IP Address"],
                "username" : row["Username"],
                "password" : row["Password"]
            }

    return devices

def command_runner(device, command):
    ssh = None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname = device["ip_address"],
            username = device["username"],
            password = device["password"],
            allow_agent = False,
            look_for_keys = False,
            timeout = 10
        )
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode("utf-8").strip()
        error = stderr.read().decode("utf-8").strip()

        if error:
            return error
        return output

    except paramiko.AuthenticationException:
        return "Authentication failed. Please check your credentials."
    except paramiko.SSHException as e:
        return f"SSH connection error: {str(e)}"
    except Exception as e:
        return None, str(e)

    finally:
        if ssh:
            ssh.close()
