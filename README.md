# DEVCOR_study_notes
Note taking repo




Mod 8 - Deploying Applications

##################################################################################################################################################

8.1 - 12-Factor App Methodology

eveolved from the cloud/PaaS deployments.

https://12factor.net - Heroku

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


##################################################################################################################################################

8.2 - Containerize Applications using Docker






minikube 
