# encoding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path as osp
import sys
import time
import numpy as np
from easydict import EasyDict as edict

C = edict()
config = C
cfg = C

C.seed = 12345

"""please config ROOT_dir and user when u first using"""
C.repo_name = 'AGD_SR'
C.abs_dir = osp.realpath(".")
C.this_dir = C.abs_dir.split(osp.sep)[-1]
C.root_dir = C.abs_dir[:C.abs_dir.index(C.repo_name) + len(C.repo_name)]
C.log_dir = osp.abspath(osp.join(C.root_dir, 'log', C.this_dir))
C.log_dir_link = osp.join(C.abs_dir, 'log')
C.snapshot_dir = osp.abspath(osp.join(C.log_dir, "snapshot"))

exp_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
C.log_file = C.log_dir + '/log_' + exp_time + '.log'
C.link_log_file = C.log_file + '/log_last.log'
C.val_log_file = C.log_dir + '/val_' + exp_time + '.log'
C.link_val_log_file = C.log_dir + '/val_last.log'

"""Data Dir and Weight Dir"""
# C.dataset_path = "/home/yf22/dataset/DIV2K_bibubic"
C.dataset_path = "/data4/low_res2"

"""Path Config"""
def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

add_path(osp.join(C.root_dir, 'furnace'))

"""Image Config"""

C.num_train_imgs = 3450
C.num_eval_imgs = 100

""" Settings for network, this would be different for each kind of model"""
C.bn_eps = 1e-5
C.bn_momentum = 0.1

"""Train Config"""



# C.lr = 0.0001
# C.lr_decay = 1

C.opt = 'Adam'

C.momentum = 0.9
C.weight_decay = 5e-4

C.betas = (0.9, 0.999)
C.num_workers = 4

""" Search Config """
C.grad_clip = 5

# C.layers = 30
C.num_cell = 5
C.op_per_cell = 5

C.pretrain = True
# C.pretrain = 'ckpt/pretrain'
########################################
C.prun_modes = 'arch_ratio'

# C.width_mult_list = [4./12, 6./12, 8./12, 10./12, 1.]
C.width_mult_list = [6./12, 8./12, 10./12, 1.]

C.loss_func = 'L1'

C.before_act = True

if C.pretrain == True:
    C.batch_size = 6
    C.niters_per_epoch = C.num_train_imgs // 2 // C.batch_size
    C.latency_weight = [0, 0]
    C.image_height = 32 # this size is after down_sampling
    C.image_width = 32
    C.save = "pretrain"

    scale = 0.05

    # C.nepochs = int(8000*scale)
    # C.eval_epoch = int(400*scale)

    C.nepochs = 100
    C.eval_epoch = 20

    C.lr_schedule = 'multistep'
    C.lr = 2e-4
    # linear 
    C.decay_epoch = 300
    # exponential
    C.lr_decay = 0.97
    # multistep
    # C.milestones = [int(1000*scale), int(2000*scale), int(4000*scale), int(6000*scale)]
    C.milestones = [25, 50, 75]
    C.gamma = 0.5

    # C.loss_weight = [1, 0, 0.006, 2e-8]
    C.loss_weight = [1, 0, 0, 0]

else:
    C.batch_size = 6
    C.niters_per_epoch = C.num_train_imgs // 2 // C.batch_size
    C.latency_weight = [0, 1e-2,]
    C.image_height = 32 # this size is after down_sampling
    C.image_width = 32
    C.save = "search"

    scale = 0.05

    # C.nepochs = int(8000*scale)
    # C.eval_epoch = int(400*scale)

    C.nepochs = 100
    C.eval_epoch = 20

    C.lr_schedule = 'multistep'
    C.lr = 1e-4
    # linear 
    C.decay_epoch = 300
    # exponential
    C.lr_decay = 0.97
    # multistep
    C.milestones = [25, 50, 75]
    C.gamma = 0.5

    # C.loss_weight = [1, 0, 0.006, 2e-8]
    C.loss_weight = [1e-2, 0, 1, 0]

########################################

C.ENABLE_BN = False

C.ENABLE_TANH = True

C.quantize = False

C.slimmable = True

C.train_portion = 0.5

C.unrolled = False

C.arch_learning_rate = 3e-4

C.alpha_weight = 2/7
C.ratio_weight = 5/7
C.beta_weight = 0
C.flops_weight = 0

C.flops_max = 400e9

C.flops_min = 100e9

# C.loss_weight = [1e-2, 0, 1, 0]

C.generator_A2B = 'ESRGAN/RRDB_ESRGAN_x4.pth'
