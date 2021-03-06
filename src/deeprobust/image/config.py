import numpy as np
# ---------------------attack config------------------------#
attack_params = {
    "FGSM_MNIST": {
    'epsilon': 8/255,
    'order': np.inf,
    'clip_max': 1.0,
    'clip_min': 0.0
    },

    "PGD_CIFAR10": {
    'epsilon': 8/255,
    'clip_max': 1.0,
    'clip_min': 0.0,
    'print_process': False
    },
    "FGSM_CIFAR": {
    'epsilon': 8/255,
    'order': np.inf,
    'clip_max': 1.0,
    'clip_min': 0.0
    },

    "LBFGS_MNIST": {
    'epsilon': 1e-4,
    'maxiter': 20,
    'clip_max': 1,
    'clip_min': 0,
    'class_num': 10
    },

    "CW_MNIST": {
    'confidence': 1e-4,
    'clip_max': 1,
    'clip_min': 0,
    'max_iterations': 1000,
    'initial_const': 1e-2,
    'binary_search_steps': 5,
    'learning_rate': 5e-3,
    'abort_early': True,
    }

}

#-----------defense(Adversarial training) config------------#

defense_params = {
    "PGDtraining_MNIST":{
        'save_dir': "./defense_model",
        'save_model': True,
        'save_name' : "mnist_fgsmtraining_0.2.pt",
        'epsilon' : 0.3,
        'epoch_num' : 1000,
        'lr' : 0.001
    },
    "PGDtraining_CIFAR10":{
        'save_dir': "./defense_model",
        'save_model': True,
        'save_name' : "cifar10_pgdtraining_0.2.pt",
        'epsilon' : 8/255,
        'epoch_num' : 100,
        'lr' : 0.001
    },
    "PGDtraining_CIFAR10_RESNET":{
        'save_dir': "./defense_model",
        'save_model': True,
        'save_name' : "cifar10_RESNET_pgdtraining_0.2.pt",
        'epsilon' : 8/255,
        'epoch_num' : 100,
        'lr' : 0.001
    },

    "FGSMtraining_MNIST":{
        'save_dir': "./defense_model",
        'save_model': True,
        'save_name' : "mnist_fgsmtraining_0.2.pt",
        'epsilon' : 0.2,
        'epoch_num' : 50,
        'lr_train' : 0.001
    },

    "FAST_MNIST":{
        'save_dir': "./defense_model",
        'save_model': True,
        'save_name' : "fast_mnist_0.3.pt",
        'epsilon' : 0.3,
        'epoch_num' : 50,
        'lr_train' : 0.001
    }
}

