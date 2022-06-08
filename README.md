# DEVCOR_study_notes

Note taking repo

## Mod 8 - Deploying Applications

---

### 8.1 - 12-Factor App Methodology

eveolved from the cloud/PaaS deployments.

<https://12factor.net> - Heroku

Codebase - One code base, saved in VCS (version control sys) - ideally same repo
multiple ENVs, testing, staging, prod....

Dependencies - explicitly declare and isolate dependencies, i.e python local ENV, Conntainers..

Configuration - never part of the src code, instead use ENV vars, watch out for security as others might be able to see them,  supply the runtime info with orchatration.

Backing services - treat backing services as attached resources, easy to replace and move

Stages -  strictly seperate build, run stages.

Processes - execute the app as one or more stateless process,

Port Binding - seperate apps so that they can run anywhere on the network.

Concurrency - scale out via the process model,

Disposability - fast startup and graceful shutdown, faststart containers, fronted by LB,

Dev/Prod - keep dev, stage and prod as similar as possible.

logs - send logs outside of the app to someother entity.

admin process - admin/mgmt tasks as oneoff processess.

---

### 8.2 - Containerize Applications using Docker

minikube

this is extra

> blockquote

` some code here `

```python
some
code
block here
```

## Mod 9 - Understanding Distributed Systems

- when writing a new application, where might performance issues arise as you scale?
- At what threshold do the benifits of a distributed system outweigh the challenges?

### 9.2 - Distributed Application Concepts

monolith - spof
three tier - layer architecture for, use dns or lb to distribue. flexible and convenient for development and scaling.

HAProxy software lb - l4 or l7 LB, frontend(VIP listner), backend(pool of servers)
could also use NGINX from F5 to do similar tasks.

What is the advantage of application-layer load balancers?
They can load-balance traffic based on the request resource.

### 9.3 Custom Dashboard Example

- frontend - HTML, Cascading Style Sheets (CSS), JavaScript, .NET, react.js, Angular, and similar frameworks whose goal is to present the data to the user in a structured, understandable way, aiming for the best user experience.

- backend - PHP, Python, Ruby, Java, .NET, and so on. The back-end sets the default behavior of the application state. It defines rules what can be done on the state and how the front end can interact with the core of the application.

```python
import requests

base_url = 'https://<IP or hostname>'
r = requests.post(f'{base_url}/dna/system/api/v1/auth/token',
                         auth=('<USERNAME>', '<PASSWORD>'))
r.raise_for_status()
token = r.json()['Token']

headers = {'X-Auth-Token': token}
r = requests.get(f'{base_url}/dna/intent/api/v1/site-health', headers=headers)
r.raise_for_status()
sites = r.json()['response']
```