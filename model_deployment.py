from azureml.core import Workspace
from azureml.core.model import Model

#ACI Deployment

from azureml.core.webservice import AciWebservice, Webservice 
from azureml.core.model import InferenceConfig 

# Connect to your Azure ML workspace
workspace = Workspace.get(name="PAIWP",
                          subscription_id="8ce46f80-4a45-4e79-a0d2-f29438358d73",
                          resource_group="Practice_AI")

# Register the model
model = Model.register(model_path="model.pkl",  # Path to the .pkl file
                       model_name="my_model",  # Name of the model for reference in Azure ML
                       workspace=workspace)


#DEPLOY THE MODEL USING AZURE ML FREE TIER

## STEP 1 - Create ACI Deployment Config
### Define ACI Config, specifying CPU and memory
aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1) 

## STEP 2 - Set Up Inference Config
### Create an inference conig using score.py and environment.yml
inference_config = InferenceConfig(runtime= "python", entry_script="score.py", conda_file="environment.yml") 

## STEP - 3 - Deploy the model
### Deploy the model using the Azure ML SDK
service = Model.deploy(workspace=workspace, name='nwo1', models=[model], inference_config=inference_config, deployment_config=aci_config)
service.wait_for_deployment(show_output=True)

