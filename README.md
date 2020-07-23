# Threader3000
<h4>Multi-threaded Python Port Scanner with Nmap integration for use on Linux or Windows

<h5>Threader3000 is a script written in Python3 that allows multi-threaded port scanning.  The program is interactive and simply requires you to run it to begin.  Once started, you will be asked to input an IP address or a FQDN as Threader3000 does resolve hostnames.  A full port scan should take three minutes or less depending on your internet connection.</h5>

<h4>Threader 3000 now has integrated Nmap functionality.  Run a scan against your target and then selecte the "Run suggested Nmap scan" option to execute a targetted nmap scan.</h4>

<h4>Requirements:</h4>
<h5>Python3 must be installed on your system in order to function</h5>

<h2>Installation</h2>
<h4>Installation via Pip</h4>
<h5>pip3 install threader3000</h5>
<h5>Run by typing "threader3000"</h5>
<h4>Install via Git</h4>

```bash
git clone https://github.com/dievus/threader3000.git #to save the program to your machine, or utilize the download option
```
You can add Threader3000 to run from any directory by adding a symbolic link:

```bash
sudo ln -s $(pwd)/threader3000.py /usr/local/bin/threader3000
```
<h2>Usage</h2>
<h4>You can load a list of hosts or scan only one host</h4>

```
Only one host e.g: localhost
List of hosts e.g: list.txt
At the moment, only accepts a list of hosts only .txt
```


***Disclaimer - This tool is under a free license for use, however it is up to the user to observe all applicable laws and appropriate uses for this tool.  The creator does not condone, support, suggest, or otherwise promote unethical or illegal behavior.  You use this tool at your own risk, and under the assumption that you are utilizing it against targets and infrastructure to which you have permission to do so.  Any use otherwise is at your peril and against the terms of use for the tool.***
