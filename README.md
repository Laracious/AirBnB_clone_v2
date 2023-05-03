# 0x03. AirBnB clone - Deploy static

## Background Context
### In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

## Tasks
### 0. Prepare your web servers
* Write a Bash script that sets up your web servers for the deployment of web_static
### 1. Compress before sending
* Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.
### 2. Deploy archive!
* Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:
### 3. Full deployment
* Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:
### 4. Keep it clean!
* Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:
### 5. Puppet for setup
* Redo the task #0 but by using Puppet:
