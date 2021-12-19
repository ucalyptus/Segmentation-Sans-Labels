import torch
import wandb
api = wandb.Api()
runid = "3hm84qqd"
run = api.run("ucalyptus/seginstyle/" + runid)
run.upload_file("checkpoint/290000.pt")
