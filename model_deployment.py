from azureml.core import Workspace
from azureml.core.model import Model

# Connect to your Azure ML workspace
workspace = Workspace.get(name="PAIWP",
                          subscription_id="8ce46f80-4a45-4e79-a0d2-f29438358d73",
                          resource_group="Practice_AI")

# Register the model
model = Model.register(model_path="model.pkl",  # Path to the .pkl file
                       model_name="my_model",  # Name of the model for reference in Azure ML
                       workspace=workspace)
