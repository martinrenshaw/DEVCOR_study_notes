# DEVCOR_study_notes

Note taking repo :weary:

---

## Mod 8 - Deploying Applications

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

---

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

sample script to interact with Cisco DNA

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

### 9.4 Event-Driven Architecture Concepts

flow of information is determined by the stream of events
Events are significant state changes inside a system.
Events do not travel outside the system, event notifications (or messages) do.

The EDA architecture can be implemented with two different types of topologies.

The mediator topology is used when there is a need for you to orchestrate several event steps through a central mediator, and the broker topology is better suited for chaining events together without a central mediator. It is important for you to know the differences between these two topologies in order to understand which one is better for your situation.

The architecture is comprised of three components:

- Event Emitter: Event emitters gather the state changes required for an event to happen within a system and send them to the event channel.

- Event Channel: Event channel is used to forward the events to an event consumer. It can also do some preprocessing of the events before they are sent. Event channels often include messaging queues, to distribute messages horizontally or to prevent the channel from being overwhelmed.

- Event Consumer: Event consumers are components that can perform a specific task, based on the event that is processed.

### 9.5 Microservice Architecture Concepts

Q. How can you efficiently scale an application when designing with microservices architecture?

A. An individual service can be deployed to a new machine, preferably in a **container**, and a **load balancer** needs to be configured for traffic balancing.

### 9.6 Effective Distributed Application Logging Strategies

The goal of distributed logging is to give you one place where you can find all the logs.

Q. Which process or property of the data is the most important for effective distributed logging?
A. data aggregation

### 9.7 Using Distributed Logging to Diagnose Problems

The primary concept of distributed tracing is to label the log when a request first appears in the system. As the request makes its journey, each log entry contains the same label that was assigned at the source of the request. This label indicates an activity that the system performs on each request. By using the label and the time stamp, you can quickly analyze the path or the activity that was performed on each request over multiple microservices.

OpenTracing and OpenCensus distributed tracing frameworks are now merged into a single project called OpenTelemetry, which is meant to replace both projects in the future.

Q. How can you achieve distributed tracing?
A. Assign the label when the request enters the system.

### 9.8 Diagnose Problems Using Application Logs

LAB

- Graylog server
- login admin/admin
- In the navigation bar, choose the System tab and then the Inputs option.

### 9.9 Application Monitoring with Cisco AppDynamics

As instrumentation code can observe the communication of application code with other systems, Cisco AppDynamics is able to create a map of application components and graphically represent how they communicate—an application topology, if you will.

Q. Which two types of monitoring agents are supported by Cisco AppDynamics? (Choose two.)
A. Machine
A. Application Server

### 9.10 Limitations of Distributed Systems and CAP Theorem

Networking Pitfalls

- Consistency: Responses provide up-to-date data or no data at all.

- Availability: Responses always provide data, even if it is not up-to-date.

- Partition tolerance: System continues operation in face of network failure.

Q. What does the CAP theorem state about a distributed system?
A. A system can be available and consistent if there are no network partitions.

### 9.11 Overcoming Challenges in Distributed Systems

Bulkhead pattern,
Circuit Breaker pattern,

### 9.12 Summary Challenge

1. Which statement describes horizontal scaling?
You increase the number of nodes that serve the same core application component.

1. What is REST?

1. Match the mediator topology architecture components with their respective descriptions.

1. Which statement about microservice architecture is correct?
Each microservice runs the code for a specific functionality within an application.

1. Which three options are components of the ELK stack? (Choose three.)
Elasticsearch
Logstash
Kibana

1. Which two options are examples of popular distributed tracing frameworks? (Choose two.)
OpenTracing
OpenCensus

1. Which mechanism does Cisco AppDynamics use in application component discovery and performance data collection?

1. Which two assumptions related to network programming are correct? (Choose two.)

1. Match the concepts with their respective descriptions.
A way to avoid split-brain behavior - Quorum
Isolates a single system failure - bulkhead pattern
Used for improved handling of timeouts - Circuit breaker pattern
A network of interconnected services - Service mesh

---
As discussed so far, the front-end components can access the back end using the API calls. There are a couple of technologies that you can use for exposing the applications back end using an API. The most popular technology for the API, at least for web applications, is REST. REST is a programmatic interface that can be used on web services for providing interoperability between applications components. API requests may be read-only queries with no side-effects or produce modifications of the resources.

REST APIs have become a standard for interacting with web services because of the following features:

Lightweight: You don't need to install special libraries, compile code, or have expert skills in any programming language to use a REST-enabled web service.

Flexible: You can use REST for simple requests or for complex operations.

Scalable: REST requests run on the web server, so their ability to scale is entirely a function of the server's abilities.

Platform-agnostic: Virtually any HTTP-enabled host can send REST requests and receive REST responses, whether on Windows, macOS, Linux or on a mobile device, such as a smart phone or a tablet.

REST is based on the HTTP request-response model. This model uses Hypertext Transfer Protocol (HTTP or HTTPS) to send a request to a web service, which returns a response.

The requests can be made with the following REST resource methods:

GET

PUT

PATCH

POST

DELETE

---

Mediator topology contains four different architecture components, where each one has its distinct role:

Event queue: A message queue that is used as an endpoint for events to be transported to the event mediator.

Event mediator: Central orchestration component that receives the initial event(s) and makes organized asynchronous calls to different event channels. The event mediator does not contain the logic to process the initial event, it only knows which steps it must take to process it.

Event channel: Used to pass processing events from the mediator to an event processor. These are usually implemented as message queues or event processors.

Event processor: Listens on event channels and executes suitable business logic, depending on the event. Each event processor should be a self-contained, independent, and loosely coupled component, that performs a very specific task within the system. It should not rely on other components, to perform its tasks

---

Application Server Agent: For analyzing and monitoring code

Machine Agent: For monitoring server utilization

End User Agent: For performance visibility from the end user perspective

---

The network is insecure.

Networking systems are diverse.

Systems may fall under different administrative domains.

The network introduces latency.

The network bandwidth is limited

---

## 10 Orchestrating Network and Infrastructure

### 10.2 Configuring Servers Using Cisco UCS APIs

```py
class UCS:
    def __init__(self, host, username, password):
        # Store argument values and instantiate the HTTPConnection class
        self.host = host
        self.username = username
        self.password = password
        self.cookie = None
        self.conn = http.client.HTTPConnection(self.host)

    def api_request(self, body):
    def login(self):
    def logout(self):
    def get_service_profile_templates(self):
    def create_service_profile(self, name, template):

    def api_request(self, body):
        # Initiate the request
        self.conn.request('POST', '/nuova', body)
        
        # Read the response
        api_response = self.conn.getresponse()
        
        # Store the status and data
        status = api_response.status
        data = api_response.read()

        return (status, data)

    def login(self):
    body = f'<aaaLogin inName="{self.username}" inPassword="{self.password}" />'

    response = self.api_request(body)
    if response[0] == 200:
        response_xml = xml.etree.ElementTree.fromstring(response[1])
        self.cookie = response_xml.attrib['outCookie']
        return self.cookie

    def logout(self):
        body = f'<aaaLogout inCookie="{self.cookie}" />'
        
        self.api_request(body)

    def get_service_profile_templates(self):
        body = f'<configResolveClasses cookie="{self.cookie}"><inIds><classId value="lsServer"/></inIds></configResolveClasses>'

        response = self.api_request(body)
        response_xml = xml.etree.ElementTree.fromstring(response[1])
            
        templates = {}
        out_configs = response_xml.find('outConfigs')
        for server in out_configs:
            if server.attrib['type'] == 'initial-template':
                templates[server.attrib['name']] = server.attrib['dn']

    return templates

    def create_service_profile(self, name, template):
        body = (
            f'<configConfMo dn="" cookie="{self.cookie}"><inConfig>'
            f'    <lsServer dn="org-root/ls-{name}"'
            f'                     name="{name}"'
            f'                     srcTemplName="{template}"/>'
            f'  </inConfig></configConfMo>'
        )
        response = self.api_request(body)
        return response

    if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', required=True)
    parser.add_argument('--prefix', required=True)
    parser.add_argument('--count', type=int, default=1)
    args = parser.parse_args()

    ucs = UCS(HOST, USERNAME, PASSWORD)
    ucs.login()
    if args.template in ucs.get_service_profile_templates():
        for i in range(args.count):
            name = f'{args.prefix}{str(i)}'
            response = ucs.create_service_profile(name, args.template)
            if response[0] == 200 and 'errorCode' not in str(response[1]):
                print(f'The service profile {name} created successfully.')
    ucs.logout()

```

```sh
~/$ python application.py --template template-web --prefix web-server --count 3
The service profile web-server0 created successfully.
The service profile web-server1 created successfully.
The service profile web-server2 created successfully.
```

### 10.3 Infrastructure as Code with Terraform
