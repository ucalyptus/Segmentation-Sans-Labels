# Segmentation-Sans-Labels
ELEC 825 Project Code Release

## Segmentation Code Instructions
To perform segmentation on a pretrained generator, follow the ipynb notebook.

## Training StyleGANv2 on the anime dataset

```
cd stylegan2-pytorch
python train.py --batch 16 <path to dataset in LMDB format> --wandb
```
