# AI

### Environment Requirement

1. Ubuntu 18.04

2. Anaconda 

3. Nvidia driver. (Make sure able to run `nvidia-smi` in terminal.)


### Installation for development

1. conda create -n <env_name> python=3.7.9

2. cd ai and run `pip install -r requirements.txt`


### Download and Compile Model 

1. cd ./face-compare-matching-service/src/provider

2. Paste model to this folder



### Run Service

1. Run main agent service using `python main.py`


### Branch Strategy

1. Branching strategy:
   - **main** 
   - **develop** 
   - **feature/{ feature-name in lowercase, dash separate }** 
   - **refactor/{ context in lowercase, dash separate }** 

2. Checkout new branch in context ex:
```
git checkout -b feature/new-feature
```





