GET CLOUDIER Windows CI/CD - Bamboo for CI and AWS Codedeploy for Deployments

git push

and then...

tail logs for a deployment here:
> Get-Content C:\ProgramData\Amazon\CodeDeploy\0ff22760-afdb-4c5f-966e-c09145052fbf\deployment-id\logs\scripts.log –Wait

future scripts to start / stop IIS and register / deregister from ELB / ALB
https://github.com/brianlund/codedeploy-elb-powershell